secrets = {
    'wink': 1, 
    'double blink': 2,
    'close your eyes': 4, 
    'jump': 8,
}

def handshake(code):
    actions = []
    
    for action, num in secrets.items():
        if code & num:
            actions.append(action)

    if code & 16:
        actions.reverse()
        
    return actions
        
        
def secret_code(actions):
    total = [secrets[action] for action in actions]
            
    if len(total) > 1 and total[0] > total[1]:
        total.append(16)
        
    return sum(total)
