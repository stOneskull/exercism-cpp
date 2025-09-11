class Cipher:
    def __init__(self, key=None):
        self.abc = 'abcdefghijklmnopqrstuvwxyz'
        if key is None:
            self.key = self.setkey()
        elif not key.islower():
            raise ValueError('key must be lowercase')
        else:
            self.key = key

    def setkey(self):
        from random import choice, randint
        return ''.join(
            choice(self.abc)
            for times in range(randint(102, 123)))

    def coder(self, text, shift=1):
        return ''.join(self.abc[
            (self.abc.index(char) +
             shift * self.abc.index(
                 self.key[i % len(self.key)])) % 26]
                       for i, char in enumerate(text))

    def encode(self, text):
        return self.coder(text)

    def decode(self, text):
        return self.coder(text, -1)
