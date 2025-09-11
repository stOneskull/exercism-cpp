def digithunt(question):
    for char in question:
        if char.isdigit() or char == '-':
            return char


def numsplit(question):
    num = digithunt(question)
    if num is not None:
        spot = question.index(num)
        try:
            question = question[spot+1:]
            while question[0].isdigit():
                num += question[0]
                question = question[1:]
        except IndexError:
            question = ''
    return num, question


def opersplit(question):
    digit = digithunt(question)
    if digit:
        digit = question.index(digit)
    operation = question[:digit]
    operation = operation.strip()
    question = question[digit:]
    operations = {
        '+': 'plus',
        '-': 'minus',
        '*': 'multiplied by',
        '/': 'divided by',
        }
    for oper, words in operations.items():
        if operation == words:
            return oper, question
    raise ValueError('invalid operation')


def calculate(question):
    question = question[:-1]
    nums = []
    operations = []
    while question:
        num, question = numsplit(question)
        nums.append(num)
        if question:
            opr, question = opersplit(question)
            operations.append(opr)
    total = nums.pop(0)
    while nums and operations:
        total = eval(
            str(total) + operations.pop(0) + nums.pop(0)
        )
    return total




