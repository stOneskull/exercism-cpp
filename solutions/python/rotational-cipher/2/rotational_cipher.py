def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def check(letter):
        if not letter.isalpha():
            return letter
        index = alphabet.index(letter.lower())
        out_letter = alphabet[(index + key) % 26]
        return(
            out_letter if alphabet[index] == letter
            else out_letter.upper()
            )

    return ''.join(check(letter) for letter in text)

