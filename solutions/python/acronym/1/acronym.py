def abbreviate(words):

    filtered = []

    for word in words.split():
        if '-' not in word:
            filtered.append(word)
        else:
            for each in word.split('-'):
                filtered.append(each)

    acro = ''.join(
        word[0].upper() for word in filtered)

    return acro