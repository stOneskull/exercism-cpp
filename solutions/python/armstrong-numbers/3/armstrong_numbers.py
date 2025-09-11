def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)

    return number == sum(
        int(digit) ** power for digit in digits
    )
