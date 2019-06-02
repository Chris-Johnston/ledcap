"""
LED View

Draws to the LEDS
"""

from view import View
import time
import rpi_ws281x as ws

brightness = 15
# TODO LED Strip init code

class LedView(View):
    def __init__(self, colors: list, dimensions: tuple, update):
        super().__init__(colors, dimensions, update)
        self.count = self.dimensions[0] * self.dimensions[1]

    def coord_to_strip_index(self, x: int, y: int) -> int:
        if y % 2 == 0:
            return x + self.dimensions[0] * y
        return (self.dimensions[1] - x) + self.dimensions[0] * y

    def internal_draw(self, strip):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                index = self.coord_to_strip_index(x, y)
                strip.setPixelColor(index, self.colors[x][y])

    def draw(self):
        """
        Draw the leds in a loop, blocks
        """
        strip = ws.Adafruit_NeoPixel(self.count, 18, 800000, 10, False, brightness)
        strip.begin()
        while True:
            self.update()
            self.internal_draw(strip)
            strip.show()
