braces = {
    '(': ')',
    '[': ']',
    '{': '}',
    }

def is_paired(line):
    box = []

    for bib in line:
        if bib in braces:
            box.append(braces[bib])
        elif bib in braces.values():
            if not box or bib != box.pop():
                return False

    return box == []
