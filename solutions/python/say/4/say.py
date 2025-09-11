chunks = {
1: 'thousand', 2: 'million', 3: 'billion'
}

tens = {
0: '', 1: 'ten', 2: 'twenty', 3: 'thirty',
4: 'forty', 5: 'fifty', 6: 'sixty',
7: 'seventy', 8: 'eighty', 9: 'ninety',
}

units = {
0: 'zero', 1: 'one', 2: 'two', 3: 'three',
4: 'four', 5: 'five', 6: 'six', 7: 'seven',
8: 'eight', 9: 'nine', 10: 'ten',
11: 'eleven', 12: 'twelve', 13: 'thirteen',
14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
}


def check_units(number):
    if number % 10 == 0: 
        return ''
    return '-' + units[number % 10] 

def check_tens(number):
    if number % 100 == 0: 
        return ''
    return ' ' + tens[(number % 100) // 10]


def check_chunk(number):
    if number < 20: 
        return units[number]

    if number < 100:
        return (
        tens[number // 10] + check_units(number)
        )

    text = units[number // 100] + ' hundred'
    text += check_tens(number)
    text += check_units(number)
    return text


def say(number):
    if number < 0:
        raise ValueError(
        "we don't like negatives round here"
        ) 
    if number >= 1e12:
        raise ValueError("take it outside")
        
    if number < 1000:
        return check_chunk(number)
        
    numstring = str(number)
    thousands = []

    while len(numstring) > 3:
        thousands.append(numstring[-3:])
        numstring = numstring[:-3]

    num = int(numstring)
    words = []

    while True:
        if num:
            words.append(check_chunk(num))
        if not thousands:
            break
        if num:
            words.append(chunks[len(thousands)])
        num = int(thousands.pop())

    return ' '.join(words)




    
    
