import random,math
import colorsys
import time

#from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from emulator import RGBMatrix
class ColourBall():
    def __init__(self,x,y,radius, angle,speed, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.xspeed = math.cos(angle)*speed
        self.yspeed = math.sin(angle)*speed
        self.colour = colour 

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if not (0 <= self.x-self.radius and self.x+self.radius < 32):
            self.xspeed *= -1
        if not (0 <= self.y-self.radius and self.y+self.radius < 32):
            self.yspeed *= -1
            
    def getpixelcolour(self,x,y):
        
        # calculates how much colour to give to a pixel, based on distance
        dist = math.sqrt(abs(self.x - x)**2 + abs(self.y-y)**2)
        if dist > self.radius:
            return [0,0,0]
        fullcolourHSL = colorsys.rgb_to_hsv(self.colour[0], self.colour[1], self.colour[2])
        distFactor = 1-dist/8
        newV = max(0,fullcolourHSL[2]*distFactor)
        return [int(c) for c in colorsys.hsv_to_rgb(fullcolourHSL[0], fullcolourHSL[1], newV) ]
        

def LEDGrid(canvas,matrix, balls, gridsize):
    for row in range(gridsize):
        for col in range(gridsize):
            colour = [0,0,0]
            for b in balls:
                distcolour = b.getpixelcolour(col,row)
                colour[0] += distcolour[0]
                colour[1] += distcolour[1]
                colour[2] += distcolour[2]
            canvas.SetPixel(col, row, min(255,colour[0]), min(255,colour[1]), min(255,colour[2]))

def runColours(matrix, cycles=None):
    canvas = matrix.CreateFrameCanvas()
    balls = []
    balls.append(ColourBall(16,15,5,random.randint(0,360),1, (255,0,0)))
    balls.append(ColourBall(20,5,5,random.randint(0,360),2, (0,255,0)))
    balls.append(ColourBall(5,12,5,random.randint(0,360),1, (0,0,255)))
    balls.append(ColourBall(20,5,5,random.randint(0,360),2, (80,80,80)))
    cyclesdone = 0
    while cycles is None or cyclesdone < cycles:
        cyclesdone+=1
        for _ in range(200):
            canvas.Clear()
            for b in balls:
                b.move()
            LEDGrid(canvas, matrix, balls, 32)
            canvas = matrix.SwapOnVSync(canvas)
            time.sleep(0.01)

if __name__ == "__main__":
    matrix = RGBMatrix()
    runColours(matrix, cycles=None)
