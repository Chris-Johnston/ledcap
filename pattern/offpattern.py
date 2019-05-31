"""
Off
"""

from pattern.pattern import Pattern

class OffPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, _ in self:
            self[idx] = 0
