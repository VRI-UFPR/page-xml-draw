import xml.etree.ElementTree as ET

class Page:
  boundary_types = [
    'Border',
    'PrintSpace'
  ]

  region_types = [
    'TextRegion',
    'ImageRegion',
    'LineDrawingRegion',
    'GraphicRegion',
    'TableRegion',
    'ChartRegion',
    'SeparatorRegion',
    'MathsRegion',
    'ChemRegion',
    'MusicRegion',
    'AdvertRegion',
    'NoiseRegion',
    'UnknownRegion',
    'CustomRegion'
  ]

  line_types = [
    'TextLine'
  ]

  word_types = [
    'Word'
  ]

  glyph_types = [
    'Glyph'
  ]

  grapheme_types = [
    'Grapheme'
  ]

  def __init__(self, path):
    self.file = ET.parse(path).getroot()

    self.parse_page()
    self.parse_boundaries()
    self.parse_regions()
    self.parse_lines()
    self.parse_words()
    self.parse_glyphs()
    self.parse_graphemes()

  def get_child(self, name, root):
    for child in root:
      if child.tag.endswith(name):
        return child

    return None

  def get_children(self, name, root):
    elements = []

    for child in root:
      if child.tag.endswith(name):
        elements.append(child)

    return elements

  def get_polygon(self, root):
    points = self.get_child('Coords', root).attrib['points']
    return [[int(coord) for coord in pt.split(',')] for pt in points.split(' ')]

  def get_image_filename(self):
    return self.page.attrib['imageFilename']

  def get_elements(self):
    elements = {}

    elements.update(self.boundaries)
    elements.update(self.regions)
    elements.update(self.lines)
    elements.update(self.words)
    elements.update(self.glyphs)
    elements.update(self.graphemes)

    return elements

  def parse_page(self):
    self.page = self.get_child('Page', self.file)

  def parse_boundaries(self):
    self.boundaries = {}

    for typ in self.boundary_types:
      children = self.get_children(typ, self.page)

      if children:
        self.boundaries[typ] = children

  def parse_regions(self):
    self.regions = {}

    for typ in self.region_types:
      children = self.get_children(typ, self.page)

      if children:
        self.regions[typ] = children

  def parse_lines(self):
    self.lines = {}

    for regions in self.regions.values():
      for region in regions:
        for typ in self.line_types:
          children = self.get_children(typ, region)

          if children:
            if typ in self.lines:
              self.lines[typ] += children
            else:
              self.lines[typ] = children

  def parse_words(self):
    self.words = {}

    for lines in self.lines.values():
      for line in lines:
        for typ in self.word_types:
          children = self.get_children(typ, line)

          if children:
            if typ in self.words:
              self.words[typ] += children
            else:
              self.words[typ] = children

  def parse_glyphs(self):
    self.glyphs = {}

    for words in self.words.values():
      for word in words:
        for typ in self.glyph_types:
          children = self.get_children(typ, word)

          if children:
            if typ in self.glyphs:
              self.glyphs[typ] += children
            else:
              self.glyphs[typ] = children

  def parse_graphemes(self):
    self.graphemes = {}

    for glyphs in self.glyphs.values():
      for glyph in glyphs:
        for typ in self.grapheme_types:
          children = self.get_children(typ, glyph)

          if children:
            if typ in self.graphemes:
              self.graphemes[typ] += children
            else:
              self.graphemes[typ] = children