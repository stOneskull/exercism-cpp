class Allergies:

    def __init__(self, score):
        self.score = score % 256

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):

        allergies = {
            1:'eggs',
            2:'peanuts',
            4:'shellfish',
            8:'strawberries',
            16:'tomatoes',
            32:'chocolate',
            64:'pollen',
            128:'cats',
            }

        vals = [128, 64, 32, 16, 8, 4, 2, 1]

        allergy_list = []

        tal = self.score

        for val in vals:
            if tal - val >= 0:
                allergy_list.append(allergies[val])
                tal -= val

        return allergy_list