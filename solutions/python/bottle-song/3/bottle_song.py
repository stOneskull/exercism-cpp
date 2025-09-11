numbers = dict(enumerate(
    ['One', 'Two', 'Three', 'Four', 'Five', 
    'Six', 'Seven', 'Eight', 'Nine', 'Ten'], start=1))


def verses(verse_num):
    lines = [
        f"{numbers[verse_num]} green {'bottle' if verse_num==1 else 'bottles'} hanging on the wall,"
        ] * 2

    lines += [
        'And if one green bottle should accidentally fall,'
        ]

    lines += [
        f"There'll be {'no' if verse_num==1 else numbers[verse_num-1].lower()} green {'bottle' if verse_num==2 else 'bottles'} hanging on the wall."
        ]

    return lines


def recite(start, take=1):
    song = []
    for verse in range(take):
        song += verses(start)
        song.append('')
        start -= 1
    
    song.pop()
    return song
