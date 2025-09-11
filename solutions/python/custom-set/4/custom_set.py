class CustomSet:
    def __init__(self, elements=[]):
        self.els = list(dict.fromkeys(elements))

    def isempty(self):
        return not self.els

    def __contains__(self, element):
        return element in self.els

    def issubset(self, other):
        return all(el in other for el in self.els)

    def isdisjoint(self, other):
        return not any(el in other for el in self.els)

    def __eq__(self, other):
        return sorted(self.els) == sorted(other.els)

    def add(self, element):
        if element not in self.els:
            self.els.append(element)

    def intersection(self, other):
        return CustomSet(
        [el for el in self.els if el in other.els]
        )

    def __sub__(self, other):
        return CustomSet(
        [el for el in self.els if el not in other.els]
        )

    def __add__(self, other):
        return CustomSet(self.els + other.els)
