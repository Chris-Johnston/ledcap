"""
Red pattern
"""

from pattern.pattern import Pattern
import time

class RedPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, val in self:
            self[idx] = 0xff0000
