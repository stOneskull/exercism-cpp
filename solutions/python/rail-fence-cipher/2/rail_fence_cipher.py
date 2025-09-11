def encode(message, rails):
    thechain = railchain(rails)
    railway = ['' for each in range(rails)]
    for letter in message:
        railway[next(thechain)] += letter
    return ''.join(railway)

    
def decode(message, rails):
    thechain = railchain(rails)
    railway = {rail: [] for rail in range(rails)}
    for pos in range(len(message)):
        railway[next(thechain)].append(pos)
    poslist = []
    for eachlist in railway.values():
        poslist += eachlist
    decoded = sorted(zip(poslist, message))
    return ''.join(tup[1] for tup in decoded)
    

def railchain(rails):
    from itertools import chain, cycle
    return cycle(
        chain(range(rails), range(rails-2, 0, -1))
        )
