class Ticker:
    
    tick_frame = 0
    tock = False

    @classmethod
    def is_active_frame(cls):
        return cls.tock

    @classmethod
    def tick(cls):
        if cls.tick_frame % 5 == 0:
            cls.tock = not cls.tock
        cls.tick_frame += 1

    @classmethod
    def get_tick(cls):
        return cls.tick_frame