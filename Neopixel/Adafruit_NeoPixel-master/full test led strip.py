# Circuit Playground NeoPixel
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.A1, 10, brightness=0.2, auto_write=True)

# choose which demos to play
# 1 means play, 0 means don't!
color_chase_demo = 1
flash_demo = 1
rainbow_demo = 1
rainbow_cycle_demo = 1


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(10):
            rc_index = (i * 256 // 60) + j * 5
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

while True:
    if color_chase_demo:
        color_chase(RED, 0.2)  # Increase the number to slow down the color chase
        color_chase(YELLOW, 0.2)
        color_chase(GREEN, 0.2)
        color_chase(CYAN, 0.2)
        color_chase(BLUE, 0.2)
        color_chase(PURPLE, 0.2)
        color_chase(OFF, 0.2)

    if flash_demo:
        pixels.fill(RED)
        pixels.show()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(1)
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(1)
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(1)
        pixels.fill(WHITE)
        pixels.show()
        time.sleep(1)

    if rainbow_cycle_demo:
        rainbow_cycle(0.05)  # Increase the number to slow down the rainbow.

    if rainbow_demo:
        rainbow(0.05)  # Increase the number to slow down the rainbow.
