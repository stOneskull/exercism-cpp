def is_paired(input_string):
    paren, brack, brace = 0, 0, 0

    for char in input_string:
        if char == '(': paren = 'open'
        if char == '[': brack = 'open'
        if char == '{': brace = 'open'

        if char == ')':
            if paren and not brack and not brace: paren -= 1

            else: return 0
        if char == ']':
            if brack and not paren and not brace: brack -= 1
            else: return 0
        if char == '}':
            if brace and not paren and not brace: brace -= 1
            else: return 0

    return paren + brack + brace == 0
