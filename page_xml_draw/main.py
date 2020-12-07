from page_xml_draw.argparse import get_options
from page_xml_draw.xml import Page
from page_xml_draw.graphics import Overlay

def main():
  # Return parsed user selected parameters:
  opt = get_options()

  # Fetch PAGE-XML file tree:
  page = Page(opt.input, opt.anottations)

  image_path = opt.base_dir / page.get_image_filename()

  overlay = Overlay(image_path, page, opt.anottations)

  overlay.save(opt.output)

if __name__ == "__main__":
  main()
