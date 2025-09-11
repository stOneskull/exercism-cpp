def is_leap_year(year):
    if not year % 4:
        if not year % 400 or year % 100:
            return True  
    return False