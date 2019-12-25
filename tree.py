"""
LED Tree Driver

This is the actual thing that drives the LEDS
"""

from patternmanager import PatternManager
from ledcontroller import LedController
from treeview import TreeLedView

LED_DIMENSIONS = (1, 50)
colors = []
for row in range(LED_DIMENSIONS[0]):
    new = []
    for col in range(LED_DIMENSIONS[1]):
        new.append(0xff00ff)
    colors.append(new)

pm = PatternManager(colors, LED_DIMENSIONS)
lv = TreeLedView(colors, LED_DIMENSIONS, pm.update)
lc = LedController(pm)
lv.draw()

