def recite(start=99, take=1):
    def respond(start):
        if start > 99:
            raise ValueError("too many bottles")
        if start >= 3:
            reply = [
            '{0} bottles of beer on the wall, {0} bottles of beer.'.format(str(start)),
            'Take one down and pass it around, {0} bottles of beer on the wall.'.format(str(start-1))
            ]
        if start == 2:
            reply = [
            '2 bottles of beer on the wall, 2 bottles of beer.',
            'Take one down and pass it around, 1 bottle of beer on the wall.'
            ]
        if start == 1:
            reply = [
                "1 bottle of beer on the wall, 1 bottle of beer.",
                (
                    "Take it down and pass it around, "
                    "no more bottles of beer on the wall."
                )
            ]
        if not start:
            reply = [
                "No more bottles of beer on the wall, no more bottles of beer.",
                (
                    "Go to the store and buy some more, "
                    "99 bottles of beer on the wall."
                )
            ]
        return reply

    answer = []
    for each in range(take):
        answer += respond(start)
        start -= 1
        if start < 0: start = 99
    return answer

