"""
Simulator for the RGB cap lights.

Used to debug things before testing on the actual hardware.
"""

import random
from simulatorview import SimulatorView

LED_DIMENSIONS = (14, 14)
colors = []
for row in range(LED_DIMENSIONS[0]):
    new = []
    for col in range(LED_DIMENSIONS[1]):
        new.append(0xff00ff)
    colors.append(new)

def update():
    # update the colors
    for row in range(LED_DIMENSIONS[0]):
        for col in range(LED_DIMENSIONS[1]):
            colors[row][col] = random.randint(0, 0xffffff)

sv = SimulatorView(colors, LED_DIMENSIONS, update)
sv.draw()