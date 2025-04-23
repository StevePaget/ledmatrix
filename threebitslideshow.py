import json
import argparse
import time
import sys
import os, random
import pixeldata as pix



sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

def hex2rgb(hexval):
    colours = [int(hexval[1:3],16), int(hexval[3:5],16), int(hexval[5:],16)]
    for c in range(3):
        colours[c] = max(colours[c]-20,0)
    return colours

def run(matrix, filename, colourboxes, colourdata):
    offset_canvas = matrix.CreateFrameCanvas()
    font = graphics.Font()
    font.LoadFont("/home/pi/ledmatrix/7x13.bdf")
    textColor = graphics.Color(255, 255, 0)
    pos = offset_canvas.width
    my_text = filename[:-3]
    thiscolour=None
    # text title
    end = pos
    while end > 0:
        offset_canvas.Clear()
        txtlen = graphics.DrawText(offset_canvas, font, pos, 10, textColor, my_text)
        pos -= 1
        end = pos + txtlen
        time.sleep(0.05)
        offset_canvas = matrix.SwapOnVSync(offset_canvas)

    # image
    count=0
    charposition = 0
    while count < 25:
        displayposition = 0
        if charposition > len(colourdata)-500:
            charposition = 0
        displayposition=0
        while displayposition < 1024 and charposition < len(colourdata):
            char = colourdata[charposition]
            if len(char.strip())==0:
                charposition += 1
                continue
            row = displayposition//32
            col = displayposition%32
            thiscolour=None
            thiscolour = colourboxes[int(char)]
            offset_canvas.SetPixel(col,row,thiscolour[0], thiscolour[1], thiscolour[2])
            displayposition+=1
            charposition+=1  
        offset_canvas = matrix.SwapOnVSync(offset_canvas)
        time.sleep(1)
        count +=1


def parsefile(filename):
    print(filename)
    f  = open("/home/pi/ledmatrix/studentfiles/" + filename).readlines()
    # get colours
    colournum = 0
    linenum=0
    colourboxes = [(),(),(),(),(),(),(),()]
    while colournum < 8:
        if "colour" in f[linenum]:
            bits = f[linenum].strip().split()
            colourboxes[colournum] = hex2rgb(bits[-1][1:-1])
            colournum += 1
        linenum+=1
    while "pixels" not in f[linenum]:
        linenum +=1
    linenum+=1
    colourdata = ""
    while '"""' not in f[linenum]:
        colourdata += f[linenum].strip()
        linenum+=1
    return colourboxes, colourdata

def runSlideshow(matrix, cycles=None):

    files = os.listdir("/home/pi/ledmatrix/studentfiles/")
    # Start loop
    cyclecount = 0

    while cycles is None or cyclecount < cycles:
        print(cycles, cyclecount)
        cyclecount += 1
        thisfile = random.choice(files)
        colourboxes, colourdata = parsefile(thisfile)
        run(matrix, thisfile, colourboxes, colourdata)

if __name__ == "__main__":
    matrix = RGBMatrix()
    runSlideshow(matrix)

