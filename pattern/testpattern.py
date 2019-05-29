"""
Test Pattern
"""

from pattern.pattern import Pattern

class TestPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.toggle = False
    
    def update(self):
        self.toggle = not self.toggle
        for idx, val in self:
            if self.toggle:
                self[idx] = 0xff0000
            else:
                self[idx] = 0x0000ff