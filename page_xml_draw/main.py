from pathlib import Path

from page_xml_draw.struct.xml import XmlTraverser
from page_xml_draw.struct.json import JsonInstance
from page_xml_draw.cli import get_opts
from page_xml_draw.core import ImageDrawer


def main() -> None:
    in_file: Path
    out_file: Path
    base_dir: Path
    output_format: str
    styles: JsonInstance
    drawer: ImageDrawer

    in_file, out_file, base_dir, output_format, styles = get_opts()

    drawer = ImageDrawer(
        XmlTraverser(str(in_file)),
        styles,
        base_dir=base_dir
    )

    if output_format == "image/png":
        drawer.draw().save(out_file)
    elif output_format == "text/html":
        drawer.map().save(out_file)
