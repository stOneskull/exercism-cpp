class Clock:
    def __init__(self, hour, minute):
        hour += minute // 60
        minute = minute % 60
        self.hour = hour % 24
        self.minute = minute

    def __repr__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minute)

    def __eq__(self, other):
        return(
            self.hour == other.hour
            and self.minute == other.minute)

    def __add__(self, minutes):
        self.minute += minutes
        self.hour += self.minute // 60
        self.hour = self.hour % 24
        self.minute = self.minute % 60
        return self

    def __sub__(self, minutes):
        if minutes > self.minute:
            if minutes > 60:
                self.hour -= minutes // 60
            else:
                self.hour -= 1
        self.minute -= minutes
        self.minute = self.minute % 60
        return self

