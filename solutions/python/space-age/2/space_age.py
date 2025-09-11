class SpaceAge:
    ratios = dict(
        on_mercury = 0.2408467,
        on_venus = 0.61519726,
        on_earth = 1,
        on_mars = 1.8808158,
        on_jupiter = 11.862615,
        on_saturn = 29.447498,
        on_uranus = 84.016846,
        on_neptune = 164.79132,
        )

    def __init__(self, seconds, year=31557600):
        self.seconds = seconds
        self.age = seconds/year
        for planet, ratio in self.ratios.items():
            setattr(self, planet, self.agefunc(ratio))

    def agefunc(self, ratio):
        return lambda: round(self.age/ratio, 2)
