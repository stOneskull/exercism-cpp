def rotate(text, key):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    out_text = ''

    for letter in text:
        if letter.isalpha():
            index = alphabet.index(letter.lower())
            out_index = (index + key) % 26
            out_letter = alphabet[out_index]
            if alphabet[index] != letter:
                out_letter = out_letter.upper()
        else: out_letter = letter

        out_text += out_letter

    return out_text