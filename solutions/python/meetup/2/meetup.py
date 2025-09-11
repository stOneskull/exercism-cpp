class MeetupDayException(Exception):
    pass

def meetup_day(year, month, day_of_the_week, which):

    from calendar import monthrange
    from datetime import date
    from time import strptime

    day = strptime(day_of_the_week, '%A').tm_wday

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
        except IndexError:
            raise MeetupDayException('no such day posi')

    return date(year, month, day_num)