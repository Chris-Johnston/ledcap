"""
hack scroller
"""

from pattern.pattern import Pattern
import time
import random
import math

class HackScrollerPattern(Pattern):
    def __init__(self, colors: list, dimensions: tuple):
        super().__init__(colors, dimensions)
        self.tick = 0

    def update(self):
        self.tick += 1
        for idx, val in self:
            if idx == (self.tick % self.__max_index__()):
                self[idx] = 0xffffff
            if (self.tick - 5 % self.__max_index__()) < idx < (self.tick % self.__max_index__()):
                self[idx] = 0x00ff00


            
