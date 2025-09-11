def is_isogram(string):
    entry = string.lower()
    for letter in entry:
        c = entry.count(letter)
        if c > 1 and letter not in " _-":
            return False
    return True