
import argparse
import time
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions


def run(matrix):
    colours = [(255,0,0), (0,200,0) , (20,20,190), (100,0,100), (100,100,0)]
    offset_canvas = matrix.CreateFrameCanvas()
    thisOffset=0
    while True:
        thisOffset+=1
        for row in range(0, matrix.height):
            for col in range(0,matrix.width):
                offset_canvas.SetPixel(col, row, colours[((row+thisOffset)//5)%5][0], colours[((row+thisOffset)//5)%5][1], colours[((row+thisOffset)//5)%5][2])
        thisOffset +=1
        offset_canvas = matrix.SwapOnVSync(offset_canvas)
        time.sleep(0.1)


matrix = RGBMatrix()

try:
    # Start loop
    print("Press CTRL-C to stop sample")
    run(matrix)
except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)
