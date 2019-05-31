"""
Spiral Pattern
"""

from pattern.pattern import Pattern
import math
import time

class SpiralPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
    
    def update(self):
        i = self.coords_to_index((7, 7))
        self[i] = 0

        for idx, val in self:
            x, y = self.index_to_coords(idx)
            x -= 7
            y -= 7
            rad = math.sqrt(x * x + y * y)
            angle = 0.0
            if x != 0 and y != 0:
                angle = math.degrees(math.atan(y / x))
            # elif x == 0 and y == 0:
            #     break
            # print(idx, rad, angle)
            if rad == 0.0:
                continue
            quiddle = 80.0
            biddle = 40.0
            l = -30.0
            mod = (angle + biddle * time.time() - l * math.log(rad)) % quiddle
            if mod < biddle:
                self[idx] = 0x00ffff
            else:
                self[idx] = 0x0