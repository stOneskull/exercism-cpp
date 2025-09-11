class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def highest(self):
        return max(self.scores)

    def top(self):
        t = []
        s = self.scores
        slen = len(s)
        if slen > 3: slen = 3
        for tops in range(slen):
            i = s.index(max(s))
            t.append(s.pop(i))
        return t

    def report(self):
        lates = self.latest()
        hi = self.highest()
        a = "Your latest score was {}. That's ".format(lates)
        z = "your personal best!"
        if lates < hi:
            a += "{} short of ".format(hi-lates)
        return a + z

