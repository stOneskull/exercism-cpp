STATUS_WIN = "escaped"
STATUS_LOSE = "hangman"
STATUS_ONGOING = "goodluck"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guesses = ""
        self.correct = ""
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING


    def guess(self, letter):
        if self.status is not STATUS_ONGOING:
            raise ValueError('game over')
        if letter not in self.guesses:
            self.guesses += letter
        if letter not in self.word or letter in self.correct:
            self.remaining_guesses -= 1
        else:
            self.correct += letter



    def get_masked_word(self):
        masked = ""
        for letter in self.word:
            if letter in self.correct:
                masked += letter
            else:
                masked += "_"
        return masked


    def get_status(self):
        if self.remaining_guesses < 1:
            self.status = STATUS_LOSE
        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        return self.status

