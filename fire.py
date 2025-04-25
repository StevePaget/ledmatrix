from emulator import RGBMatrix
import random,time,math, colorsys

panel = RGBMatrix()
canvas = panel.CreateFrameCanvas()


class Flamepart():
    def __init__(self,hue, sat,size,y,x):
        self.hue = hue
        self.saturation = sat
        self.light = 255
        self.size = size
        self.y = y
        self.x = x

    def move(self):
        self.y -= 1
        self.size = self.size * 0.94
        self.light *= 0.99
        if int(self.size) == 0:
            return False
        return True
    
    def draw(self,canvas):
        for c in range(int(self.x-self.size),int(self.x-1 +self.size)):
            if 0<=c<=32:
                colour = colorsys.hsv_to_rgb(self.hue,self.saturation, self.light)
                canvas.SetPixel(c,self.y,int(colour[0]),int(colour[1]), int(colour[2] ))

class Flamegenerator():
    def __init__(self,x,size):
        self.life = random.randint(90,100)
        self.x = x
        self.size = size
        self.basex = x

    def update(self, parts, gens):
        parts.append(Flamepart(3/360, 1, self.size, 32, self.x))
        parts.append(Flamepart(34/360, 1, self.size-1, 32, self.x))
        parts.append(Flamepart(59/360, 1, self.size-3, 32, self.x))


        self.x = self.basex + random.randint(-2,2)
        self.life -=1
        if self.life < 5:
            self.size -=1
            if self.size == 0:
                return False
        return True




parts = []
gens = []

for i in range(3):
    xpos = random.randint(2,30)
    size = random.randint(4,9)
    gens.append(Flamegenerator(xpos, size))

colours = []
while True:
    nextparts = []
    nextgens = []
    canvas.Clear()
    for g in gens:
        if g.update(parts, gens):
            nextgens.append(g)
    gens = nextgens
    if len(gens) <2:
        xpos = random.randint(2,30)
        size = random.randint(4,9)
        gens.append(Flamegenerator(xpos, size))
    for p in parts:
        if p.move():
            p.draw(canvas)
            nextparts.append(p)
    parts = nextparts
    canvas.SwapOnVSync(canvas)
    time.sleep(0.05)

