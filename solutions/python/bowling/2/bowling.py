class BowlingGame:
    def __init__(self):
        self.frames = {}
        self.frame, self.framed = 1, 0
   
   
    def roll(self, roll):
        if roll < 0 or roll > 10:
            raise ValueError(f'check pins: {roll}')
        
        self.frames.setdefault(self.frame,[]).append(roll)
        
        frames, frameno = self.frames, self.frame
        frame = frames[frameno]
        
        if sum(frame) > 10 or (
            frameno == 12 and frames[11][0] < 10 
            and frames[11][0] + frame[0] > 10):
            raise ValueError(f'bad frame{frameno} score')
        
        if frameno > 12 or (
            frameno == 12 and frames[10][0] < 10) or (
            frameno > 10 and sum(frames[10]) < 10):
            raise IndexError('too many rolls')
        
        if frameno > 10 or roll == 10:
            self.framed = True
            
        if self.framed:
            self.frame += 1
        
        self.framed = not self.framed
        
        
    def score(self):
        scores = []
        frames = self.frames
        
        try:
            if frames[10][0] == 10 and frames[12] or (
            sum(frames[10]) == 10 and frames[11]): pass
        except:
            raise IndexError('not enough rolls')

        for frame in range(1, 11):
            if frames[frame][0] == 10:
                if frames[frame+1][0] == 10:
                    score = 20 + frames[frame+2][0]
                elif frame == 10:
                    score = 10 + sum(frames[11]+frames[12])
                else:
                    score = 10 + sum(frames[frame+1])
            elif sum(frames[frame]) == 10:
                score = 10 + frames[frame+1][0]
            else:
                score = sum(frames[frame])
                
            scores.append(score)

        return sum(scores) 


    
    
