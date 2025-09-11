brace = {
    '(': ')', '[': ']', '{': '}'
    }

def is_paired(line):
    chi = []

    for you in line:
        if you in brace:
            chi.append(brace[you])
        elif you in brace.values():
            if not chi or chi.pop() != you:
                return False

    return chi == []
