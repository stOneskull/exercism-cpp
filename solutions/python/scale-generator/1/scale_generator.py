class Scale:
    use_sharps = [
        'A', 'B', 'C', 'F#', 'G', 'a', 'f#',
        ]
    sharps = [
        'A', 'A#', 'B', 'C', 'C#', 'D',
        'D#', 'E', 'F', 'F#', 'G', 'G#',
        ]
    flats = [
        'A', 'Bb', 'B', 'C', 'Db', 'D',
        'Eb', 'E', 'F', 'Gb', 'G', 'Ab',
        ]

    def __init__(self, tonic, intervals=None):
        if tonic in Scale.use_sharps:
            tonic = tonic.capitalize()
            if tonic.endswith('b'):
                pos = Scale.flats.index(tonic)
            else:
                pos = Scale.sharps.index(tonic)
            notes = Scale.sharps[pos:] + Scale.sharps[:pos]
        else:
            tonic = tonic.capitalize()
            if tonic.endswith('#'):
                pos = Scale.sharps.index(tonic)
            else:
                pos = Scale.flats.index(tonic)
            notes = Scale.flats[pos:] + Scale.flats[:pos]

        if intervals is None:
            self.pitches = notes
        else:
            self.pitches = [tonic]
            pos = 0
            for interval in intervals[:-1]:
                if interval == 'm':
                    pos += 1
                elif interval == 'M':
                    pos += 2
                else:
                    pos += 3
                pos %= len(notes)
                self.pitches.append(notes[pos])
