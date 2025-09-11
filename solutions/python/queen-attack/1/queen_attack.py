class Queen(object):
    def __init__(self, row, column):
        if not 8 > row > -1 < column < 8:
            raise ValueError('cannot go there')

        self.row = row
        self.column = column


    def can_attack(self, other):
        if (self.row == other.row and
            self.column == other.column):
            raise ValueError('queens in same square')

        return(
            self.row == other.row or
            self.column == other.column or
            abs(self.row - other.row) ==
            abs(self.column - other.column)
            )
