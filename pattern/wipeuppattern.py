"""
Wipe Up Pattern
"""

from pattern.pattern import Pattern
import random
import time

class WipeUpPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.offset = 0
        self.last_time = time.time()
        self.time_delay = 0.1

    def update(self):
        primary = 0xff0000
        secondary = 0x00ff00
        t = time.time() * 1000
        delay = 800.0

        if (t // delay) % 2 == 0:
            # swap colors
            primary = 0x00ff00
            secondary = 0xff0000
        
        completed = (t % delay) / delay
        completed = self.__max_index__() * completed

        for idx, _ in self:
            if idx < completed:
                self[idx] = secondary
            else:
                self[idx] = primary
