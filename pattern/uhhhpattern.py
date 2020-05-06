"""
uhhh
"""

from pattern.pattern import Pattern
import time
import random
import math
import colorsys

class HackScrollerPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        x = time.time()
        # cool idea, maybe have "on" color adjust hue over time
        for idx, val in self:
            _, y = self.index_to_coords(idx)
            dist = (y - (self.dimensions[1] / 2)) / (self.dimensions[1] / 2)

            r, g, b = colorsys.hsv_to_rgb(dist % 1.0, 1.0, 1.0)
            on_color = self.rgb_to_val(r * 255, g * 255, b * 255)
            self[idx] = on_color
            # bitmask = 1 << bit
            # if int(x) & bitmask > 0:
            #     self[idx] = on_color
            # else:
            #     self[idx] = 0