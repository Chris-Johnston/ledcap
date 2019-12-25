"""
Pattern Manager
"""

import importlib
import inspect
from pattern.pattern import Pattern

patterns = [
    'pattern.sinepattern',
    'pattern.scrollpattern',
    # 'pattern.testpattern',
    # 'pattern.spiralpattern',
    # 'pattern.lifepattern',
    # 'pattern.phasespattern',
    'pattern.blinkypattern',
    # 'pattern.gifpattern',
    # 'pattern.msftlogopattern',
    # 'pattern.onlyuwpattern',
    # 'pattern.uwpattern',
    'pattern.uwpinwheelpattern',
    # 'pattern.clockpattern',
    # 'pattern.hackerpattern',
    # 'pattern.dvdpattern',
    # 'pattern.loadingpattern',
    # 'pattern.ripplepattern',
    'pattern.offpattern' # off must be the last pattern
]

OFF_PATTERN = len(patterns) - 1

class PatternManager():
    """
    Manages a bunch of the patterns and runs the update loop
    """

    def __init__(self, colors, dimensions):
        self.handler_index = 0
        self.handlers = []
        # load all of the patterns
        for p in patterns:
            mod = importlib.import_module(p)
            # get pattern subclasses of module
            for name, obj in inspect.getmembers(mod):
                if obj is not Pattern and isinstance(obj, type) and issubclass(obj, Pattern):
                    instance = obj(colors, dimensions)
                    self.handlers.append(instance)

    def is_off(self) -> bool:
        return self.handler_index == OFF_PATTERN

    def off(self):
        self.handler_index = OFF_PATTERN

    def set_index(self, index: int):
        self.handler_index = index

    def next_pattern(self):
        self.handler_index = (self.handler_index + 1) % (len(patterns) - 1)

    def prev_pattern(self):
        self.handler_index = (self.handler_index - 1) % (len(patterns) - 1)

    def update(self):
        self.handlers[self.handler_index].update()
