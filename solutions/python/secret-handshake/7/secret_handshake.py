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


# def secret_code(actions):
#     total = [secrets[action] for action in actions]

#     if total[0] > total[-1]:
#         total.append(16)

#     return sum(total)
