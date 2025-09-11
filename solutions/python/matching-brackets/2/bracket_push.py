brackets = {'(': ')', '[': ']', '{': '}'}

def is_paired(string):
    stack = []
    for char in string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if(not stack or
            char != brackets[stack.pop()]):
                return 0
    return stack == []
