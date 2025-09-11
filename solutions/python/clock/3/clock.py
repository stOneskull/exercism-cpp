class Clock:
    def __init__(self, hour, minute):
        hour += minute // 60
        self.hour = hour % 24
        self.minute = minute % 60

    def __repr__(self):
        return '{:02d}:{:02d}'.format(
            self.hour, self.minute)

    def __eq__(self, other):
        return(self.hour == other.hour
            and self.minute == other.minute)

    def __add__(self, minutes):
        self.minute += minutes
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self

    def __sub__(self, minutes):
        return self.__add__(-minutes)
