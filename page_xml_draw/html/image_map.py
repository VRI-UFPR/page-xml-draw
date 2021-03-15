import pkg_resources
import jinja2


class Map():
    def __init__(self, typ, FillColor, Opacity, polygons):
        self.type = typ
        self.FillColor = FillColor
        self.Opacity = Opacity
        self.polygons = polygons


class ImageMap():
    def __init__(self, imageFilename):
        self.imageFilename = imageFilename

        self.template = jinja2.Template(
            str(
                pkg_resources.resource_string(
                    __name__,
                    "template.html.j2"
                ),
                'utf-8'
            )
        )

        self.maps = []

    def add_map(self, map):
        self.maps.append(map)

    def render(self):
        return self.template.render(
            image_filename=self.imageFilename,
            maps=self.maps
        )
