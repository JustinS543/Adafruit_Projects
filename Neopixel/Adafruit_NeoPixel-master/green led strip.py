import board
import neopixel
pixels = neopixel.NeoPixel(board.A1, 60)    # Feather wiring!
# pixels = neopixel.NeoPixel(board.D18, 30) # Raspberry Pi wiring!
pixels[0,2,4,6,8] = (255, 0, 0)
