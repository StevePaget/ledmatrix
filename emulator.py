import pygame_functions as pyg
import random

class RGBMatrix:
    def __init__(self):
        self.LEDsWide = 32
        self.LEDSize = 20
        pyg.screenSize(self.LEDsWide*self.LEDSize,self.LEDsWide*self.LEDSize)
        pyg.setBackgroundColour("black")
        pyg.setAutoUpdate(False)

    def CreateFrameCanvas(self):
        return self
    
    def Clear(self):
        pyg.clearShapes()

    def SetPixel(self,row,col,r,g,b):
        colour = pyg.parseColour((r,g,b))
        pyg.drawEllipse(row*self.LEDSize+self.LEDSize//2, col * self.LEDSize+self.LEDSize//2, self.LEDSize, self.LEDSize, colour)

    def SwapOnVSync(self,c):
        pyg.updateDisplay()
        return self

if __name__ == "__main__":
    app = RGBMatrix()
    m = app.CreateFrameCanvas()
    while True:
        m.Clear()
        for row in range(32):
            for col in range(32):
                m.SetPixel(row,col, random.randint(0,255),random.randint(0,255),random.randint(0,255))
        m = app.SwapOnVSync(m)
        pyg.pause(100)
    pyg.endWait()
