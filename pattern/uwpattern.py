"""
UW Pattern
"""

from pattern.pattern import Pattern
import random
from PIL import Image
import time

image = 'gif/uw.gif'

class UWPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.load_gif(image)

    def load_gif(self, path):
        self.image = Image.open(path)
    
    def update(self):
        rgb = self.image.convert('RGBA')
        for idx, _ in self:
            x, y = self.index_to_coords(idx)
            coord = (y, x)
            r, g, b, a = rgb.getpixel(coord)
            self[idx] = int(0xffffff * a / 255.0) & (r << 16 | g << 8 | b)