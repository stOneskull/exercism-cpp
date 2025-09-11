class School:
    def __init__(self):
        self.data = {}

    def add_student(self, name, grade):
        self.data.setdefault(grade, []).append(name)

    def grade(self, grade):
        return sorted(self.data.get(grade, []))

    def roster(self):
        return [
            name for grade in sorted(self.data.keys())
            for name in sorted(self.data[grade])
            ]

