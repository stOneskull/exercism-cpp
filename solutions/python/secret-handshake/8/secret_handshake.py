secrets = {
    'wink': 1,
    'double blink': 2,
    'close your eyes': 4,
    'jump': 8,
}


def commands(code):
    code = int(code, 2)

    actions = [
        secret for secret, num in secrets.items()
        if code & num
    ]

    if code & 16:
        actions.reverse()

    return actions