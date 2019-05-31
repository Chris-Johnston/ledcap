"""
Loads a gif

"""

from pattern.pattern import Pattern
import random
from PIL import Image
import time

gifs = ['gif/loading.gif', 'gif/crob.gif']
# gifs = ['gif/bigtest.gif']

class GifPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.load_gif(gifs[0])
        self.frame = 0

    def load_gif(self, path):
        self.image = Image.open(path)
    
    def update(self):
        if self.image.is_animated:
            self.frame = (self.frame + 1) % self.image.n_frames
        self.image.seek(self.frame)
        rgb = self.image.convert('RGBA')
        for idx, _ in self:
            x, y = self.index_to_coords(idx)
            coord = (y, x)
            r, g, b, a = rgb.getpixel(coord)
            self[idx] = int(0xffffff * a / 255.0) & (r << 16 | g << 8 | b)