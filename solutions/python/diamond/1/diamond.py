alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_diamond(letter):
    if letter == 'A': return 'A\n'

    width = alph.index(letter)
    length = width * 2 + 1

    start = 'A'.center(length) + '\n'
    lines = ''
    gap = -1
    for each in alph[1:width+1]:
        gap += 2
        lines += shape(each, length, gap)
    for each in reversed(alph[1:width]):
        gap -= 2
        lines += shape(each, length, gap)
    return start + lines + start


def shape(each, length, gap):
    shape = each + (' ' * gap) + each
    return shape.center(length) + '\n'

