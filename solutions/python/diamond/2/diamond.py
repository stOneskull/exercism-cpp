alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_diamond(letter):
    if letter == 'A': return 'A\n'

    addy = alph.index(letter)
    length = addy * 2 + 1
    start = 'A'.center(length) + '\n'

    gap = -1; lines = ''

    for each in alph[1:addy+1]:
        gap += 2
        line = each + (' ' * gap) + each
        lines += line.center(length) + '\n'

    for each in reversed(alph[1:addy]):
        gap -= 2
        line = each + (' ' * gap) + each
        lines += line.center(length) + '\n'

    return start + lines + start

