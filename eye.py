import math

class Eye:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def render_open(self, ctx):
        ctx.gray(0).arc(self.x, self.y, 10, 0, 2 * math.pi, True).fill()
        ctx.gray(1).arc(self.x - 5, self.y - 5, 2, 0, 2 * math.pi, True).fill()

    def render_winking(self, ctx):
        ctx.gray(0).begin_path()
        ctx.move_to(self.x - 10, self.y)
        ctx.curve_to(self.x, self.x * -1, self.x, self.x * -1, self.x + 10, self.y)
        ctx.stroke()

    def render_tear(self, ctx):
        self.render_open(ctx)
        ctx.rgb(0,0,1).arc(self.x, self.y + 10, 5, 0, 2 * math.pi, True).fill()
            