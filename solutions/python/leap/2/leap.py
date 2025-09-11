def is_leap_year(year):
    return (not year % 4 if year % 100 or not year % 400 else False)