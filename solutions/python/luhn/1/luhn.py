class Luhn:
    def __init__(self, card_num):
        self.num = card_num.replace(' ', '')[::-1]

    def is_valid(self):
        if len(self.num) < 2:
            return False

        digits = []
        for i, digit in enumerate(self.num):
            if not digit.isdigit():
                return False
            digit = int(digit)
            if i % 2:
                digit *= 2
                if digit > 9:
                    digit -= 9
            digits.append(digit)

        return not sum(digits) % 10
