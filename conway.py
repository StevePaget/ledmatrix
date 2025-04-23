import json
import argparse
import time
import sys
import os, random
from copy import deepcopy

from emulator import RGBMatrix
#from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

def hex2rgb(hexval):
    colours = [int(hexval[1:3],16), int(hexval[3:5],16), int(hexval[5:],16)]
    for c in range(3):
        colours[c] = max(colours[c]-20,0)
    return colours


def nextphase(grid,size):
    newgrid = deepcopy(grid)
    for row in range(size):
        for col in range(size):
            # count neighbours
            tot = 0
            neighbours = ((-1,-1),(-1,0),(-1,1), (0,-1), (0,1), (1,-1),(1,0),(1,1))
            for n in neighbours:
                newx = (col+n[0])%size
                newy = (row+n[1])%size
                tot += grid[newy][newx]
            if tot >3:
                newgrid[row][col] = 0
            elif tot < 2:
                newgrid[row][col] = 0
            elif tot == 3 and grid[row][col]==0:
                newgrid[row][col] = 1
            else:
                newgrid[row][col] = grid[row][col]
    return newgrid

def LEDGrid(grid, canvas,size,matrix):
    canvas.Clear()
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 1:
                canvas.SetPixel(col, row, 180,180,180)
            else:
                canvas.SetPixel(col, row, 0 , 0, 0)
    canvas = matrix.SwapOnVSync(canvas)

def runConway(matrix, cycles=None):
    size = 32
    canvas = matrix.CreateFrameCanvas()          
    generationcount = 0
    cyclecount = -1
    while cycles is None or cyclecount < cycles:
        if generationcount== 0:
            cyclecount +=1
            grid = [[ random.choice([0,1]) for col in range(size)] for row in range(size)]
        grid = nextphase(grid,size)
        LEDGrid(grid, canvas,size,matrix)
        generationcount = (generationcount+1)%500
        time.sleep(0.1)

if __name__ == "__main__":
    matrix = RGBMatrix()
    runConway(matrix)
