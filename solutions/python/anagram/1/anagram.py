def detect_anagrams(word, candidates):

    wordsplit = list(word.lower())
    wordsplit.sort()

    solution = []

    for candy in candidates:
        saute = list(candy.lower())
        saute.sort()
        if saute == wordsplit and word.lower() != candy.lower():
            solution.append(candy)

    return solution