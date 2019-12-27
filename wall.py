"""
Light Wall
"""

from patternmanager import PatternManager
from ledcontroller import LedController
from wallview import WallView

LED_DIMENSIONS = (6, 16)
colors = []
for row in range(LED_DIMENSIONS[0]):
    new = []
    for col in range(LED_DIMENSIONS[1]):
        new.append(0xff00ff)
    colors.append(new)

pm = PatternManager(colors, LED_DIMENSIONS)
lv = WallView(colors, LED_DIMENSIONS, pm.update)
lc = LedController(pm)
lv.draw()

