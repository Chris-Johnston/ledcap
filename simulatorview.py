"""
Simulator View

Draws the color data in a canvas window
"""

import tkinter
from view import View

SCREEN_DIMENSIONS = (500, 500)
LED_SIZE = 10 # px
LED_SPACE = 30 # px
OFFSET = 25
DRAW_RATE = int(1000 / 10.0)
UPDATE_RATE = int(1000 / 30.0)

class SimulatorView(View):
    def __init__(self, colors: list, dimensions: tuple, update):
        super().__init__(colors, dimensions, update)
        # canvas widget
        self.m = tkinter.Tk()
        self.can = tkinter.Canvas(self.m, width=SCREEN_DIMENSIONS[0], height=SCREEN_DIMENSIONS[1])
        self.packed = False
        
    def convert_color(self, color_val: int) -> str:
        """
        Converts a color value into a hex string.
        """
        return "#%06x" % color_val

    def internal_draw(self):
        self.update()
        self.can.delete(tkinter.ALL)
        # black background
        self.can.create_rectangle(0, 0, SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1], fill="black")
        
        # draw each of the rows and cols
        for row in range(self.dimensions[0]):
            for col in range(self.dimensions[1]):
                x1 = col * LED_SPACE + OFFSET
                y1 = row * LED_SPACE + OFFSET
                color = self.convert_color(self.colors[row][col])
                self.can.create_rectangle(x1, y1, x1 + LED_SIZE, y1 + LED_SIZE, fill=color)
        self.m.after(DRAW_RATE, self.internal_draw)

    def draw(self):
        """
        calls tk blocking main loop
        """
        if not self.packed:
            self.can.pack()
            self.packed = True
        self.m.after(DRAW_RATE, self.internal_draw)
        tkinter.mainloop()
