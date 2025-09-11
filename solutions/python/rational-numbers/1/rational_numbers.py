class Rational:
    def __init__(self, numer, denom):
        highestfactor = self.hcf(numer, denom)
        self.numer = numer / highestfactor
        self.denom = denom / highestfactor

    def __eq__(self, other):
        return(
            self.numer == other.numer and 
            self.denom == other.denom
            )

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(
            self.numer * other.denom +
                self.denom * other.numer,
            self.denom * other.denom
            )

    def __sub__(self, other):
        return Rational(
            self.numer * other.denom -
                self.denom * other.numer,
            self.denom * other.denom
            )

    def __mul__(self, other):
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
            )

    def __truediv__(self, other):
        return Rational(
            self.numer * other.denom,
            self.denom * other.numer
            )

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(
            self.numer ** power, self.denom ** power
            )

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
    
    @staticmethod
    def hcf(x, y):
        while x:
            y, x = x, y % x
        return y
