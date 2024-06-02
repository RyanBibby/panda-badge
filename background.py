from .colour import Colour

class Background:

    def __init__(self):
        self.tick = 0

    def render(self, ctx):
        r, g, b = Colour.hsv_to_rgb(self.tick / 100.0,1,1)
        ctx.rgb(r,g, b).rectangle(-120,-120,240,240).fill()
        self.tick += 1
