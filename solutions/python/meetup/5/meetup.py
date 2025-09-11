class MeetupDayException(BaseException):
    pass


def meetup_day(year, month, dotw, which):
    from time import strptime
    from calendar import monthrange
    from datetime import date

    try:
        # get day as a number, monday is 0, sunday 6
        day = strptime(
            dotw, '%A').tm_wday
    except ValueError:
        raise MeetupDayException(
            f'{dotw} not a day of the week')

    firstday, days = monthrange(year, month)
    # get first dotw in the month
    ourfirstday = (day - firstday) % 7 + 1
    # in range of month days, count by 7 after our first
    daylist = [
        each for each in range(ourfirstday, days + 1, 7)
        ]
    teenths = range(13, 20)

    posi = {
        '1st': 0, '2nd': 1, '3rd': 2,
        '4th': 3, '5th': 4, 'last': -1,
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
