"""
Pattern Manager
"""

import importlib
import inspect
from pattern.pattern import Pattern
import os.path
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

RESERVED_PATTERNS = [
    'pattern.offpattern',
]

USER_PATTERNS = [
    # 'pattern.testpattern',
    'pattern.spiralpattern',
    # 'pattern.lifepattern',
    'pattern.phasespattern',
    'pattern.blinkypattern',
    # 'pattern.gifpattern',
    # 'pattern.msftlogopattern',
    # 'pattern.onlyuwpattern',
    # 'pattern.uwpattern',
    # 'pattern.uwpinwheelpattern',
    # 'pattern.clockpattern',
    'pattern.hackerpattern',
    # 'pattern.dvdpattern',
    'pattern.loadingpattern',
    'pattern.ripplepattern',
]

class PatternManager():
    """
    Manages a bunch of the patterns and runs the update loop
    """

    def __init__(self, colors, dimensions):
        self.handler_index = 1
        self.handlers = []
        self.patterns = RESERVED_PATTERNS + USER_PATTERNS
        self.setup_handlers(colors, dimensions)

    def setup_handlers(self, colors, dimensions):
        self.handlers = []
        # load all of the PATTERNS
        for p in self.patterns:
            mod = importlib.import_module(p)
            # get pattern subclasses of module
            for name, obj in inspect.getmembers(mod):
                if obj is not Pattern and isinstance(obj, type) and issubclass(obj, Pattern):
                    instance = obj(colors, dimensions)
                    self.handlers.append(instance)

    def is_off(self) -> bool:
        return self.handler_index == 0

    def off(self):
        self.handler_index = 0

    def set_index(self, index: int):
        # fail silently
        self.handler_index = index % len(self.patterns)

    def next_pattern(self):
        self.handler_index = (self.handler_index + 1) % (len(self.patterns) - 1)

    def prev_pattern(self):
        self.handler_index = (self.handler_index - 1) % (len(self.patterns) - 1)

    def update(self):
        self.handlers[self.handler_index].update()

class FileBasedPatternManager(PatternManager):
    def __init__(self, colors, dimensions, filename):
        super().__init__(colors, dimensions)
        self.filename = filename
        self.setup_file()

    def setup_file(self):
        if os.path.exists(self.filename):
            self.read_file()
        else:
            # use defaults from super init
            self.write_file()

    def read_file(self):
        with open(self.filename, 'r') as state_file:
            state_json = json.loads(state_file.read())
            self.patterns = RESERVED_PATTERNS + state_json["patterns"] 
            self.handler_index = state_json["selected"]
            # TODO: could consider adding additional state per patterns, like color values

    def write_file(self):
        with open(self.filename, 'w') as state_file:
            payload = {
                "selected": self.handler_index,
                "patterns": self.patterns,
            }
            state_json = json.dumps(payload)
            state_file.write(state_json)

class ModifiedHandler(FileSystemEventHandler):
    def __init__(self, pm):
        self.pm = pm

    def on_modified(self, event):
        print(json.dumps(event))
        if not isinstance(event, FileModifiedEvent):
            return
        print(event.src_path)
        if self.pm.filename not in event.src_path:
            return
        pm.read_file()

class ObservingFilePatternManager(FileBasedPatternManager):
    def __init__(self, colors, dimensions, filename):
        super().__init__(colors, dimensions, filename)
        self.handler = ModifiedHandler(self)
        self.observer = Observer()
        # hack: observer only works with dirs and not individual files, lame.
        self.observer.schedule(self.handler, '.', recursive=False)
        self.observer.start()

    def update():
        super().update()
        if self.observer.isAlive():
            self.observer.join(0.1)