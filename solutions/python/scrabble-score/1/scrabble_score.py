def score(word):
    scores = {
        1: 'AEIOULNRST',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ',
        }
    total = 0
    for letter in word.upper():
        for value, letters in scores.items():
            if letter in letters:
                total += value
    return total
