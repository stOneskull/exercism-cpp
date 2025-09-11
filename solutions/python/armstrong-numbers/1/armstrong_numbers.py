def is_armstrong(number):
    digits = list(str(number))
    total = sum(int(digit) ** len(digits) for digit in digits)
    return int(number) == total