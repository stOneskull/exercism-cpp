def egg_count(display_value):
    binary = []
    while display_value:
        display_value, bit = divmod(display_value, 2)
        binary.append(bit)
    return sum(binary)
