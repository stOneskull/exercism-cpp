def calculate(quest):
    quest = quest[8:-1]

    for oper, words in {
    ('+', 'plus'),
    ('-', 'minus'),
    ('*', 'multiplied by'),
    ('/', 'divided by'),
    }:
        quest = quest.replace(words, oper)

    quest = quest.split()

    try:
        while len(quest) > 1:
            first_op = eval(' '.join(quest[:3]))
            quest = [str(first_op)] + quest[3:]
        return int(float(quest[0]))
    except:
        raise ValueError('check yo question')