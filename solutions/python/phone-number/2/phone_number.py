class Phone(object):
    def __init__(self, phone_number):
        self.number = self.clean(phone_number)
        self.area_code = self.number[:3]

    @staticmethod
    def clean(number):
        cleaned = ''.join(
            ch for ch in number if ch.isdigit())
        if len(cleaned) == 11:
            if cleaned[0] != '1':
                raise ValueError('check country code')
            cleaned = cleaned[1:]
        if len(cleaned) != 10:
            raise ValueError('check digit length')
        if cleaned[0] in '01':
            raise ValueError('check exchange code')
        if cleaned[3] in '01':
            raise ValueError('check subscriber code')
        return cleaned

    def pretty(self):
        area = self.number[:3]
        exch = self.number[3:6]
        subs = self.number[6:]
        return f'({area}) {exch}-{subs}'
