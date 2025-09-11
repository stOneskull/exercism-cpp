class ConnectGame:
    def __init__(self, board):
        self.rows = [
            ''.join(line.split())
            for line in board.splitlines()]

        rolen = len(self.rows[0])
        colen = len(self.rows)

        self.tokens = {
            'X': {
                'start': [
                    (0, row) for row in range(rolen)],
                'end': [
                    (rolen-1, row) for row in range(rolen)]
                    },
            'O': {
                'start': [
                    (col, 0) for col in range(colen)],
                'end': [
                    (col, colen-1) for col in range(colen)]
                    }
            }


    def get_winner(self):
        for token in self.tokens:
            if self.path(token):
                return token
        return ('')


    def path(self, token):
        start = self.tokens[token]['start']
        end = self.tokens[token]['end']

        queue = start
        been = set()

        while queue:
            x, y = queue.pop()

            if (x, y) in been:
                continue

            been.add((x, y))

            if not (
                0 <= y < len(self.rows) and
                0 <= x < len(self.rows[0])):
                    continue

            if self.rows[y][x] != token:
                    continue

            if (x, y) in end:
                return True

            moves = (
                (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1))

            queue.extend(
                (x+xmove, y+ymove) for xmove, ymove in moves)
