def private_key(p):
    from secrets import randbelow
    return randbelow(p-1) + 1


def public_key(p, g, private):
    return g ** private % p


def secret(p, public, private):
    return public ** private % p
