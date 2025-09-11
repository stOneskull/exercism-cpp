def recite(start, end):
    verses = 1

    if start != end:
        verses += end - start

    return [
        makeverse(start+verse)
            for verse in range(verses)
        ]


def makeverse(day):
    dayths = (
        'zeroth first second third fourth fifth sixth '
        'seventh eighth ninth tenth eleventh twelfth'
        )

    dayth = dayths.split()[day]

    verse = (
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

    while day:
        verse += lines[-day]
        day -= 1

    return verse
