def rebase(inbase, digitlist, outbase):
    if inbase < 2:
        raise ValueError('input base must be >= 2')
    if outbase < 2:
        raise ValueError('output base must be >= 2')
    if any(digit not in range(inbase) for digit in digitlist):
            raise ValueError(
                'all digits must satisfy 0 <= d < input base'
                )

    digitlist.reverse()

    digits = []
    
    num = sum(
         digit * inbase ** power 
         for power, digit in enumerate(digitlist)
         )
    
    while num:
        num, digit = divmod(num, outbase)
        digits.append(digit)

    digits.reverse()

    return digits or [0]