class State:

    HAPPY = "happy"
    SAD = "sad"
    CONFUSED = "confused"
    FLIRTY = "flirty"

    def __init__(self):
        self.states = [self.HAPPY, self.SAD, self.CONFUSED, self.FLIRTY]

    def get_state(self):
        return self.states[0]

    def next_state(self):
        self.states = self.states[1:] + self.states[:1]