EAST = lambda x_y: (x_y[0] + 1, x_y[1])
NORTH = lambda x_y: (x_y[0], x_y[1] + 1)
WEST = lambda x_y: (x_y[0] - 1, x_y[1])
SOUTH = lambda x_y: (x_y[0], x_y[1] - 1)

TURNS = [EAST, NORTH, WEST, SOUTH]


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def advance(self):
        self.coordinates = self.bearing(self.coordinates)

    def turn_left(self):
        self.bearing = TURNS[
            (TURNS.index(self.bearing) + 1) % 4
            ]

    def turn_right(self):
        self.bearing = TURNS[
            (TURNS.index(self.bearing) - 1) % 4
            ]

    def simulate(self, moves):
        if not moves:
            print('beep, boop.. what to do..')
            
        for move in moves:
            if move == 'L':
                self.turn_left()
            elif move == 'R':
                self.turn_right()
            elif move == 'A':
                self.advance()
            else:
                raise ValueError(f'bad move: {move}')
            
