from __future__ import annotations

from pkg_resources import resource_string
from jinja2 import Template


class HtmlArea:
    key: str
    polygon: str
    fill_color: str
    fill_opacity: float
    stroke_color: str
    stroke_opacity: float
    stroke_width: int

    def __init__(self, key: str, polygon: str, fill_color: str,
                 fill_opacity: float, stroke_color: str, stroke_opacity: float,
                 stroke_width: int) -> HtmlArea:
        self.key = key
        self.polygon = polygon
        self.fill_color = fill_color
        self.fill_opacity = fill_opacity
        self.stroke_color = stroke_color
        self.stroke_opacity = stroke_opacity
        self.stroke_width = stroke_width


class HtmlMap:
    image_path: str
    areas: list[HtmlArea]
    template: Template

    def __init__(self, image_path: str) -> HtmlMap:
        self.image_path = image_path
        self.areas = []

        string = str(resource_string(__name__, "template.html.j2"), "utf-8")
        self.template = Template(string)

    def add_area(self, area: HtmlArea) -> None:
        self.areas.append(area)

    def render(self) -> str:
        return self.template.render(
            image_path=self.image_path,
            areas=self.areas
        )
