def say(number):

    if number < 0:
        raise ValueError("we don't like negatives around here")
    if number >= 1e12:
        raise ValueError("take it outside")

    thousands = []
    numstring = str(int(number))

    while len(numstring) > 3:
        thousands.append(numstring[-3:])
        numstring = numstring[:-3]

    chunks = {1: 'thousand', 2: 'million', 3: 'billion'}

    units = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three',
        4: 'four', 5: 'five', 6: 'six', 7: 'seven',
        8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
        }

    tens = {
        0: '', 1: 'ten', 2: 'twenty', 3: 'thirty',
        4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety',
        }


    def checklow(number):

        if number < 20:
            return units[number]

        if number < 100:
            text = tens[number // 10]
            text += check_units(number)
            return text

        if number < 1000:
            text = units[number // 100] + ' hundred'
            text += check_tens(number)
            text += check_units(number)
            return text


    def check_units(number):
        if number % 10:
            return '-' + units[number % 10]
        return ''


    def check_tens(number):
        if number % 100:
            return ' and ' + tens[(number % 100) // 10]
        return ''


    def wonderwall():
        nonlocal numstring

        if number < 1000:
            return checklow(number)

        words = []

        num = int(numstring)

        while True:
            if num:
                if not thousands and num < 100:
                    words.append('and')
                words.append(checklow(num))
            if not thousands:
                break
            if num:
                words.append(chunks[len(thousands)])
            num = int(thousands.pop())

        return ' '.join(words)

    return wonderwall()