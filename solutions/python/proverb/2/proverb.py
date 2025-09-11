def proverb(*words, qualifier=None):
    if not words:
        return []
    lines = []
    word = word1 = words[0]
    length = len(words)
    if length > 1:
        word2 = words[1]
        index = 2
        while index < length:
            lines.append(f"For want of a {word1} the {word2} was lost.")
            word1, word2 = word2, words[index]
            index += 1
        lines.append(f"For want of a {word1} the {word2} was lost.")
    qualifier = '' if not qualifier else qualifier + ' '
    lines.append(f"And all for the want of a {qualifier}{word}.")
    return lines
