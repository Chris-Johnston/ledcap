"""
Scroll Pattern
"""

from pattern.pattern import Pattern
import random

class BlinkyPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.offset = 0

    def update(self):
        self.offset += 1
        self.offset %= self.__max_index__()
        for idx, _ in self:
            self[idx] = 0xff00ff if idx == self.offset else 0
