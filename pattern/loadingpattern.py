"""
Loading Pattern
"""

from pattern.pattern import Pattern
import random
import time
import math

class LoadingPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, _ in self:
            x, y = self.index_to_coords(idx)
            # center the coords
            x -= 6.5
            y -= 6.5
            radius = math.sqrt(x * x + y * y)
            offset = 5
            angle = (math.atan(y / (x + 0.00001)) + (time.time() * 1000.0 / 400.0)) % 3.14
            angle = angle if angle > 1.28 else 0
            amp = math.sin(angle)
            amp = amp if amp > 0 else -amp
            size = 1.4
            a = int(amp * 0xff * math.cos((radius - offset) / size))
            a = a if a > 0 else 0
            val = 0xffffff & (0 << 16 | a << 8 | a)
            self[idx] = val
