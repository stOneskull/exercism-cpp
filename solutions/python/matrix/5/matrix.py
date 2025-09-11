class Matrix:

    def __init__(self, matrix):
        self.rows = [
            [int(num) for num in row.split()]
            for row in matrix.splitlines()
        ]
        self.cols = [
            list(col) for col in zip(*self.rows)
        ]

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.cols[index-1]
