def encode(numbers):
    encoded = []
    
    for number in numbers:
        encoded += encode_each(number)

    return encoded

        
def encode_each(number):
    if not number: return [0]
    
    bit7run = []

    while number:
        bit7 = number % 128
        if bit7run: bit7 += 128
        bit7run.append(bit7)
        number //= 128

    bit7run.reverse()
    return bit7run


def decode(bit7run):
    if bit7run[-1] // 128 == 1:
        raise ValueError("end byte continuation bit set")

    decoded = []
    tally = 0

    for bit7 in bit7run:
        tally += bit7 % 128
        
        if bit7 < 128:
            decoded.append(tally)
            tally = 0
        else:
            tally *= 128

    return decoded
