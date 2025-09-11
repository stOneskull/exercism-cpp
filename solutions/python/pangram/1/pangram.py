def is_pangram(sentence):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in sentence.lower():
            return False
    return True