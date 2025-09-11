def alphabet(rev=False):
    if not rev:
        return 'abcdefghijklmnopqrstuvwxyz'
    return 'zyxwvutsrqponmlkjihgfedcba'

def encode(plain_text):
    enc_text = ''.join(
        alphabet('r')[alphabet().index(letter.lower())] if letter.isalpha()
        else letter if letter.isdigit() else ''
        for letter in plain_text
        )

    split_enc_text = ''.join(
        ' ' + letter if i and i % 5 == 0 else letter
        for i, letter in enumerate(enc_text)
        )

    return split_enc_text


def decode(ciphered_text):
    dec_text = ''.join(
        alphabet()[alphabet('r').index(letter)] if letter.isalpha()
        else letter if letter.isdigit() else ''
        for letter in ciphered_text
        )

    return dec_text