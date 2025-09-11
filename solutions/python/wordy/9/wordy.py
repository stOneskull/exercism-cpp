def answer(quest):
    quest = quest.lstrip('What is').rstrip('?')

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
            op = eval(' '.join(quest[:3]))
            quest = [str(op)] + quest[3:]
        return float(quest.pop())
    except:
        raise ValueError('check yo question')
