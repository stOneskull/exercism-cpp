STATUS_WIN = "escaped"
STATUS_LOSE = "hangman"
STATUS_ONGOING = "goodluck"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING


    def guess(self, letter):
        if self.status != STATUS_ONGOING:
            raise ValueError('game over')
            
        if (
        letter in self.word
        and letter not in self.guesses
        ):
            self.guesses.append(letter)
        else:
            self.remaining_guesses -= 1

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
            
        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN

        
    def get_masked_word(self):
        masked = ""
        for letter in self.word:
            if letter in self.guesses:
                masked += letter
            else:
                masked += "_"
        return masked


    def get_status(self):
        return self.status

