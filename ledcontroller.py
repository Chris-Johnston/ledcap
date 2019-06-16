"""
Led Controller
"""

from controller import Controller
import RPi.GPIO as GPIO
import time

BUTTON_NEXT = 21
BUTTON_PREV = 12
# dunno exactly what I'll use these extra buttons for
BUTTON_HOLD = 25
BUTTON_OFF = 24
BUTTON_ON = 23

BOUNCE_TIME = 200

class LedController(Controller):
    def __init__(self, pm):
        super().__init__(pm)
        self.holding = False
        self.off_index = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTON_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_PREV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_ON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_OFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_HOLD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # looks like this doesn't break, despite using interrupts
        GPIO.add_event_detect(BUTTON_NEXT, GPIO.FALLING, callback=self.next_callback, bouncetime=BOUNCE_TIME)
        GPIO.add_event_detect(BUTTON_PREV, GPIO.FALLING, callback=self.prev_callback, bouncetime=BOUNCE_TIME)
        GPIO.add_event_detect(BUTTON_ON, GPIO.FALLING, callback=self.on_callback, bouncetime=BOUNCE_TIME)
        GPIO.add_event_detect(BUTTON_OFF, GPIO.FALLING, callback=self.off_callback, bouncetime=BOUNCE_TIME)
        GPIO.add_event_detect(BUTTON_HOLD, GPIO.FALLING, callback=self.hold_callback, bouncetime=BOUNCE_TIME)

    def off_callback(self, event):
        if not self.holding and not self.pattern_manager.is_off():
            self.off_index = self.pattern_manager.handler_index
            self.pattern_manager.off()

    def on_callback(self, event):
        if not self.holding and self.pattern_manager.is_off():
            self.pattern_manager.set_index(self.off_index)

    def hold_callback(self, event):
        start = time.time()
        while GPIO.input(BUTTON_HOLD) == GPIO.LOW:
            time.sleep(0.01)
        delta = time.time() - start
        if delta > 3:
            self.holding = not self.holding
            print('holding: ', self.holding)

    def prev_callback(self, event):
        if not self.holding:
            self.pattern_manager.prev_pattern()

    def next_callback(self, event):
        if not self.holding:
            self.pattern_manager.next_pattern()
