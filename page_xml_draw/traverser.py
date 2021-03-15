import pathlib
import numpy as np
import cv2
import webcolors

from page_xml_draw.html.image_map import Map, ImageMap


class Color:
    def __init__(self, string):
        if string in webcolors.CSS3_NAMES_TO_HEX:
            self.name = string
            self.hex = webcolors.name_to_hex(string, spec=webcolors.CSS3)
        else:
            self.name = None
            self.hex = string

    def to_rgb(self):
        return webcolors.hex_to_rgb(self.hex)

    def to_bgr(self):
        r, g, b = self.to_rgb()
        return b, g, r

    def to_hashless_hex(self):
        return self.hex[1:]


class Traverser():
    '''
    PAGE-XML tree traverser and layout annotation drawer
    '''
    def __init__(self, tree, base_dir):
        self.tree = tree

        # Resolve path to image referenced by PAGE-XML file:
        image_path = base_dir / pathlib.Path(self.tree.get_imageFilename())

        # Read image:
        self.image = cv2.imread(str(image_path))

        self.name = None

        # Focused nodes of the tree (root at start):
        self.focused = self.tree

        # Stack of parent nodes of focused:
        self.parent_stack = []

        # Mask for drawing the color values:
        self.color_mask = np.zeros_like(self.image)

        # Mask for drawing the opacity values:
        self.weight_mask = np.zeros(
            (self.image.shape[0], self.image.shape[1], 1),
            dtype=np.float
        )

        self.image_map = ImageMap(self.tree.get_imageFilename())

    def focus_on_children(self, name):
        '''
        Move focus to children nodes with given name
        '''
        # Save focused nodes as parents:
        self.parent_stack.append((self.name, self.focused))

        self.name = name

        if isinstance(self.focused, list):
            children = []

            for element in self.focused:
                # Get child node by name:
                getter = getattr(element, "get_" + name)
                child = getter()

                if isinstance(child, list):
                    children += child
                else:
                    children.append(child)

            self.focused = children
        else:
            # Get child node by name:
            getter = getattr(self.focused, "get_" + name)
            self.focused = getter()

    def focus_on_parents(self):
        '''
        Move focus back to parent nodes
        '''
        self.name, self.focused = self.parent_stack.pop()

    def draw_focused(self, fill_color, edge_color, edge_thickness, opacity):
        '''
        Draw polygons associated to focused nodes
        '''
        if isinstance(self.focused, list):
            polygons = [np.array(elm.get_polygon()) for elm in self.focused]
        else:
            polygons = [np.array(self.focused.get_polygon())]

        if fill_color:
            # Wrap in color object:
            fill_color = Color(fill_color)

            # Fill polygons of color mask:
            cv2.fillPoly(
                self.color_mask,
                polygons,
                fill_color.to_bgr()
            )

            # Fill polygons of weight mask (with opacity value):
            cv2.fillPoly(
                self.weight_mask,
                polygons,
                opacity
            )

        if edge_color:
            # Wrap in color object:
            edge_color = Color(edge_color)

            # Draw polygon edges of color mask:
            cv2.polylines(
                self.color_mask,
                polygons,
                True,
                edge_color.to_bgr(),
                edge_thickness
            )

            # Draw polygon edges of weight mask (with opacity value):
            cv2.polylines(
                self.weight_mask,
                polygons,
                True,
                opacity,
                edge_thickness
            )

    def map_focused(self, fill_color, edge_color, edge_thickness, opacity):
        '''
        Map polygons associated to focused nodes
        '''
        if isinstance(self.focused, list):
            polygons = [elm.get_polygon() for elm in self.focused]
        else:
            polygons = [self.focused.get_polygon()]

        # TODO: User method for pairs of points?
        polygons = [
            ','.join(
                [','.join([str(point) for point in pairs]) for pairs in poly]
            ) for poly in polygons
        ]

        # Create map for polygons and append to image map:
        self.image_map.add_map(Map(self.name, Color(fill_color).to_hashless_hex(), opacity, polygons))

    def overlay(self):
        '''
        Overlay image with drawn polygons
        '''
        image = self.image * (1.0 - self.weight_mask)
        overlay = self.color_mask * self.weight_mask

        return image + overlay

    def render(self):
        return self.image_map.render()
