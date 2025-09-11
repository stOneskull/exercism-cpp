def encode(message, rails):
    thechain = railchain(rails)
    therails = ['' for each in range(rails)]
    for letter in message:
        therails[next(thechain)] += letter
    return ''.join(therails)

    
def decode(message, rails):
    thechain = railchain(rails)
    derail = {rail: [] for rail in range(rails)}
    for pos in range(len(message)):
        derail[next(thechain)].append(pos)
    poslist = []
    for eachlist in derail.values():
        poslist += eachlist
    decoded = sorted(zip(poslist, message))
    return ''.join(tup[1] for tup in decoded)
    

def railchain(rails):
    from itertools import chain, cycle
    return cycle(
        chain(range(rails), range(rails-2, 0, -1))
        )
