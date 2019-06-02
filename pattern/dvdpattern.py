"""
'DVD logo' pattern

bounces around, maybe hits a corner?
"""

from pattern.pattern import Pattern
import random

NUM_BOUNCERS = 15
COLORS = [
    0xff0000, 0xffff00, 0x00ff00, 0x0000ff
]

class DVDPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.bouncers = []
    
    def update(self):
        # turn off everything
        for idx, _ in self:
            self[idx] = 0
        if len(self.bouncers) < NUM_BOUNCERS:
            # spawn a new bouncer
            x, y = random.randint(1, self.dimensions[0] - 2), random.randint(1, self.dimensions[1] - 2)
            dir_x, dir_y = random.randint(0, 1), random.randint(0, 1)
            dir_x = -1 if dir_x == 0 else dir_x
            dir_y = -1 if dir_y == 0 else dir_y
            color = random.choice(COLORS)
            self.bouncers.append([x, y, dir_x, dir_y, color])
        for b in self.bouncers:
            # if at the edge, change direction
            if b[0] == 0 or b[0] == (self.dimensions[0] - 1):
                b[2] = -b[2]
                b[4] = random.choice(COLORS)
            if b[1] == 0 or b[1] == (self.dimensions[1] - 1):
                b[3] = -b[3]
                b[4] = random.choice(COLORS)
            # update position
            b[0] += b[2]
            b[1] += b[3]
            idx = self.coords_to_index((b[0], b[1]))
            self[idx] = b[4]