"""
View

Abstract class responsible for drawing the state of the lights
either for the simulator or for the hardware.

Calls the update method before each call.

Maintains a delta time, which is how long it took in between each update.
"""

from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def draw():
        """
        Draws the state of the lights
        on the GUI or actual hardware.
        """
        pass