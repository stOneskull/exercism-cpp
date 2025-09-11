class School:

    def __init__(self, name):
        self.name = name
        self.data = {}

    def add(self, student, year):
        self.data.setdefault(year, []).append(student)

    def grade(self, year):
        return self.data.get(year, ())

    def sort(self):
        years = sorted(list(self.data.keys()))
        return [
            (year, tuple(sorted(self.data[year])))
            for year in years
            ]

