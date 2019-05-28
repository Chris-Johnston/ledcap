"""
Simulator for the RGB cap lights.

Used to debug things before testing on the actual hardware.
"""

import tkinter
import random

SCREEN_DIMENSIONS = (500, 500)
LED_DIMENSIONS = (14, 14)
LED_SIZE = 10 # px
LED_SPACE = 30 # px
OFFSET = 25
DRAW_RATE = int(1000 / 30.0)
UPDATE_RATE = int(1000 / 5.0)

colors = []
for row in range(LED_DIMENSIONS[0]):
    new = []
    for col in range(LED_DIMENSIONS[1]):
        new.append(0xff00ff)
    colors.append(new)

def convert_color(color_val: int) -> str:
    """
    Converts a color value into a hex string.
    """
    return "#%06x" % color_val

# canvas widget
m = tkinter.Tk()
can = tkinter.Canvas(m, width=SCREEN_DIMENSIONS[0], height=SCREEN_DIMENSIONS[1])
can.pack()

def update():
    # update the colors
    for row in range(LED_DIMENSIONS[0]):
        for col in range(LED_DIMENSIONS[1]):
            colors[row][col] = random.randint(0, 0xffffff)
            print((row, col), colors[row][col])
    # assert False
    m.after(UPDATE_RATE, update)

def draw():
    # black background
    can.create_rectangle(0, 0, SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1], fill="black")
    
    # draw each of the rows and cols
    for row in range(LED_DIMENSIONS[0]):
        for col in range(LED_DIMENSIONS[1]):
            x1 = col * LED_SPACE + OFFSET
            y1 = row * LED_SPACE + OFFSET
            color = convert_color(colors[row][col])
            print((row, col), colors[row][col], color)
            can.create_rectangle(x1, y1, x1 + LED_SIZE, y1 + LED_SIZE, fill=color)
    # assert False
    m.after(DRAW_RATE, draw)

update()
draw()

tkinter.mainloop()