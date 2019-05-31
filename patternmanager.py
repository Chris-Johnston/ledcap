"""
Pattern Manager
"""

import importlib
import inspect
from pattern.pattern import Pattern

patterns = [
    'pattern.testpattern',
    'pattern.spiralpattern',
    'pattern.lifepattern',
    'pattern.phasespattern',
    'pattern.blinkypattern'
]

class PatternManager():
    """
    Manages a bunch of the patterns and runs the update loop
    """

    def __init__(self, colors, dimensions):
        self.handler_index = 4
        self.handlers = []
        # load all of the patterns
        for p in patterns:
            mod = importlib.import_module(p)
            # get pattern subclasses of module
            for name, obj in inspect.getmembers(mod):
                if obj is not Pattern and isinstance(obj, type) and issubclass(obj, Pattern):
                    instance = obj(colors, dimensions)
                    self.handlers.append(instance)

    def update(self):
        self.handlers[self.handler_index].update()
