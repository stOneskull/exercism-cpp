def score(word):
    return sum(
        value for letter in word.upper()
        for value, letters in (
            (1, 'AEIOULNRST'), (2, 'DG'),
            (3, 'BCMP'), (4, 'FHVWY'),
            (5, 'K'), (8, 'JX'), (10, 'QZ')
            )
        if letter in letters
        )
