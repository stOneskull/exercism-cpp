class MeetupDayException(BaseException):
    def __init__(self, *msg):
        print('\nError\n', msg, '\n')


def meetup_day(year, month, dotw, which):

    from calendar import monthrange
    from datetime import date
    from time import strptime

    try:
        day = strptime(dotw, '%A').tm_wday
    except:
        raise MeetupDayException(
            dotw, 'not a day of the week', year, month, which, dotw)

    firstday, days = monthrange(year, month)
    ourfirstday = (day - firstday) % 7 + 1
    daylist = [each for each in range(ourfirstday, days + 1, 7)]
    teenths = range(13, 20)

    posi = {
        '1st': 0,
        '2nd': 1,
        '3rd': 2,
        '4th': 3,
        '5th': 4,
        'last': -1,
        }

    if 'teenth' in which:
        for num in daylist:
            if num in teenths:
                day_num = num
    else:
        try:
            day_num = daylist[posi[which]]
        except Exception as e:
            raise MeetupDayException(
                e, year, month, which, dotw
            )

    return date(year, month, day_num)

if __name__ == '__main__':
    import random
    year = random.choice(range(-999, 11000))
    month = random.choice(range(-2, 15))
    day = random.choice(
        ['Eggday', 'Saturday', 1, 'monday', 'tuesday', 'tue', 'tues'])
    posi = random.choice(['1st', 'teenth', '5th', 'last', '6th', 4, 7, '7'])

    try:
        testdate = meetup_day(year, month, day, posi)
    except Exception as e:
        raise MeetupDayException(e, year, month, day, posi)

    print(testdate)