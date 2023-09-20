import argparse
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions


def run(matrix):
    offset_canvas = matrix.CreateFrameCanvas()
    while True:
        for x in range(0, matrix.width):
            offset_canvas.SetPixel(x, x, 255, 255, 255)
            offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)

        for x in range(0, offset_canvas.width):
            offset_canvas.SetPixel(x, 0, 255, 0, 0)
            offset_canvas.SetPixel(x, offset_canvas.height - 1, 255, 255, 0)

        for y in range(0, offset_canvas.height):
            offset_canvas.SetPixel(0, y, 0, 0, 255)
            offset_canvas.SetPixel(offset_canvas.width - 1, y, 0, 255, 0)
        offset_canvas = matrix.SwapOnVSync(offset_canvas)


matrix = RGBMatrix()

try:
    # Start loop
    print("Press CTRL-C to stop sample")
    run(matrix)
except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)
