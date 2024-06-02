import app
from tildagonos import tildagonos
from system.eventbus import eventbus
from system.patterndisplay.events import *
from app_components import clear_background

from .face import Face
from .colour import Colour
from .background import Background
from .ticker import Ticker
from .state import State
from .button_helper import ButtonHelper

class App(app.App):

    def __init__(self):

        self.button_helper = ButtonHelper(self)
        self.state = State()
        self.background = Background()
        self.face = Face()

        self.free_to_update = True

    def update(self, delta):

        if self.button_helper.cancel_pressed() and self.button_helper.left_pressed() and self.free_to_update:
            # Change mode here
            self.free_to_update = False
        elif self.free_to_update and self.button_helper.confirm_pressed(): 
            self.state.next_state()
            self.free_to_update = False
        elif not self.button_helper.any_buttons_pressed():
            self.free_to_update = True

    def draw(self, ctx):

        clear_background(ctx)

        self.background.render(ctx)
        self.face.render(ctx, self.state.get_state())

        self.render_heart(ctx)
        
        Ticker.tick()

    def render_heart(self, ctx):

        if Ticker.is_active_frame():

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