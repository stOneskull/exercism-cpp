def alphabet(rev=False):
    if rev:
        return 'zyxwvutsrqponmlkjihgfedcba'
    return 'abcdefghijklmnopqrstuvwxyz'


def encode(plain_text):
    enc_text = ''.join(
        alphabet()[alphabet('r').index(letter.lower())]
        if letter.isalpha()
        else letter if letter.isdigit() else ''
        for letter in plain_text
        )
    return ''.join(
        ' ' + letter if i and i % 5 == 0 else letter
        for i, letter in enumerate(enc_text)
        )


def decode(ciphered_text):
    return ''.join(
        alphabet('r')[alphabet().index(letter)]
        if letter.isalpha()
        else letter if letter.isdigit() else ''
        for letter in ciphered_text
        )
