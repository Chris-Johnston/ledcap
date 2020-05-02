"""
Red pattern
"""

from pattern.pattern import Pattern
import time
import random
import math

class RedPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, val in self:
            if random.randint(0, 50) == 1:
                self[idx] = 0xff7777
            else:
                coords = self.index_to_coords(idx)
                size = 5.0
                offset = time.time() * 1000.0 / 555.0

                gb = int(0x13 * math.cos((coords[1] - (0.34 * offset)) / (size * 0.3)))
                if gb < 0:
                    gb = 0

                r = 127 + int(127 * math.cos((coords[1] - offset) / size))
                r |= gb
                if r < 0:
                    r = 0
                self[idx] = r << 16 | gb << 8 | gb
