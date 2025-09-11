class Garden:

    seeds = dict(
        G = 'Grass', C = 'Clover',
        R = 'Radishes', V = 'Violets'
        )

    kids = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry',
        ]

    def __init__(self, diagram, students=kids):
        self.row1, self.row2 = diagram.split('\n')
        self.students = students
        self.students.sort()

    def plants(self, student):
        pos = self.students.index(student) * 2
        return [
            Garden.seeds[self.row1[pos]], Garden.seeds[self.row1[pos+1]],
            Garden.seeds[self.row2[pos]], Garden.seeds[self.row2[pos+1]],
            ]