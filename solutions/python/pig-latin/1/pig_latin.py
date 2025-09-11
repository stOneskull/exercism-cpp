def translate(text):

    text = text.split()
    words = []
    vowels = 'aeiou'

    for word in text:
        if word[0] in vowels or word[0:2] in ['xr', 'yt']:
            pass
        elif word[0] not in vowels and word[1:3] == 'qu':
            word = word[3:] + word[:3]
        elif word.startswith('qu'):
            word = word[2:] + 'qu'
        elif len(word) == 2 and word[1] == 'y':
            word = word[::-1]
        elif word.startswith('y'):
            word = word[1:] + 'y'
        else:
            for letter in word:
                if letter in vowels or letter == 'y':
                    v = word.index(letter)
                    word = word[v:] + word[:v]
                    break

        word += 'ay'

        words.append(word)

    return ' '.join(words)
