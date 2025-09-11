digits = [
    " _     _  _     _  _  _  _  _ ",
    "| |  | _| _||_||_ |_   ||_||_|",
    "|_|  ||_  _|  | _||_|  ||_| _|",
    "                              ",
]


def junk2book(junk):
    book = {}
    units = len(junk[0]) // 3
    chop = 0

    for unit in range(units):
        book[unit] = [line[chop:chop+3] for line in junk]
        chop += 3

    return book


digitbook = junk2book(digits)


def readbook(book):
    output = ''

    for entry in book:
        for digit, code in digitbook.items():
            if book[entry] == code:
                output += str(digit)
                break
        else:
            output += '?'

    return output


def convert(grid):
    if len(grid) % 4 or any(
        len(line) % 3 for line in grid):
        raise ValueError('incorrect grid size')

    books = []
    ranks = (len(grid) - 4) // 4 + 1
    step = 0

    for rank in range(ranks):
        books.append(junk2book(grid[step:step+4]))
        step += 4

    return ','.join(readbook(book) for book in books)
