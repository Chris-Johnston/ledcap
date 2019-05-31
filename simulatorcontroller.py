"""
Simulator Controller

Listens to the key press events and calls the methods of the pattern manager
"""

from controller import Controller
from tkinter import Canvas

class SimulatorController(Controller):
    def __init__(self, patternmanager):
        super().__init__(patternmanager)
        self.canvas = None

    def keydown(self, event):
        if event.char.lower() == 'a':
            self.pattern_manager.next_pattern()
        elif event.char.lower() == 'd':
            self.pattern_manager.prev_pattern()

    def focus(self, event):
        self.canvas.focus_set()

    def set_binds(self, can: Canvas):
        self.canvas = can
        can.bind("<Key>", self.keydown)
        can.bind("<Button-1>", self.focus)
        can.focus_set()
        can.pack()
