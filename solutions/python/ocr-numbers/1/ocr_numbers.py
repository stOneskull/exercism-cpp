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


def convert(input_grid):
    if len(input_grid) % 4 or any(
        len(line) % 3 for line in input_grid):
        raise ValueError('incorrect grid size')

    commas = 0
    length = len(input_grid)

    if length > 4:
        commas = True
        times = (length - 4) // 4
        chop = 4
        for time in range(times):
            for line in range(4):
                input_grid[line] += input_grid[chop]
                chop += 1

    input_grid = input_grid[:4]

    toread = {}
    cut = 0
    num_chars = len(input_grid[0]) // 3

    for char in range(num_chars):
        toread[char] = []
        for line in input_grid:
            toread[char].append(line[cut:cut+3])
        cut += 3

    output = ''

    for val in toread.values():
        if not any(v == val for v in OCRdict.values()):
            output += '?'
        else:
            for k, v in OCRdict.items():
                if v == val:
                    output += str(k)

    if commas:
        try:
            numput = int(output)
            if numput >= 1000000000:
                output = output[:-9] + ',' + output[-9:]
            if numput >= 1000000:
                output = output[:-6] + ',' + output[-6:]
            if numput >= 1000:
                output = output[:-3] + ',' + output[-3:]
        except:
            pass

    return output


if __name__ == '__main__':
    for key in OCRdict:
        print(key)
        for line in OCRdict[key]:
            print(line)