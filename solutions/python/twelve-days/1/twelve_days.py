def recite(start, end):
    verses = 1

    if start != end:
        verses += end - start

    return [verser(start+verse) for verse in range(verses)]


def verser(start):
    dayths = (
        'zeroth first second third fourth fifth sixth '
        'seventh eighth ninth tenth eleventh twelfth'
        )

    dayth = dayths.split()[start]

    song = (
        f'On the {dayth} day of Christmas '
        'my true love gave to me: '
        )

    lines = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, and ",
        "a Partridge in a Pear Tree.",
        ]

    now = start

    while now:
        song += lines[-now]
        now -= 1

    return song
