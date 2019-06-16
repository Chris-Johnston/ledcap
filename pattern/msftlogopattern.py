"""
MSFT Logo Pattern
"""

from pattern.pattern import Pattern
import time

r = 0xf25022
g = 0x7fba00
b = 0x00a4ef
y = 0xffb900

logo = [
    [r, g],
    [b, y]
]

class MSFTLogoPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def update(self):
        for idx, _ in self:
            x, y = self.index_to_coords(idx)
            self[idx] = logo[x // 7][y // 7]
        time.sleep(1/10.0)