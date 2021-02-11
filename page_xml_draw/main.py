import cv2

from page_xml_draw.cli import get_opts
from page_xml_draw.gends.page import parse
from page_xml_draw.drawer import Drawer
from page_xml_draw.json.instance import Instance


def main():
    # Get options from CLI:
    in_file, out_file, base_dir, instance = get_opts()

    # Parse PAGE-XML file and pass it to drawer:
    drawer = Drawer(parse(str(in_file), silence=True), base_dir)

    # Wrap JSON instance representing the profile:
    instance = Instance(instance, drawer)

    # Traverse the PAGE-XML tree and draw the annotations:
    instance.traverse_and_draw()

    # Retrieve overlay and write it to output file:
    cv2.imwrite(str(out_file), drawer.overlay())
