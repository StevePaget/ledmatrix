import random, time, sys, os
import pixeldata as pix
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))
from rgbmatrix import RGBMatrix, RGBMatrixOptions

class SlideShow():
    def __init__(self, matrix):
        self.matrix=matrix
        self.drawPixels()

    def from_rgb(self,rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb

    def drawPixels(self):
        colourdata = pix.pixels.strip()
        position = 0
        offset_canvas = self.matrix.CreateFrameCanvas()
        while True:
            for char in colourdata:
                if len(char.strip())==0:
                    continue
                row = position//32
                col = position%32
                colourBoxes = [pix.colour0, pix.colour1, pix.colour2, pix.colour3, pix.colour4, pix.colour5, pix.colour6, pix.colour7]
                thiscolour=None
                try:
                    thiscolour = colourBoxes[int(char)]
                    offset_canvas.SetPixel(col,row,thiscolour)
                except:
                    offset_canvas.SetPixel(col,row,20,20,20)
                position+=1
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

matrix = RGBMatrix()

if __name__ == "__main__":
    app = SlideShow(matrix)
