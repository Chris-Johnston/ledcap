"""
Hacker Pattern
"""

import random
from pattern.pattern import Pattern

MAX_BLIPS = 25 # number of blips to show

class HackerPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.blips = []

    def spawn_blip(self):
        x, y = random.randint(14, 28), random.randint(-14, 0)
        self.blips.append((x, y))
        print('spawned blip at ', (x, y))
    
    def update(self):
        if len(self.blips) < MAX_BLIPS and random.randint(0, 100) > 20:
            self.spawn_blip()
        # black out everything first
        for idx, _ in self:
            self[idx] = 0
        for idx in range(len(self.blips)):
            # increment position of the blip
            x, y = self.blips[idx]
            self.blips[idx] = x - 1, y + 1
            if 0 <= x < self.dimensions[0] and 0 <= y < self.dimensions[1]:
                strip_index = self.coords_to_index((x, y))
                self[strip_index] = 0xccffcc
            # draw the trail
            trail_x, trail_y = x, y
            for g in range(225, 0, -25):
                trail_x, trail_y = trail_x + 1, trail_y - 1
                if 0 <= trail_x < self.dimensions[0] and 0 <= trail_y < self.dimensions[1]:
                    strip_index = self.coords_to_index((trail_x, trail_y))
                    self[strip_index] = 0x00ff00 & (g << 8)
        # cleanup old blips
        self.blips = [b for b in self.blips if not (b[0] < -10 or b[1] > 24)]
