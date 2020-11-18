import argparse
import xml.etree.ElementTree as ET
import pathlib
import webcolors as wc

#Default values:
default_color = 0x0000FF
default_alpha = 0.3
default_thickness = 3

# https://stackoverflow.com/questions/12116685/how-can-i-require-my-python-scripts-argument-to-be-a-float-between-0-0-1-0-usin
def restricted_float(x):
  try:
    x = float(x)
  except ValueError:
    raise argparse.ArgumentTypeError("%r not a floating-point literal" % (x,))

  if x < 0.0 or x > 1.0:
    raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]" % (x,))

  return x

def css3_rgb(x):
  if x in wc.CSS3_NAMES_TO_HEX:
    x = wc.name_to_rgb(x, spec=wc.CSS3)
  else:
    x = wc.hex_to_rgb("#" + x)

  r, g, b = x

  return b, g, r

def path(x):
  return pathlib.Path(x)

class Element:
  def __init__(self, fill_color=default_color, outline_color=default_color, thickness=default_thickness, alpha=default_alpha):
    self.fill_color = fill_color
    self.outline_color = outline_color
    self.thickness = thickness
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
    namespace.border = Element()

    # Save current element:
    namespace.cur_element = namespace.border

class TextRegionsAction(argparse.Action):
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Store true and initialize values:
    namespace.text_regions = Element()

    # Save current element:
    namespace.cur_element = namespace.text_regions

class TextLinesAction(argparse.Action):
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Store true and initialize values:
    namespace.text_lines = Element()

    # Save current element:
    namespace.cur_element = namespace.text_lines

class FillColorAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set color of current element:
    namespace.cur_element.fill_color = values

class OutlineColorAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set color of current element:
    namespace.cur_element.outline_color = values

class ThicknessAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set thickness of current element:
    namespace.cur_element.thickness = values

class AlphaAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set alpha of current element:
    namespace.cur_element.alpha = values

def get_options():
  parser = argparse.ArgumentParser()

  parser.add_argument("-i", "--input", type=path, dest="input", required=True, help="")
  parser.add_argument("-o", "--output", type=path, dest="output", required=True, help="")
  parser.add_argument("--base-dir", type=path, dest="base_dir", default=pathlib.Path.cwd(), help="")
  parser.add_argument("--border", dest="border", default=None, action=BorderAction, help="")
  parser.add_argument("--text-regions", dest="text_regions", default=None, action=TextRegionsAction, help="")
  parser.add_argument("--text-lines", dest="text_lines", default=None, action=TextLinesAction, help="")
  parser.add_argument("--fill-color", type=css3_rgb, action=FillColorAction, help="")
  parser.add_argument("--outline-color", type=css3_rgb, action=OutlineColorAction, help="")
  parser.add_argument("--thickness", type=int, action=ThicknessAction, help="")

  options = parser.parse_args(namespace=MyNamespace())

  return options
