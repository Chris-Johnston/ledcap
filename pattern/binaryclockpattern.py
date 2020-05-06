"""
binary clock
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
            bit = idx % 32
            on_color = colorsys.hsv_to_rgb(0.5 + (bit/64), 1, 0.5)
            on_color = self.tuple_to_val(on_color)
            bitmask = 1 << bit
            if int(x) & bitmask > 0:
                self[idx] = on_color
            else:
                self[idx] = 0