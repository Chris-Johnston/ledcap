"""
Blinky Pattern
Blinks a lot
"""

from pattern.pattern import Pattern
import random

class BlinkyPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, _ in self:
            if random.randint(0, 100) > 90:
                self[idx] = 0xffffff
            else:
                self[idx] = 0x0
