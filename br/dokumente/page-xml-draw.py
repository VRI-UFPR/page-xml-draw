#! /usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET
import pathlib
import numpy as np
import cv2
import webcolors as wc

# Default values:
default_color = (0, 0, 255) # Red
default_alpha = 0.3

# https://stackoverflow.com/questions/12116685/how-can-i-require-my-python-scripts-argument-to-be-a-float-between-0-0-1-0-usin

def restricted_float(x):
  try:
    x = float(x)
  except ValueError:
    raise argparse.ArgumentTypeError("%r not a floating-point literal" % (x,))

  if x < 0.0 or x > 1.0:
    raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]" % (x,))

  return x

def rgb_to_bgr(color):
  r, g, b = color
  return b, g, r

def css3_rgb(x):
  if x in wc.CSS3_NAMES_TO_HEX:
    x = wc.name_to_rgb(x, spec=wc.CSS3)
  else:
    x = wc.hex_to_rgb("#" + x)

  return rgb_to_bgr(x)

class Element:
  def __init__(self, color, alpha):
    self.color = color
    self.alpha = alpha

class MyNamespace(argparse.Namespace):
  cur_element = None

# https://stackoverflow.com/questions/21879657/argparse-argument-dependency
# https://stackoverflow.com/questions/11001678/argparse-custom-action-with-no-argument

class BorderAction(argparse.Action):
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Store true and initialize values:
    namespace.border = Element(default_color, default_alpha)

    # Save current element:
    namespace.cur_element = namespace.border

class TextRegionsAction(argparse.Action):
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Store true and initialize values:
    namespace.text_regions = Element(default_color, default_alpha)

    # Save current element:
    namespace.cur_element = namespace.text_regions

class TextLinesAction(argparse.Action):
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Store true and initialize values:
    namespace.text_lines = Element(default_color, default_alpha)

    # Save current element:
    namespace.cur_element = namespace.text_lines

class ColorAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set color of current element:
    namespace.cur_element.color = values

class AlphaAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set alpha of current element:
    namespace.cur_element.alpha = values

def get_options():
  parser = argparse.ArgumentParser()

  parser.add_argument("-i", "--input", dest="input", required=True, help="")
  parser.add_argument("-o", "--output", dest="output", required=True, help="")
  parser.add_argument("-d", "--base-dir", dest="base_dir", default=pathlib.Path.cwd(), help="")
  parser.add_argument("-b", "--border", dest="border", default=None, action=BorderAction, help="")
  parser.add_argument("-r", "--text-regions", dest="text_regions", default=None, action=TextRegionsAction, help="")
  parser.add_argument("-l", "--text-lines", dest="text_lines", default=None, action=TextLinesAction, help="")
  parser.add_argument("-c", "--color", type=css3_rgb, action=ColorAction, help="")
  parser.add_argument("-a", "--alpha", type=restricted_float, action=AlphaAction, help="")

  options = parser.parse_args(namespace=MyNamespace())

  options.input = pathlib.Path(options.input)
  options.output = pathlib.Path(options.output)

  if options.base_dir:
    options.base_dir = pathlib.Path(options.base_dir)
  else:
    options.base_dir = option.input.parent

  return options

def get_element(parent, name):
  element = None

  for child in parent:
    if child.tag.endswith(name):
      element = child

  return element

def get_elements(parent, name):
  elements = []

  for child in parent:
    if child.tag.endswith(name):
      elements.append(child)

  return elements

def get_page(root):
  return get_element(root, "Page")

def get_border(page):
  return get_element(page, "Border")

def get_regions(page):
  return get_elements(page, "TextRegion")

def get_lines(region):
  return get_elements(region, "TextLine")

def get_polygon(element):
  coords = get_element(element, "Coords")
  point_string = coords.attrib['points']

  polygon = []
  for point in point_string.split(" "):
    polygon.append([int(p) for p in point.split(",")])

  return np.array(polygon)

def overlay_image(image, polygons, color, alpha):
  overlay = image.copy()

  #cv2.polylines(image, [border_points], True, (0, 0, 255), 3)
  cv2.fillPoly(overlay, polygons, color)
  return cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

if __name__ == "__main__":
  options = get_options()

  tree = ET.parse(str(options.input))
  root = tree.getroot()

  page = get_page(root)

  image_path = options.base_dir / page.attrib['imageFilename']
  image = cv2.imread(str(image_path))

  if options.border is not None:
    border = get_border(page)
    polygon = get_polygon(border)

    image = overlay_image(image, [polygon], options.border.color, options.border.alpha)

  regions = None

  if options.text_regions is not None:
    regions = get_regions(page)

    polygons = []
    for region in regions:
      polygons.append(get_polygon(region))

    image = overlay_image(image, polygons, options.text_regions.color, options.text_regions.alpha)

  if options.text_lines is not None:
    if regions is None:
      regions = get_regions(page)

    polygons = []
    for region in regions:
      lines = get_lines(region)

      for line in lines:
        polygons.append(get_polygon(line))

    image = overlay_image(image, polygons, options.text_lines.color, options.text_lines.alpha)

  cv2.imwrite(str(options.output), image)
