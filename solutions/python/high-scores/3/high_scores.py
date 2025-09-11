class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        hi, lates = self.highest(), self.latest()
        a = "Your latest score was {}. That's ".format(
            lates)
        if lates < hi:
            a += "{} short of ".format(hi-lates)
        z = "your personal best!"
        return a + z

