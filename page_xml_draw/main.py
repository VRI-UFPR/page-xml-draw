import cv2

from page_xml_draw.cli import get_opts
from page_xml_draw.gends.page import parse
from page_xml_draw.traverser import Traverser
from page_xml_draw.json.instance import Instance


def main():
    # Get options from CLI:
    in_file, out_file, base_dir, mode, instance = get_opts()

    # Parse PAGE-XML file and pass it to traverser:
    traverser = Traverser(parse(str(in_file), silence=True), base_dir)

    # Wrap JSON instance representing the profile:
    instance = Instance(instance, traverser)

    if mode == "image":
        # Traverse the PAGE-XML tree and draw the annotations:
        instance.traverse_and_draw()

        # Retrieve overlay and write it to output file:
        cv2.imwrite(str(out_file), traverser.overlay())
    elif mode == "image-map":
        # Traverse the PAGE-XML tree and map the annotations:
        instance.traverse_and_map()

        # Render image map ans write it to output file:
        with out_file.open(mode='w') as fp:
            fp.write(traverser.render())
