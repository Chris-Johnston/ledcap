"""
binary clock
"""

from pattern.pattern import Pattern
import time
import random
import math

class HackScrollerPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.on_color = 0x00ff00

    def update(self):
        x = time.time()
        # cool idea, maybe have "on" color adjust hue over time
        for idx, val in self:
            bit = idx % 32
            bitmask = 1 << bit
            if x & bitmask > 0:
                self[idx] = self.on_color
            else:
                self[idx] = 0