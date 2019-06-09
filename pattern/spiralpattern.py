"""
Spiral Pattern
"""

from pattern.pattern import Pattern
import math
import time
SWITCH_TIME = 30

class SpiralPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.switch_timer = time.time()
        self.direction = 1
    
    def update(self):
        if (SWITCH_TIME + self.switch_timer) < time.time():
            self.switch_timer = time.time()
            self.direction *= -1
        i = self.coords_to_index((7, 7))
        self[i] = 0

        for idx, val in self:
            x, y = self.index_to_coords(idx)
            x -= 7
            y -= 7
            rad = math.sqrt(x * x + y * y)
            angle = 0.0
            if x != 0:
                angle = math.degrees(math.atan(y / x))
            if rad == 0.0:
                continue
            a = 80.0
            b = 40.0
            l = -30.0
            mod = (angle + b * self.direction * time.time() - l * math.log(rad)) % a
            if mod < b:
                r = 0xff & int(0xff * 1.4 * (rad / self.dimensions[0]))
                color = 0x330033 | r << 16 | r << 0
                color &= 0xffffff
                self[idx] = color
            else:
                self[idx] = 0x0