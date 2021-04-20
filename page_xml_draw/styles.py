from __future__ import annotations

import numpy as np
import cv2

from webcolors import CSS3, CSS3_NAMES_TO_HEX, name_to_hex, hex_to_rgb

from page_xml_draw.struct.xml import XmlTag
from page_xml_draw.struct.json import JsonInstance
from page_xml_draw.struct.html import HtmlMap, HtmlArea

FALLBACK_OPACITY = 0.3
FALLBACK_THICKNESS = 1


class Color:
    name: str
    hex: str

    def __init__(self, string: str) -> Color:
        if string in CSS3_NAMES_TO_HEX:
            self.name = string
            self.hex = name_to_hex(string, spec=CSS3)
        else:
            self.name = None
            self.hex = string

    def to_rgb(self) -> tuple[int, int, int]:
        return hex_to_rgb(self.hex)

    def to_bgr(self) -> tuple[int, int, int]:
        r, g, b = self.to_rgb()
        return b, g, r

    def to_hashless_hex(self) -> str:
        return self.hex[1:]


class StyleSpec:
    tag: XmlTag
    instance: JsonInstance
    fill_color: Color
    fill_opacity: float
    stroke_color: Color
    stroke_opacity: float
    stroke_width: int

    def __init__(self, tag: XmlTag, instance: JsonInstance) -> StyleSpec:
        self.tag = tag
        self.instance = instance

        if 'FillColor' in self.instance:
            self.fill_color = Color(instance['FillColor'])

            if 'FillOpacity' in instance:
                self.fill_opacity = instance['FillOpacity']
            else:
                self.fill_opacity = FALLBACK_OPACITY
        else:
            self.fill_color = None
            self.fill_opacity = None

        if 'StrokeColor' in instance:
            self.stroke_color = Color(instance['StrokeColor'])

            if 'StrokeOpacity' in instance:
                self.stroke_opacity = instance['StrokeOpacity']
            else:
                self.stroke_opacity = FALLBACK_OPACITY

            if 'StrokeWidth' in instance:
                self.stroke_width = instance['StrokeWidth']
            else:
                self.stroke_width = FALLBACK_THICKNESS
        else:
            self.stroke_color = None
            self.stroke_opacity = None
            self.stroke_width = None

    def draw(self, color_mask: np.ndarray, weight_mask: np.ndarray) -> None:
        polygons = [np.array(elm.get_polygon()) for elm in self.tag.elements]

        if self.fill_color:
            cv2.fillPoly(
                color_mask,
                polygons,
                self.fill_color.to_bgr()
            )

            cv2.fillPoly(
                weight_mask,
                polygons,
                self.fill_opacity
            )

        if self.stroke_color:
            cv2.polylines(
                color_mask,
                polygons,
                True,
                self.stroke_color.to_bgr(),
                self.stroke_width
            )

            cv2.polylines(
                weight_mask,
                polygons,
                True,
                self.stroke_opacity,
                self.stroke_width
            )

    def map(self, html_map: HtmlMap) -> None:
        for elm in self.tag.elements:
            html_map.add_area(
                HtmlArea(
                    self.tag.name + "," + elm.get_id(),
                    elm.get_polygon_string(),
                    self.fill_color,
                    self.fill_opacity,
                    self.stroke_color,
                    self.stroke_opacity,
                    self.stroke_width
                )
            )
