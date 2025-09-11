def encode(numbers):
    encoded = []
    
    for number in numbers:
        encoded += encode_each(number)

    return encoded

        
def encode_each(number):
    if not number: return [0]
    
    byte7run = []

    while number:
        byte7 = number % 128
        if byte7run: byte7 += 128
        byte7run.append(byte7)
        number //= 128

    byte7run.reverse()
    
    return byte7run


def decode(byte7run):
    if byte7run[-1] // 128 == 1:
        raise ValueError("end byte continuation bit set")

    decoded = []
    tally = 0

    for byte7 in byte7run:
        tally += byte7 % 128
        
        if byte7 < 128:
            decoded.append(tally)
            tally = 0
        else:
            tally *= 128

    return decoded
