import argparse
import pathlib

import page_xml_draw.graphics as graphics

class Namespace(argparse.Namespace):
  # Dict representing the anottations to be drawn and their properties:
  anottations = {}

  # Most recent anottation:
  most_recent = None

  def new_anottation(self, name):
    # Add new anottation entry:
    self.anottations[name] = {}

    # Register most recent anottation:
    self.most_recent = self.anottations[name]

  def new_property(self, key, value):
    # Add new property to the most recent anottation:
    self.most_recent[key] = value

class BackgroundAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('Background')

class BorderAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('Border')

class PrintSpaceAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('PrintSpace')

class TextRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('TextRegion')

class ImageRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('ImageRegion')

class LineDrawingRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('LineDrawingRegion')

class GraphicRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('GraphicRegion')

class TableRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('TableRegion')

class ChartRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('ChartRegion')

class SeparatorRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('SeparatorRegion')

class MathsRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('MathsRegion')

class ChemRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('ChemRegion')

class MusicRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('MusicRegion')

class AdvertRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('AdvertRegion')

class NoiseRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('NoiseRegion')

class UnknownRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('UnknownRegion')

class CustomRegionsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('CustomRegion')

class TextLinesAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('TextLine')

class WordsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('Word')

class GlyphsAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('Glyph')

class GraphemesAction(argparse.Action):
  # Argumentless option:
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)

  def __call__(self, parser, namespace, values, option_string=None):
    # Append new anottation:
    namespace.new_anottation('Grapheme')

class FillColorAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set property 'FillColor' of most recent anottation:
    namespace.new_property('FillColor', values)

class EdgeColorAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set property 'EdgeColor' of most recent anottation:
    namespace.new_property('EdgeColor', values)

class EdgeThicknessAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set property 'EdgeThickness' of most recent anottation:
    namespace.new_property('EdgeThickness', values)

class OpacityAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    # Set property 'Opacity' of most recent anottation:
    namespace.new_property('Opacity', values)

def get_options():
  # Formatting: https://stackoverflow.com/a/52606755
  parser = argparse.ArgumentParser(
    formatter_class=lambda prog: argparse.HelpFormatter(
      prog,
      max_help_position=52
    )
  )

  parser.add_argument(
    "-i",
    type=pathlib.Path,
    dest="input",
    required=True,
    metavar=("/path/to/input.xml"),
    help="path to the input PAGE-XML file"
  )

  parser.add_argument(
    "-o",
    type=pathlib.Path,
    dest="output",
    required=True,
    metavar=("/path/to/output.{png,jpg}"),
    help="path to the output image (PNG/JPEG) file"
    # TODO: Support other extensions like TIFF
  )

  parser.add_argument(
    "--base-dir",
    type=pathlib.Path,
    dest="base_dir",
    default=pathlib.Path.cwd(),
    metavar=("/path/to/base/dir/"),
    help="path to the base directory for the image paths in the PAGE-XML file"
  )

  parser.add_argument(
    "--background",
    action=BackgroundAction,
    help="if this option is provided, the background of the page is drawn"
  )

  parser.add_argument(
    "--border",
    action=BorderAction,
    help="if this option is provided, the Border anottation of the page is " \
         "drawn"
  )

  parser.add_argument(
    "--print-space",
    action=PrintSpaceAction,
    help="if this option is provided, the PrintSpace anottation of the page " \
         "is drawn"
  )

  parser.add_argument(
    "--text-regions",
    action=TextRegionsAction,
    help="if this option is provided, the TextRegion anottations of the page " \
         "are drawn"
  )

  parser.add_argument(
    "--image-regions",
    action=ImageRegionsAction,
    help="if this option is provided, the ImageRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--line-drawing-regions",
    action=LineDrawingRegionsAction,
    help="if this option is provided, the LineDrawingRegion anottations of " \
         "the page are drawn"
  )

  parser.add_argument(
    "--graphic-regions",
    action=GraphicRegionsAction,
    help="if this option is provided, the GraphicRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--table-regions",
    action=TableRegionsAction,
    help="if this option is provided, the TableRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--chart-regions",
    action=ChartRegionsAction,
    help="if this option is provided, the ChartRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--separator-regions",
    action=SeparatorRegionsAction,
    help="if this option is provided, the SeparatorRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--maths-regions",
    action=MathsRegionsAction,
    help="if this option is provided, the MathsRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--chem-regions",
    action=ChemRegionsAction,
    help="if this option is provided, the ChemRegion anottations of the page " \
         "are drawn"
  )

  parser.add_argument(
    "--music-regions",
    action=MusicRegionsAction,
    help="if this option is provided, the MusicRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--advert-regions",
    action=AdvertRegionsAction,
    help="if this option is provided, the AdvertRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--noise-regions",
    action=NoiseRegionsAction,
    help="if this option is provided, the NoiseRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--unknown-regions",
    action=UnknownRegionsAction,
    help="if this option is provided, the UnknownRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--custom-regions",
    action=CustomRegionsAction,
    help="if this option is provided, the CustomRegion anottations of the " \
         "page are drawn"
  )

  parser.add_argument(
    "--text-lines",
    action=TextLinesAction,
    help="if this option is provided, the TextLine anottations of the page " \
         "are drawn"
  )

  parser.add_argument(
    "--words",
    action=WordsAction,
    help="if this option is provided, the Word anottations of the page are " \
         "drawn"
  )

  parser.add_argument(
    "--glyphs",
    action=GlyphsAction,
    help="if this option is provided, the Glyph anottations of the page are " \
         "drawn"
  )

  parser.add_argument(
    "--graphemes",
    action=GraphemesAction,
    help="if this option is provided, the Grapheme anottations of the page " \
         "are drawn"
  )

  parser.add_argument(
    "--fill-color",
    type=graphics.Color.normalize_color_string,
    action=FillColorAction,
    metavar=("[COLOR]"),
    help="CSS3 name or RGB hex string of the color to fill the polygons with"
  )

  parser.add_argument(
    "--edge-color",
    type=graphics.Color.normalize_color_string,
    action=EdgeColorAction,
    metavar=("[COLOR]"),
    help="CSS3 name or RGB hex string of the color to draw the polygon edges " \
         "with"
  )

  parser.add_argument(
    "--edge-thickness",
    type=int,
    action=EdgeThicknessAction,
    metavar=("[1 .. inf]"),
    help="thickness of the edges of the polygons to be drawn"
  )

  parser.add_argument(
    "--opacity",
    type=float,
    action=OpacityAction,
    metavar=("[0.0 .. 1.0]"),
    help="opacity of the polygons to be drawn"
  )

  options = parser.parse_args(namespace=Namespace())

  return options