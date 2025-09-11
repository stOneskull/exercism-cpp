def detect_anagrams(word, candidates):

    return [
        candy for candy in candidates
        if candy.lower() != word.lower()
        and sorted(candy.lower()) == sorted(word.lower())
        ]