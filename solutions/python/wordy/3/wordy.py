def calculate(quest):
    quest = quest[8:-1]

    for oper, words in {
    ('+', 'plus'),
    ('-', 'minus'),
    ('*', 'multiplied by'),
    ('//', 'divided by'),
    }:
        quest = quest.replace(words, oper)

    quest = quest.split()

    if len(quest) % 2 == 0:
        raise ValueError('check yo question')

    try:
        while len(quest) > 1:
            first_op = eval(' '.join(quest[:3]))
            quest = [str(first_op)] + quest[3:]
        return int(quest[0])
    except SyntaxError:
        raise ValueError('check yo question')