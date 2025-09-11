class Clock:
    def __init__(self, hour, minute):
        self.minutes = hour*60 + minute

    def __repr__(self):
        hour, minute = divmod(self.minutes, 60)
        return f'{hour%24:02d}:{minute:02d}'

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        self.minutes += minutes
        return self

    def __sub__(self, minutes):
        self.minutes -= minutes
        return self