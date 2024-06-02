import asyncio
import app
import math
import random
import sys
from tildagonos import tildagonos
from .face import Face


from events.input import Buttons, BUTTON_TYPES
from app_components import clear_background

from system.eventbus import eventbus
from system.patterndisplay.events import *

class Panda(app.App):
    def __init__(self):
        # exec(compile(open('face.py', "rb").read(), 'face.py', 'exec'), globals, locals)
        self.button_states = Buttons(self)
        self.tick = 0
        self.show = True
        self.emotion = "happy"
        self.r = 0.5
        self.g = 0.5
        self.b = 0.5
        self.can_change = True
        self.manual = False


        self.left_eye = True
        self.right_eye = True
        self.tounge = False

        face = Face()
        face.moo()

    def hsv_to_rgb(self,h, s, v):
        if s == 0.0:
            return v, v, v
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        if i == 0:
            return v, t, p
        if i == 1:
            return q, v, p
        if i == 2:
            return p, v, t
        if i == 3:
            return p, q, v
        if i == 4:
            return t, p, v
        if i == 5:
            return v, p, q

    def update(self, delta):
        if self.manual:   
            for i in range(0,12):
                tildagonos.leds[i+1] = (100, 100, 100)
        if self.button_states.get(BUTTON_TYPES["CANCEL"]) and self.button_states.get(BUTTON_TYPES["LEFT"]):
            self.manual = not self.manual
            if self.manual:
                eventbus.emit(PatternDisable())
            else:
                eventbus.emit(PatternEnable())
        elif self.button_states.get(BUTTON_TYPES["DOWN"]):
            self.tounge = not self.tounge
        elif self.button_states.get(BUTTON_TYPES["CANCEL"]):
            # self.button_states.clear()
            # self.minimise()
            True
        elif self.can_change and self.button_states.get(BUTTON_TYPES["CONFIRM"]): 
            if self.emotion == "happy":
                self.emotion = "sad"
            elif self.emotion == "sad":
                self.emotion = "confused"
            elif self.emotion == "confused":
                self.emotion = "flirty"
            else:
                self.emotion = "happy"
            self.can_change = False
        elif not self.button_states.get(BUTTON_TYPES["CONFIRM"]):
            self.can_change = True
            # # The button_states do not update while you are in the background.
            # # Calling clear() ensures the next time you open the app, it stays open.
            # # Without it the app would close again immediately.
            # self.button_states.clear()

    def draw(self, ctx):
        clear_background(ctx)

        # Bg
        # ctx.rgb(self.r,self.g, self.b).rectangle(-120,-120,240,240).fill()

        rr, gg, bb = self.hsv_to_rgb(self.tick / 100.0,1,1)
        ctx.rgb(rr,gg, bb).rectangle(-120,-120,240,240).fill()
        

        # Ears
        ctx.linear_gradient(-55, -20, -35, 0)
        ctx.add_stop(0, (100,100,100), 1)
        ctx.add_stop(1, (0,0,0), 1)
        ctx.arc(-45, -10, 20, 0, 2 * math.pi, True).fill()

        ctx.linear_gradient(35, -20, 55, 0)
        ctx.add_stop(0, (100,100,100), 1)
        ctx.add_stop(1, (0,0,0), 1)
        ctx.arc(45, -10, 20, 0, 2 * math.pi, True).fill()


        # ctx.gray(0).arc(-45, -10, 20, 0, 2 * math.pi, True).fill()
        # ctx.gray(0).arc(45, -10, 20, 0, 2 * math.pi, True).fill()

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


        # Eyes
        ctx.gray(0).arc(25, 30, 10, 0, 2 * math.pi, True).fill()
        ctx.gray(1).arc(20, 25, 2, 0, 2 * math.pi, True).fill()

        if self.emotion == "flirty" and self.show and (not self.manual):
            ctx.gray(0).begin_path()
            ctx.move_to(-35, 30)
            ctx.curve_to(-25, 25, -25, 25, -15, 30)
            ctx.stroke()
        else:
            ctx.gray(0).arc(-25, 30, 10, 0, 2 * math.pi, True).fill()
            ctx.gray(1).arc(-30, 25, 2, 0, 2 * math.pi, True).fill()

        if self.emotion == "sad":
            ctx.rgb(0,0,1).arc(25, 40, 5, 0, 2 * math.pi, True).fill()
            

        # Snout 
        ctx.linear_gradient(-20, 45, 40, 105)
        ctx.add_stop(0, (240,240,240), 1)
        ctx.add_stop(1, (50,50,50), 1)
        ctx.arc(0, 60, 30, 0, 2 * math.pi, True).fill()


        # ctx.gray(0.5).arc(0, 60, 30, 0, 2 * math.pi, True).fill()

        # Nose
        ctx.gray(0).begin_path()
        ctx.move_to(-10,50)
        ctx.curve_to(0, 60, 0, 60, 10, 50)
        ctx.fill()

        # Hat
        ctx.rgb(1,0,0).begin_path()
        ctx.move_to(-40, -40)

        # Smile

        if (self.emotion == "flirty" and not self.manual) or (self.manual and self.tounge):
            ctx.rgb(1,0,0).begin_path()
            ctx.move_to(-5,71)
            ctx.curve_to(-6, 83, 6, 83, 5, 71)
            ctx.fill()

        if self.emotion == "happy" or self.emotion == "flirty" or self.manual:
            ctx.gray(0).begin_path()
            ctx.move_to(-10,65)
            ctx.curve_to(0, 75, 0, 75, 10, 65)
            ctx.stroke()
        elif self.emotion == "confused":
            ctx.gray(0).begin_path()
            ctx.move_to(-10,70)
            ctx.curve_to(0, 75, 5, 60, 10, 70)
            ctx.stroke()
        else:
            ctx.gray(0).begin_path()
            ctx.move_to(-10,70)
            ctx.curve_to(0, 60, 0, 60, 10, 70)
            ctx.stroke()
        
     


        # Heart
        
        if self.show or self.manual:

            ctx.linear_gradient(-100, -120, 90, -10)
            ctx.add_stop(0, (255,200,200), 1)
            ctx.add_stop(1, (200,0,0), 1)
            ctx.add_stop(2, (0,0,0), 1)

            ctx.begin_path()
            ctx.move_to(0, -90);
            ctx.curve_to(70, -110, 100, -60, 0, -35);
            ctx.fill();
            ctx.move_to(0, -90);
            ctx.curve_to(-70, -110, -100, -60, 0, -35);
            ctx.fill();


            # ctx.rgb(1,0,0).begin_path()

            # ctx.move_to(0, -90);
            # ctx.curve_to(70, -110, 100, -60, 0, -40);
            # ctx.fill();
            # ctx.move_to(0, -90);
            # ctx.curve_to(-70, -110, -100, -60, 0, -40);
            # ctx.fill();

        self.tick = self.tick + 1
        if self.tick % 5 == 0:
            self.show = not self.show
            self.r = random.randint(0, 100) / 100.0
            self.g = random.randint(0, 100) / 100.0
            self.b = random.randint(0, 100) / 100.0



__app_export__ = Panda