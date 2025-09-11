alphabet = "abcdefghijklmnopqrstuvwxyz"


def is_coprime(x, y=26):
    while x:
        y, x = x, y % x
    return y == 1


def mmi(x, y=26):
        m = 1
        while m * x % y != 1:
            m += 1
        return m


def encode(plain_text, a, b):
    if not is_coprime(a):
        raise ValueError(a, 'not valid')

    check = "".join(
        char for char in plain_text.lower()
        if char.isalnum()
    )

    encoded = ""

    for i, char in enumerate(check):
        encoded += (
        alphabet[(a * alphabet.index(char) + b) % 26]
        if char.isalpha() else char
        )

        if (i+1) % 5 == 0:
            encoded += " "

    return encoded.strip()


def decode(ciphered_text, a, b):
    decoded = ""

    for char in ciphered_text:
        if char.isspace():
            continue
        if not char.isalpha():
            decoded += char
            continue

        i = alphabet.index(char)
        o = mmi(a) * (i - b) % 26

        decoded += alphabet[o]

    return decoded
