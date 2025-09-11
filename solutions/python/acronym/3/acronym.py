def abbreviate(words):
    return ''.join(
            each.replace('_', '')[0].upper()
            for word in words.split()
            for each in word.split('-')
            if each
            )
