numbers = dict(enumerate(
    ['One', 'Two', 'Three', 'Four', 'Five', 
    'Six', 'Seven', 'Eight', 'Nine', 'Ten'], start=1))


def verses(verse):
    lines = [
        f"{numbers[verse]} green {'bottle' if verse==1 else 'bottles'}"
        " hanging on the wall,"
        ] * 2

    lines += [
        'And if one green bottle should accidentally fall,'
        ]

    lines += [
        f"There'll be {'no' if verse==1 else numbers[verse-1].lower()}"
        f" green {'bottle' if verse==2 else 'bottles'} hanging on the wall."
        ]

    return lines


def recite(start, take=1):
    song = []
    for _ in range(take):
        song += verses(start)
        song.append('')
        start -= 1
    
    song.pop()
    return song
