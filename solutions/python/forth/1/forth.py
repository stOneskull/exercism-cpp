# Froth Forth

from operator import add, sub, mul, floordiv


class StackUnderflowError(Exception):
    pass


class Stack:
    builtins = ['dup', 'drop', 'swap', 'over']
    opers = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv,
    }

    def __init__(self):
        self.stack = []
        self.funcs = {}

    def dup(self):
        self.stack.append(self.stack[-1])

    def drop(self):
        self.stack.pop()

    def swap(self):
        self.stack.append(self.stack.pop(-2))

    def over(self):
        self.stack.append(self.stack[-2])

    def check(self, words):
        word = words[0]
        return (
            words if word not in self.funcs
            else self.funcs[word] + words[1:]
        )

    def makefunc(self, words):
        words = words[1:-1]
        funcname = words.pop(0)
        if funcname[0].isnumeric():
            raise ValueError(
                f'func: {funcname} cannot begin number'
            )
        self.funcs[funcname] = self.check(words)

    def feed(self, words):
        while words:
            words = self.check(words)
            word = words.pop(0)

            if word.isnumeric():
                self.stack.append(int(word))

            elif word in self.builtins:
                try:
                    exec(f'self.{word}()')
                except IndexError:
                    raise StackUnderflowError('oops')

            elif word in self.opers:
                try:
                    self.stack.append(
                        self.opers[word](
                            self.stack.pop(-2),
                            self.stack.pop()
                        )
                    )
                except IndexError:
                    raise StackUnderflowError('oops')
                
            else:
                raise ValueError(f'{word} wrong')


def evaluate(input_data):
    stack = Stack()

    for line in input_data:
        words = line.lower().split()

        if words[0] == ':':
            stack.makefunc(words)
        else:
            stack.feed(words)

    return stack.stack
