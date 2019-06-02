"""
Led Controller
"""

from controller import Controller
import RPi.GPIO as GPIO

BUTTON_NEXT = 21
BUTTON_PREV = 12

class LedController(Controller):
    def __init__(self, pm):
        super().__init__(pm)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_PREV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # TODO ensure that the leds don't break this
        # may have to poll instead
        GPIO.add_event_detect(BUTTON_NEXT, GPIO.FALLING, callback=self.next_callback, bouncetime=200)
        GPIO.add_event_detect(BUTTON_PREV, GPIO.FALLING, callback=self.prev_callback, bouncetime=200)

    def prev_callback(self, event):
        self.pattern_manager.prev_pattern()

    def next_callback(self, event):
        self.pattern_manager.next_pattern()
