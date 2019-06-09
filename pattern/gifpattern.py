"""
Gif Pattern

Cycles through some animated gifs
"""

from pattern.pattern import Pattern
import random
from PIL import Image
import time

gifs = ['gif/question2.gif', 'gif/question_crop.gif']
CHANGE_TIME = 5 # seconds

class GifPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.gif_num = 2
        self.load_gif(gifs[self.gif_num])
        self.frame = 0
        self.change_time = time.time()

    def load_gif(self, path):
        self.image = Image.open(path)
    
    def update(self):
        if (self.change_time + CHANGE_TIME) < time.time():
            self.gif_num = (self.gif_num + 1) % len(gifs)
            self.load_gif(gifs[self.gif_num])
            self.change_time = time.time()
        # advance the frame if animated
        if self.image.is_animated:
            self.frame = (self.frame + 1) % self.image.n_frames
        self.image.seek(self.frame)
        rgb = self.image.convert('RGBA')
        if 'duration' in self.image.info:
            time.sleep(self.image.info['duration'] / 1000.0)
        for idx, _ in self:
            x, y = self.index_to_coords(idx)
            coord = (y, x)
            r, g, b, a = rgb.getpixel(coord)
            self[idx] = int(0xffffff * a / 255.0) & (r << 16 | g << 8 | b)