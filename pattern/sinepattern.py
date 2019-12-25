"""
Sine Pattern
"""

from pattern.pattern import Pattern
import random
import math
import time

class SinePattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, _ in self:
            r = int(abs(0xff * math.sin(time.time() * 1.1 + idx / 30.0))) & 0xff
            g = int(abs(0xff * math.sin(time.time() * 1.3 + idx / 50.0))) & 0xff
            b = int(abs(0xff * math.sin(time.time() * 0.8 + idx / 45.0))) & 0xff
            self[idx] = r << 16 | g << 8 | b
