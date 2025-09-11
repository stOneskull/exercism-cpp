def encode(string):
    char, mem = '', ''
    encoded = ''

    count = 0

    for char in string:
        if char == mem:
            count += 1
        elif count == 0:
            mem = char
            count = 1
        elif count == 1:
            encoded += mem
            mem = char
        else:
            encoded += str(count) + mem
            mem = char
            count = 1

    if count > 1:
        encoded += str(count) + char
    else:
        encoded += char

    return encoded


def decode(string):
    mem = ''
    decoded = ''

    for char in string:
        if char.isalpha() or char.isspace():
            if mem == '':
                decoded += char
            else:
                decoded += int(mem) * char
                mem = ''
        else:
            mem += char

    return decoded
