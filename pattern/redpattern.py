"""
Red pattern
"""

from pattern.pattern import Pattern
import time
import random

class RedPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, val in self:
            if random.randint(0, 90) == 0:
                self[idx] = 0xff0000
            else:
                r = int(0xff * math.cos((offset) / size))
                if r < 0:
                    r = 0
                self[idx] = r << 16
