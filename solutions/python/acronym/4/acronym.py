def abbreviate(words):
    return ''.join(
        word[0].upper() for word in
        words.replace('_','').replace('-',' ').split()
        )
