from .ticker import Ticker

class Mouth:

    def render_smile(self, ctx):
        ctx.gray(0).begin_path()
        ctx.move_to(-10,65)
        ctx.curve_to(0, 75, 0, 75, 10, 65)
        ctx.stroke()

    def render_sad(self, ctx):
        ctx.gray(0).begin_path()
        ctx.move_to(-10,70)
        ctx.curve_to(0, 60, 0, 60, 10, 70)
        ctx.stroke()
    
    def render_confused(self, ctx):
        ctx.gray(0).begin_path()
        ctx.move_to(-10,70)
        ctx.curve_to(0, 75, 5, 60, 10, 70)
        ctx.stroke()

    def render_flirty(self, ctx):
        if Ticker.is_active_frame():
            ctx.rgb(1,0,0).begin_path()
            ctx.move_to(-5,71)
            ctx.curve_to(-6, 83, 6, 83, 5, 71)
            ctx.fill()         

        self.render_smile(ctx)


