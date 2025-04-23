import threebitslideshow as bits
import conway
import colours
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics


while True:
    matrix = RGBMatrix()
    bits.runSlideshow(matrix,cycles = 1)
    conway.runConway(matrix,cycles=1)
    colours.runColours(matrix, cycles=1)
