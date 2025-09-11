def verify(isbn):
    try:
        isbn = list(isbn.replace('-', ''))
        assert len(isbn) == 10
        multiplier = 10
        total = 0
        for num in isbn:
            if multiplier == 1 and num == 'X':  
                num = 10
            total += int(num) * multiplier
            multiplier -= 1
        return total % 11 == 0
    except:
        return False