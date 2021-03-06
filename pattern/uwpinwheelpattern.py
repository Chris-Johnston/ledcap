"""
UW Pinwheel
"""

from pattern.pattern import Pattern
import random
import time

PURPLE = 0x65, 0x39, 0x99
GOLD = 0xef, 0xe3, 0x62

class UWPinwheelPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.chase_index = 0

    def get_edge_coordinates(self):
        count = 0
        for x in range(self.dimensions[0]):
            yield x, 0, count
            count += 1
        for y in range(self.dimensions[1]):
            yield self.dimensions[0] - 1, y, count
            count += 1
        for x in range(self.dimensions[0]):
            yield self.dimensions[0] - 1 - x, self.dimensions[1] - 1, count
            count += 1
        for y in range(self.dimensions[1]):
            yield 0, self.dimensions[1] - 1 - y, count
            count += 1
    
    def update(self):
        # black out everything
        for idx, _ in self:
            self[idx] = 0
        # add a 'chasing' thing around the corner
        for x, y, count in self.get_edge_coordinates():
            # print('edge: ', x, y, count)
            # TODO: clean this up
            index = self.coords_to_index((x, y))
            max_count = (self.dimensions[0] + self.dimensions[1]) * 2
            if ((self.chase_index + count) % max_count ) // (max_count / 2) == 0:
                r, g, b = PURPLE
                # print('purple')
                color_count = (self.chase_index + count) % max_count
            else:
                r, g, b = GOLD
                # print('gold')
                color_count = (self.chase_index + count) % max_count - (max_count // 2)
            # determine amp from distance from chase_index
            amp = 1.0
            if color_count > 0:
                amp = 1 - 2 * (color_count / (max_count / 2))
                # print(color_count, amp)
                r *= amp
                g *= amp
                b *= amp
                if amp < 0:
                    r, g, b = 0, 0, 0
            self[index] = 0xffffff & (int(r) << 16 | int(g) << 8 | int(b))
        self.chase_index += 1

        # for x in range(5):
        #     idx = random.randint(0, 14 * 14 - 1)
        #     self[idx] = 0xffffff
