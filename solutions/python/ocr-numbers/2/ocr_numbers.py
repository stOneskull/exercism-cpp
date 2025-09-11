OCR = [
    " _     _  _     _  _  _  _  _ ",
    "| |  | _| _||_||_ |_   ||_||_|",
    "|_|  ||_  _|  | _||_|  ||_| _|",
    "                              ",
]

OCRdict = {}
cut = 0
for num in range(10):
    OCRdict[num] = []
    for line in OCR:
        OCRdict[num].append(line[cut:cut+3])
    cut += 3


def convert(grid):
    if len(grid) % 4 or any(
        len(line) % 3 for line in grid):
        raise ValueError('incorrect grid size')

    commas = 0
    length = len(grid)

    if length > 4:
        commas = True
        times = (length - 4) // 4
        chop = 4
        for time in range(times):
            for line in range(4):
                grid[line] += grid[chop]
                chop += 1

    grid = grid[:4]

    toread = {}
    cut = 0
    chars = len(grid[0]) // 3

    for char in range(chars):
        toread[char] = []
        for line in grid:
            toread[char].append(line[cut:cut+3])
        cut += 3

    output = ''

    for junk in toread.values():
        if not any(
            junk == code for code in OCRdict.values()
            ):
            output += '?'
        else:
            for digit, code in OCRdict.items():
                if junk == code:
                    output += str(digit)

    if commas:
        numput = int(output)
        if numput >= 1000000000:
            output = output[:-9] + ',' + output[-9:]
        if numput >= 1000000:
            output = output[:-6] + ',' + output[-6:]
        if numput >= 1000:
            output = output[:-3] + ',' + output[-3:]

    return output
