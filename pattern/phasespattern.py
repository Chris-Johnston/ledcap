"""
Phases Pattern
"""

from pattern.pattern import Pattern
import time
import math

class PhasesPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, _ in self:
            size = 10.0
            coords = self.index_to_coords(idx)
            offset = time.time() * 1000.0 / 555.0
            r = int(0xff * math.cos((coords[1] - offset) / size) * math.sin((coords[0] + offset) / size))
            if r < 0:
                r = 0
            r = 0

            offset = time.time() * 1000.0 / 888.0
            g = int(0xff * math.cos((coords[1] + offset) / size) * math.sin((coords[0] + offset) / size))
            if g < 0:
                g = 0

            offset = time.time() * 1000.0 / 333.0
            b = int(0xff * math.cos((coords[1] + offset) / size) * math.sin((coords[0] - offset) / size))
            if b < 0:
                b = 0
            val = 0xffffff & (r << 16 | g << 8 | b)
            self[idx] = val
