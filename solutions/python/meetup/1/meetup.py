def MeetupDayException(err, msg):
    print(err, msg)

def meetup_day(year, month, day_of_the_week, which):

    from calendar import monthrange
    from datetime import date
    from time import strptime

    day = strptime(day_of_the_week, '%A').tm_wday

    firstday, days = monthrange(year, month)

    ourfirstday = (day - firstday) % 7 + 1

    daylist = [each for each in range(ourfirstday, days + 1, 7)]

    print(daylist)

    teenths = range(13, 20)

    posi = {
        '1st': 0,
        '2nd': 1,
        '3rd': 2,
        '4th': 3,
        '5th': 4,
        'last': -1,
        }

    try:
        if 'teenth' in which:
            for num in daylist:
                if num in teenths:
                    day_num = num
        elif posi[which] + 1 > len(daylist):
            print('hvjhvkhvkhvkhvkhgkhg')
            raise ValueError('no such day posi')
        else:
            day_num = daylist[posi[which]]
    except ValueError:
        MeetupDayException(ValueError, 'no such day posi')

    return date(year, month, day_num)