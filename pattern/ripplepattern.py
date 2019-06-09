"""
Ripple Pattern
"""

from pattern.pattern import Pattern
import random
import time
import math

class RipplePattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, _ in self:
            x, y = self.index_to_coords(idx)
            # center the coords
            x -= 7
            y -= 7
            radius = math.sqrt(x * x + y * y)
            offset = time.time() * 1000.0 / 900.0
            size = 1.9
            a = int(0xff * math.sin((radius - offset) / size) ) #* math.sin((y + offset) / size)
            a = a if a > 0 else 0
            size = 2.1
            offset = time.time() * 1000.0 / 750.0
            g = int(0xff * math.cos((radius - offset) / size) ) #* math.sin((y + offset) / size)
            g = g if g > 0 else 0
            size = 1.8            
            offset = -time.time() * 1000.0 / 800.0
            b = int(0xff * math.cos((radius - offset) / size) ) #* math.sin((y + offset) / size)
            b = b if b > 0 else 0
            val = 0xffffff & (a << 16 | g << 8 | b)
            self[idx] = val
