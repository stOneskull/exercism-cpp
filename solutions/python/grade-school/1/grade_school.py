class School:

    def __init__(self, name):
        self.name = name
        self.data = {}

    def add(self, student, grade_num):
        if grade_num not in self.data:
            self.data[grade_num] = [student]
        else:
            self.data[grade_num].append(student)

    def grade(self, grade_num):
        if grade_num in self.data:
            return self.data[grade_num]
        return ()

    def sort(self):
        keys = list(self.data.keys())
        keys.sort()
        sorted_school = []
        for key in keys:
            sorted_school.append(
                (key, tuple(sorted(self.data[key]))))
        return sorted_school