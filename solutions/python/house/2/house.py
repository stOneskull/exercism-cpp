songlines = '''
This is the horse and the hound and the horn
that belonged to the farmer sowing his corn
that kept the rooster that crowed in the morn
that woke the priest all shaven and shorn
that married the man all tattered and torn
that kissed the maiden all forlorn
that milked the cow with the crumpled horn
that tossed the dog
that worried the cat
that killed the rat
that ate the malt
that lay in the house that Jack built.
'''.splitlines()


def recite(start, end):
    return [
        ' '.join(makeverse(verse))
        for verse in range(start, end+1)
    ]


def makeverse(start):
    startline = songlines[-start].split('the', 1)[1]
    rest = [
        songlines[-line] for line in range(start-1, 0, -1)
    ]
    return ['This is the' + startline] + rest