from __future__ import annotations

import numpy as np
import cv2

from pathlib import Path

from page_xml_draw.struct.xml import XmlTag, XmlTraverser
from page_xml_draw.struct.json import JsonInstance
from page_xml_draw.struct.html import HtmlMap
from page_xml_draw.gends.page import PcGtsType
from page_xml_draw.styles import StyleSpec

PAGE_ATTRIBUTES = set([
    'Page',
    'Border',
    'PrintSpace',
    'TextRegion',
    'ImageRegion',
    'LineDrawingRegion',
    'GraphicRegion',
    'TableRegion',
    'ChartRegion',
    'MapRegion',
    'SeparatorRegion',
    'MathsRegion',
    'ChemRegion',
    'MusicRegion',
    'AdvertRegion',
    'NoiseRegion',
    'UnknownRegion',
    'CustomRegion',
    'TextLine',
    'Word',
    'Glyph',
    'Graphemes',
    'Grapheme'
])

STYLE_ATTRIBUTES = set([
    'FillColor',
    'FillOpacity',
    'StrokeColor',
    'StrokeOpacity',
    'StrokeWidth'
])


class Drawing:
    result: np.ndarray

    def __init__(self, pcgts: PcGtsType, specs: list[StyleSpec],
                 base_dir: Path = None) -> Drawing:
        image_path: Path
        color_mask: np.ndarray
        weight_mask: np.ndarray

        image_path = Path(pcgts.get_imageFilename())

        if base_dir is not None:
            image_path = base_dir / image_path

        image = cv2.imread(str(image_path))

        color_mask = np.zeros_like(image)

        weight_mask = np.zeros(
            (image.shape[0], image.shape[1], 1),
            dtype=np.float
        )

        for spec in specs:
            spec.draw(color_mask, weight_mask)

        image = image * (1.0 - weight_mask)
        overlay = color_mask * weight_mask

        self.result = image + overlay

    def save(self, output_path: Path) -> None:
        cv2.imwrite(str(output_path), self.result)


class ImageMap:
    def __init__(self, pcgts: PcGtsType, specs: list[StyleSpec],
                 base_dir: Path = None) -> ImageMap:
        image_path: Path
        html_map: HtmlMap

        image_path = Path(pcgts.get_imageFilename())

        if base_dir is not None:
            image_path = base_dir / image_path

        html_map = HtmlMap(image_path)

        for spec in specs:
            spec.map(html_map)

        self.result = html_map.render()

    def save(self, output_path: Path) -> None:
        with output_path.open(mode='w') as fp:
            fp.write(self.result)


class ImageDrawer:
    traverser: XmlTraverser
    specs: list[StyleSpec]
    styles: JsonInstance
    base_dir: Path

    def __init__(self, traverser: XmlTraverser, styles: JsonInstance,
                 base_dir: Path = None) -> ImageDrawer:
        self.traverser = traverser
        self.specs = []
        self.styles = styles
        self.base_dir = base_dir

    def traverse(self, styles: JsonInstance = None) -> None:
        if styles is None:
            styles = self.styles

        if styles & STYLE_ATTRIBUTES:
            self.specs.append(StyleSpec(self.traverser.focused, styles))

        for key in styles & PAGE_ATTRIBUTES:
            self.traverser.focus_on_children(key)
            self.traverse(styles[key])
            self.traverser.focus_on_parents()

    def draw(self) -> None:
        return Drawing(self.traverser.pcgts, self.specs, self.base_dir)

    def map(self) -> None:
        return ImageMap(self.traverser.pcgts, self.specs, self.base_dir)
