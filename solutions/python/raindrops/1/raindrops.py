def raindrops(num):
    sound = ''
    
    if not num % 3:
        sound += 'Pling'
    if not num % 5:
        sound += 'Plang'
    if not num % 7:
        sound += 'Plong'
        
    if not sound:
        return str(num)
        
    return sound
