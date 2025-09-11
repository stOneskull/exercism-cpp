EAST = lambda xy: (xy[0] + 1, xy[1])
NORTH = lambda xy: (xy[0], xy[1] + 1)
WEST = lambda xy: (xy[0] - 1, xy[1])
SOUTH = lambda xy: (xy[0], xy[1] - 1)

TURNS = [EAST, NORTH, WEST, SOUTH]

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def advance(self):
        self.coordinates = self.bearing(self.coordinates)

    def turn_left(self):
        self.bearing = TURNS[(TURNS.index(self.bearing) + 1) % 4]

    def turn_right(self):
        self.bearing = TURNS[(TURNS.index(self.bearing) - 1) % 4]

    def simulate(self, command):
        if command:
            for move in command:
                if move == 'L':
                    self.turn_left()
                elif move == 'R':
                    self.turn_right()
                elif move == 'A':
                    self.advance()
                else:
                    raise ValueError(
                        'Incorrect command in simulate sequence: ' + move
                        )
        else:
            print('beep, boop.. what to do..')