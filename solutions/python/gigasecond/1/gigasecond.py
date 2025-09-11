def add_gigasecond(birth_date):
    from datetime import timedelta
    return birth_date + timedelta(seconds=10**9)