import webcolors
import numpy as np
import cv2

class Color:

  @staticmethod
  def normalize_color_string(color):
    if color in webcolors.CSS3_NAMES_TO_HEX:
      return color
    else:
      if not color.startswith("#"):
        # Append '#' hex string indicator prefix:
        color = "#" + color

      return webcolors.normalize_hex(color)

  def __init__(self, color):
    if color in webcolors.CSS3_NAMES_TO_HEX:
      self.hex = webcolors.name_to_hex(color, spec=webcolors.CSS3)
    else:
      self.hex = color

  def to_rgb(self):
    return webcolors.hex_to_rgb(self.hex)

  def to_bgr(self):
    r, g, b = self.to_rgb()
    return b, g, r


class Polygon:

  def __init__(self, points):
    self.points = points

  def to_np(self):
    return np.array(self.points)


class Overlay:

  def __init__(self, image_path, page, anottations):
    try:
      bg = anottations.pop('Background')

      bg_color = Color(bg['FillColor'])
      bg_alpha = bg['Transparency']
    except KeyError:
      bg_color = Color('#000000')
      bg_alpha = 0.0

    self.image = cv2.imread(str(image_path))

    color_mask = np.zeros_like(self.image)
    weight_mask = np.zeros((
      self.image.shape[0], self.image.shape[1], 1),
      dtype=np.float
    )

    color_mask[:] = bg_color.to_bgr()
    weight_mask[:] = bg_alpha

    element_types = page.get_elements()

    for typ, properties in zip(anottations.keys(), anottations.values()):
      elements = element_types[typ]
      polygons = [Polygon(page.get_polygon(el)).to_np() for el in elements]

      if 'FillColor' in properties:
        color = Color(properties['FillColor'])
        cv2.fillPoly(color_mask, polygons, color.to_bgr())

        if 'Transparency' in properties:
          alpha = properties['Transparency']
          cv2.fillPoly(weight_mask, polygons, alpha)

      if 'EdgeColor' in properties and 'EdgeThickness' in properties:
        color = Color(properties['EdgeColor'])
        thickness = properties['EdgeThickness']
        cv2.polylines(color_mask, polygons, True, color.to_bgr(), thickness)

        if 'Transparency' in properties:
          alpha = properties['Transparency']
          cv2.polylines(weight_mask, polygons, True, alpha, thickness)

    self.overlay = color_mask * weight_mask + self.image * (1.0 - weight_mask)

  def save(self, output_path):
    cv2.imwrite(str(output_path), self.overlay)
