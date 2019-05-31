"""
LED View

Draws to the LEDS
"""

from view import View
import time
import neopixel
import board

brightness = 0.2
# TODO LED Strip init code

class LedView(View):
    def __init__(self, colors: list, dimensions: tuple, update):
        super().__init__(colors, dimensions, update)
        self.count = self.dimensions[0] * self.dimensions[1]

    def coord_to_strip_index(self, x: int, y: int) -> int:
        if x % 2 == 0:
            return x + self.dimensions[0] * y
        return (self.dimensions[1] - x) + self.dimensions[0] * y

    def internal_draw(self, strip):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                index = self.coord_to_strip_index(x, y)
                strip[index] = self.colors

    def draw(self):
        """
        Draw the leds in a loop, blocks
        """
        
        with neopixel.NeoPixel(board.D18, self.count, bpp=3, auto_write=False, brightness=brightness, pixel_order=neopixel.GRB) as strip:
            while True:
                self.update()
                self.internal_draw(strip)
                strip.show(0) 
