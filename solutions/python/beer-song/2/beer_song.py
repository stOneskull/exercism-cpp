def recite(start, take=1):


    def verse(bottles):

        if bottles >= 3:
            reply = [
            "{0} bottles of beer on the wall, {0} bottles of beer.".format(start),
            ("Take one down and pass it around, "
            "{} bottles of beer on the wall.".format(start - 1))
            ]

        elif bottles == 2:
            reply = [
            "2 bottles of beer on the wall, 2 bottles of beer.",
            ("Take one down and pass it around, "
            "1 bottle of beer on the wall.")
            ]

        elif bottles == 1:
            reply = [
            "1 bottle of beer on the wall, 1 bottle of beer.",
            ("Take it down and pass it around, "
            "no more bottles of beer on the wall.")
            ]

        else:
            reply = [
            "No more bottles of beer on the wall, no more bottles of beer.",
            ("Go to the store and buy some more, "
            "99 bottles of beer on the wall.")
            ]

        return reply


    song = []

    if take > 1:
        for takes in range(take - 1):
            song += verse(start)
            song.append("")
            start -= 1
            if start < 0: start = 99

    song += verse(start)

    return song

