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

            shift = time.time() / 50.0
            width = 40.0 + 0.3 * abs(dist) + 39.9 * math.sin(shift)
            v = 0.5 + 0.5 * math.cos(shift + dist * math.pi * width)
            h = 0.3 + abs(dist / 2.0) + 0.1 * math.sin(shift / 7.0)
            r, g, b = colorsys.hsv_to_rgb(h, 1.0, v)
            on_color = self.rgb_to_val(r * 255, g * 255, b * 255)
            self[idx] = on_color
            # bitmask = 1 << bit
            # if int(x) & bitmask > 0:
            #     self[idx] = on_color
            # else:
            #     self[idx] = 0
