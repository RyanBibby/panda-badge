import math

class Mouth:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def render_open(self, ctx):
        ctx.gray(0).arc(self.x, self.y, 10, 0, 2 * math.pi, True).fill()
        ctx.gray(1).arc(self.x - 5, self.y - 5, 2, 0, 2 * math.pi, True).fill()

