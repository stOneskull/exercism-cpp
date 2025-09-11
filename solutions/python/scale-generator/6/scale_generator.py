class Scale:
    use_sharps = ['A', 'B', 'C', 'F#', 'G', 'a', 'f#']
    sharps = [
        'A', 'A#', 'B', 'C', 'C#', 'D',
        'D#', 'E', 'F', 'F#', 'G', 'G#',
        ]
    flats = [
        'A', 'Bb', 'B', 'C', 'Db', 'D',
        'Eb', 'E', 'F', 'Gb', 'G', 'Ab',
        ]
    skips = {'A': 3, 'M': 2, 'm': 1}

    def __init__(self, tonic, interval=None):
        if tonic in self.use_sharps:
            tonic = tonic.capitalize()
            if tonic.endswith('b'):
                pos = self.flats.index(tonic)
            else:
                pos = self.sharps.index(tonic)
            notes = self.sharps[pos:] + self.sharps[:pos]
        else:
            tonic = tonic.capitalize()
            if tonic.endswith('#'):
                pos = self.sharps.index(tonic)
            else:
                pos = self.flats.index(tonic)
            notes = self.flats[pos:] + self.flats[:pos]
        self.tonic = tonic
        self.notes = notes

    def chromatic(self):
        return self.notes

    def interval(self, intervals):
        notes = [self.tonic]
        pos = 0
        for interval in intervals:
            pos += self.skips[interval]
            notes.append(self.notes[pos%12])
        return notes[:-1]
