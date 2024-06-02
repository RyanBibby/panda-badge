import asyncio
import app
import math
import random
import sys
from tildagonos import tildagonos
from .face import Face
from .colour import Colour
from .background import Background
from .ticker import Ticker


from events.input import Buttons, BUTTON_TYPES
from app_components import clear_background

from system.eventbus import eventbus
from system.patterndisplay.events import *

class App(app.App):

    def __init__(self):

        self.button_states = Buttons(self)
        self.tick = 0
        self.emotion = "happy"
  
        self.can_change = True
        self.manual = False

     
        self.tounge = False

        self.background = Background()
        self.face = Face()


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

        self.background.render(ctx)
        self.face.render(ctx, self.emotion)

        self.render_heart(ctx)
        
        Ticker.tick()

    def render_heart(self, ctx):

        if Ticker.is_active_frame() or self.manual:

            ctx.linear_gradient(-100, -120, 90, -10)
            ctx.add_stop(0, (255,200,200), 1)
            ctx.add_stop(1, (200,0,0), 1)
            ctx.add_stop(2, (0,0,0), 1)

            ctx.begin_path()
            ctx.move_to(0, -90)
            ctx.curve_to(70, -110, 100, -60, 0, -35)
            ctx.fill()
            ctx.move_to(0, -90)
            ctx.curve_to(-70, -110, -100, -60, 0, -35)
            ctx.fill()
     


__app_export__ = App