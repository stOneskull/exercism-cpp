class School:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        self.grades.setdefault(grade, []).append(name)

    def grade(self, grade):
        return sorted(self.grades.get(grade, []))

    def roster(self):
        return [
            name for grade in sorted(self.grades.keys())
            for name in sorted(self.grades[grade])
            ]

