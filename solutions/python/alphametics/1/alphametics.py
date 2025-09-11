def solve(puzzle):
    from itertools import permutations

    letters = set(letter for letter in puzzle if letter.isalpha())

    for combo in permutations(range(10), len(letters)):
        expression = puzzle

        for letter, num in zip(letters, combo):
            expression = expression.replace(letter, str(num))

        if any(word.startswith('0') for word in expression.split()):
            continue

        if eval(expression):
            return dict(zip(letters, combo))

    return {}
