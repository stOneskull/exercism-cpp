def abbreviate(words):
    filtered = []

    for word in words.split():
        word = word.replace('_', '')
        for each in word.split('-'):
            if each: filtered.append(each)

    return ''.join(
        word[0].upper() for word in filtered
        )