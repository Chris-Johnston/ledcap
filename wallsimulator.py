"""
Simulator for the RGB cap lights.

Used to debug things before testing on the actual hardware.
"""

from treesimulatorview import TreeSimulatorView
from patternmanager import PatternManager
from simulatorcontroller import SimulatorController

if __name__ == "__main__":

    LED_DIMENSIONS = (1, 50)
    colors = []
    for row in range(LED_DIMENSIONS[0]):
        new = []
        for col in range(LED_DIMENSIONS[1]):
            new.append(0xff00ff)
        colors.append(new)
    pm = PatternManager(colors, LED_DIMENSIONS)
    sv = TreeSimulatorView(colors, LED_DIMENSIONS, pm.update)
    sc = SimulatorController(pm)
    sc.set_binds(sv.can)
    sv.draw()