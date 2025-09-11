def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]


# class HighScores:
    # def __init__(self, scores):
        # self.scores = scores

    # def latest(self):
        # return self.scores[-1]

    # def personal_best(self):
        # return max(self.scores)

    # def personal_top_three(self):
        # return sorted(self.scores, reverse=True)[:3]

    # def report(self):
        # hi, lates = self.personal_best(), self.latest()
        # a = f"Your latest score was {lates}. That's "
        # if lates < hi:
            # a += f"{hi-lates} short of "
        # b = "your personal best!"
        # return a + b

