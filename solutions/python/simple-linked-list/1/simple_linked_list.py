class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        self.val = value

    def value(self):
        return self.val

    def next(self):
        return self.mum


class LinkedList:
    def __init__(self, values=[]):
        self.mum = None
        for value in values:
            self.push(value)

    def __len__(self):
        node = self.mum
        count = 0
        while node:
            count += 1
            node = node.next()
        return count

    def __iter__(self):
        node = self.mum
        while node:
            yield node.val
            node = node.next()

    def head(self):
        if not self.mum:
            raise EmptyListException('no head')
        return self.mum

    def push(self, value):
        node = Node(value)
        node.mum = self.mum
        self.mum = node

    def pop(self):
        if not self.mum:
            raise EmptyListException('nothing to pop')
        pop = self.mum.val
        self.mum = self.mum.next()
        return pop

    def reversed(self):
        return [node for node in self][::-1]
