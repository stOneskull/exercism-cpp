class Phone(object):
    def __init__(self, phone_number):
        cleaned = ''.join(
        char for char in phone_number if char.isdigit()
        )
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
            
        self.number = cleaned
        self.area_code = cleaned[:3]
        self.exch = cleaned[3:6]
        self.subscr = cleaned[6:]

    def pretty(self):
        return (
        f'({self.area_code}) {self.exch}-{self.subscr}'
        )
