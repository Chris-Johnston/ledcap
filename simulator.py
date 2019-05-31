"""
Simulator for the RGB cap lights.

Used to debug things before testing on the actual hardware.
"""

from simulatorview import SimulatorView
from patternmanager import PatternManager
from simulatorcontroller import SimulatorController

LED_DIMENSIONS = (14, 14)
colors = []
for row in range(LED_DIMENSIONS[0]):
    new = []
    for col in range(LED_DIMENSIONS[1]):
        new.append(0xff00ff)
    colors.append(new)

pm = PatternManager(colors, LED_DIMENSIONS)
sv = SimulatorView(colors, LED_DIMENSIONS, pm.update)
sc = SimulatorController(pm)
sc.set_binds(sv.can)
sv.draw()