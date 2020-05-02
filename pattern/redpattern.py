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
            if random.randint(0, 90) == 1:
                self[idx] = 0xff0000
            else:
                coords = self.index_to_coords(idx)
                size = 5.0
                offset = time.time() * 1000.0 / 555.0
                r = 127 + int(127 * math.cos((coords[1] - offset) / size))
                if r < 0:
                    r = 0
                self[idx] = r << 16