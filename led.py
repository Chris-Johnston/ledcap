"""
LED Driver

This is the actual thing that drives the LEDS
"""

LED_DIMENSIONS = (14, 14)
colors = []
for row in range(LED_DIMENSIONS[0]):
    new = []
    for col in range(LED_DIMENSIONS[1]):
        new.append(0xff00ff)
    colors.append(new)

pm = PatternManager(colors, LED_DIMENSIONS)
