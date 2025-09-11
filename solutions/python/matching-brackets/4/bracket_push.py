brace = {
    '(': ')',
    '[': ']',
    '{': '}',
    }

def is_paired(line):
    chi = []

    for u in line:
        if u in brace:
            chi.append(brace[u])
        elif u in brace.values():
            if not chi or chi.pop() != u:
                return 0

    return chi == []
