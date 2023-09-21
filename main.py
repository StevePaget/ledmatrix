
###############################################
# You don't need to edit this! 
# Open the pixeldata.py file and edit that
###############################################


from tkinter import *
import tkinter.font as tkFont
import random
import pixeldata as pix

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Consolas", size=18)
        self.geometry("640x640")
        self.config(bg="#000000")
        
        self.theCanvas = Canvas(self, width=640,height = 640, bg="#000000")
        self.theCanvas.grid(row=0, column=0, rowspan=7)
        self.drawPixels(None)
        self.mainloop()
    
    def from_rgb(self,rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb      
    
    def drawPixels(self,e):
        colourdata = pix.pixels.strip()
        position =0
        for char in colourdata:
            if len(char.strip())==0:
                continue
            row = position//32
            col = position%32
            colourBoxes = [pix.colour0, pix.colour1, pix.colour2, pix.colour3, pix.colour4, pix.colour5, pix.colour6, pix.colour7]
            thiscolour=None
            try:
                thiscolour = colourBoxes[int(char)]
                self.theCanvas.create_rectangle(col*20,row*20,col*20+20,row*20+20,fill=thiscolour)
            except:
                self.theCanvas.create_rectangle(col*20,row*20,col*20+20,row*20+20,fill="#000000")
                if not thiscolour:
                    print("{} not between 0 and 7".format(char))
                else:
                    print("{} not a colour".format(thiscolour))
            position+=1
        



if __name__ == "__main__":
    app = App()