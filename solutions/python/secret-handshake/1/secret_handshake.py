def handshake(code):
    actions = []
    rev = 1
    if code - 16 >= 0:
        code -= 16
        rev = 0
    if code - 8 >= 0:
        code -= 8
        actions.append('jump')
    if code - 4 >= 0:
        code -= 4
        actions.append('close your eyes')
    if code - 2 >= 0:
        code -= 2
        actions.append('double blink')
    if code - 1 >= 0:
        code -= 1
        actions.append('wink')
    if rev:
        actions = list(reversed(actions))
    return actions
        
        
def secret_code(actions):
    total = []
    secrets = {'wink': 1, 'double blink': 2,
               'close your eyes': 4, 'jump': 8}
    
    for action in actions:
        if action in secrets:
            total.append(secrets[action])
    if len(total) > 1 and total[0] > total[1]:
        total.append(16)
    return sum(total)
