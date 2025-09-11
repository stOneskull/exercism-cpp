def make_diamond(letter):
    if letter == 'A': return 'A\n'

    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    addy = alph.index(letter)
    length = addy * 2 + 1
    start = 'A'.center(length) + '\n'

    gap = -1; lines = ''

    for chap in alph[1:addy+1]:
        gap += 2
        line = chap + (' ' * gap) + chap
        lines += line.center(length) + '\n'

    for chap in reversed(alph[1:addy]):
        gap -= 2
        line = chap + (' ' * gap) + chap
        lines += line.center(length) + '\n'

    return start + lines + start

