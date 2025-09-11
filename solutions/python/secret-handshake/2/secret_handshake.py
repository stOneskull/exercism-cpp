def handshake(code):
    actions = []
    
    if code & 1:
        actions.append('wink')
    if code & 2:
        actions.append('double blink')
    if code & 4:
        actions.append('close your eyes')
    if code & 8:
        actions.append('jump')
    if code & 16:
        actions.reverse()
        
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
