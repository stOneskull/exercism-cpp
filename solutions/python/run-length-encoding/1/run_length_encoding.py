def encode(string):
    encoded = ''
    char = ''
    mem_char = ''
    count = 0
    for char in string:
        if char != mem_char:
            if count == 0:
                mem_char = char
                count = 1
            elif count == 1:
                encoded += mem_char
                mem_char = char
            else:
                encoded += str(count) + mem_char
                mem_char = char
                count = 1
        else:
            count += 1
    if count > 1: encoded += str(count) + char
    else: encoded += char
    return encoded
            
            
def decode(string):
    decoded = ''
    int_string = ''
    for char in string:
        if (char.isalpha() or char.isspace()) and not int_string:
            decoded += char
        elif char.isalpha() or char.isspace():
            decoded += int(int_string) * char
            int_string = ''
        else:
            int_string += char
    return decoded