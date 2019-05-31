"""
LED View

Draws to the LEDS
"""

from view import View
import time

# TODO LED Strip init code

class LedView(View):
    def __init__(self, colors: list, dimensions: tuple, update):
        super().__init__(colors, dimensions, update)

    def draw(self):
        """
        Draw the leds in a loop, blocks
        """
        while True:
            self.update()
            time.sleep(1) 
