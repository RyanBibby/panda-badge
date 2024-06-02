from events.input import Buttons, BUTTON_TYPES

class ButtonHelper:

    def __init__(self, app):
        self.button_states = Buttons(app)

    def confirm_pressed(self):
        return self.button_states.get(BUTTON_TYPES["CONFIRM"])

    def cancel_pressed(self):
        return self.button_states.get(BUTTON_TYPES["CANCEL"])

    def left_pressed(self):
        return self.button_states.get(BUTTON_TYPES["LEFT"])

    def any_buttons_pressed(self):
        
        return self.button_states.get(BUTTON_TYPES["UP"]) or \
        self.button_states.get(BUTTON_TYPES["DOWN"]) or \
        self.button_states.get(BUTTON_TYPES["LEFT"]) or \
        self.button_states.get(BUTTON_TYPES["RIGHT"]) or \
        self.button_states.get(BUTTON_TYPES["CONFIRM"]) or \
        self.button_states.get(BUTTON_TYPES["CANCEL"])