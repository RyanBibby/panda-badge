from .colour import Colour
from .ticker import Ticker

class Background:

    def render(self, ctx):
        r, g, b = Colour.hsv_to_rgb(Ticker.get_tick() / 100.0,1,1)
        ctx.rgb(r,g, b).rectangle(-120,-120,240,240).fill()
