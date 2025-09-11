class CustomSet:
    def __init__(self, elements=[]):
        self.els = list(dict.fromkeys(elements))

    def isempty(self):
        return not self.els

    def __contains__(self, element):
        return element in self.els

    def issubset(self, other):
        return all(x in other for x in self.els)

    def isdisjoint(self, other):
        return not any(x in other for x in self.els)

    def __eq__(self, other):
        return sorted(self.els) == sorted(other.els)

    def add(self, element):
        if element not in self.els:
            self.els.append(element)

    def intersection(self, other):
        return CustomSet(
            [e for e in self.els if e in other.els]
        )

    def __sub__(self, other):
        return CustomSet(
            [e for e in self.els if e not in other.els]
        )

    def __add__(self, other):
        return CustomSet(self.els + other.els)
