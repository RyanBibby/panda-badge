
import math
from .eye import Eye
from .ticker import Ticker

class Face:
    def __init__(self):
        self.left_eye = Eye(-25, 30)
        self.right_eye = Eye(25, 30)

        self.left_ear = None
        self.right_ear = None

        self.mouth = None

        self.heart = None
    


    def render(self, ctx, emotion):
        # Ears
        ctx.linear_gradient(-55, -20, -35, 0)
        ctx.add_stop(0, (100,100,100), 1)
        ctx.add_stop(1, (0,0,0), 1)
        ctx.arc(-45, -10, 20, 0, 2 * math.pi, True).fill()

        ctx.linear_gradient(35, -20, 55, 0)
        ctx.add_stop(0, (100,100,100), 1)
        ctx.add_stop(1, (0,0,0), 1)
        ctx.arc(45, -10, 20, 0, 2 * math.pi, True).fill()

        # Head
        ctx.linear_gradient(0, 0, 100, 100)
        ctx.add_stop(0, (255,255,255), 1)
        ctx.add_stop(1, (50,50,50), 1)
        ctx.add_stop(2, (0,0,0), 1)
        ctx.arc(0, 30, 60, -0.25 * math.pi, 1.25 * math.pi, False).fill()

        ctx.begin_path()
        ctx.move_to(-45,-10)
        ctx.curve_to(-16, -35, 16, -35, 45, -10)
        ctx.fill()



        if emotion == "sad":
            self.right_eye.render_tear(ctx)
        else:
            self.right_eye.render_open(ctx)

        # if emotion == "flirty" and self.show and (not self.manual):


        if emotion == "flirty" and Ticker.is_active_frame():
            self.left_eye.render_winking(ctx)
        else:
            self.left_eye.render_open(ctx)