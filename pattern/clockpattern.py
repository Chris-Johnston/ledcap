"""
Clock Pattern

It's a clock. Only good if the time is right
"""

from pattern.pattern import Pattern
import datetime
import math

class BlinkyPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)

    def draw_rad(self, color, rad, radius):
        x = math.sin(rad) * radius + (self.dimensions[0] / 2.0)
        y = math.cos(rad) * radius + (self.dimensions[1] / 2.0)
        x, y = round(x), round(y)
        index = self.coords_to_index((x, y))
        self[index] = color

    def update(self):
        # turn everything off
        for idx, _ in self:
            self[idx] = 0
        clock_radius = -1 + self.dimensions[0] / 2
        # draw a circle
        for deg in range(0, 360):
            rad = math.radians(deg)
            self.draw_rad(0xffffff, rad, clock_radius)
        offset = 180 + 45
        
        # 12 hour should be red
        # also rotate by 45 degrees
        self.draw_rad(0xff0000, math.radians(offset), clock_radius)

        # hour hand
        t = datetime.datetime.now()
        hour = -t.hour * 30 + offset
        for x in range(0, int(clock_radius - 1)):
            self.draw_rad(0x00ff00, math.radians(hour), x)
        # minute hand
        minute = -t.minute * 6 + offset
        for x in range(0, int(clock_radius)):
            self.draw_rad(0x0000ff, math.radians(minute), x)

        # second
        second = -t.second * 6 + offset
        for x in range(0, int(clock_radius)):
            self.draw_rad(0xff0000, math.radians(second), x)
        



