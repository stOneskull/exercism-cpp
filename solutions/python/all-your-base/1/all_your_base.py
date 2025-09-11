def rebase(inbase, digitlist, outbase):
    if inbase < 2 or outbase < 2:
        raise ValueError('the lowest base is 2')
    if any(
        digit not in range(inbase)
        for digit in digitlist):
            raise ValueError('invalid digit in list')

    digitlist.reverse()
    digits = []
    num = 0

    for power, digit in enumerate(digitlist):
        num += digit * inbase ** power

    while num:
        digit = num % outbase
        num = num // outbase
        digits.append(digit)

    digits.reverse()
    return digits