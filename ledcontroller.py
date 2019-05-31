"""
Led Controller
"""

from controller import Controller
import RPi.GPIO as GPIO

BUTTON_NEXT = 10

class LedController(Controller):
    def __init__(self, pm):
        super().__init__(pm)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # TODO ensure that the leds don't break this
        # may have to poll instead
        GPIO.add_event_detect(BUTTON_NEXT, GPIO.RISING, callback=self.next_callback)

    def next_callback(self, event):
        self.pattern_manager.next_pattern()
