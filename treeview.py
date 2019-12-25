"""
Tree LED View

Draws to the LEDS
"""

from view import View
import time
import rpi_ws281x as ws

brightness = 100
update_rate = 1.0 / 90.0

class TreeLedView(View):
    def __init__(self, colors: list, dimensions: tuple, update):
        super().__init__(colors, dimensions, update)
        self.count = self.dimensions[0] * self.dimensions[1]

    def coord_to_strip_index(self, x: int, y: int) -> int:
        return self.dimensions[0] * x + y

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
        try:
            while True:
                self.update()
                self.internal_draw(strip)
                strip.show()
                time.sleep(update_rate)
        except KeyboardInterrupt:
            for x in range(self.count):
                strip.setPixelColor(x, 0)
            strip.show()
            time.sleep(update_rate)
