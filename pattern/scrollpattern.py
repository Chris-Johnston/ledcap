"""
Scroll Pattern
"""

from pattern.pattern import Pattern
import random
import time

class BlinkyPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.offset = 0
        self.last_time = time.time()
        self.time_delay = 0.5

    def update(self):
        if time.time() > self.last_time + self.time_delay:
            self.offset += 1
            self.offset %= self.__max_index__()
            self.last_time = time.time()
        for idx, _ in self:
            self[idx] = 0xff00ff if idx == self.offset else 0
