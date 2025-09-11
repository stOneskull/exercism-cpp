from random import randint

class Character:
    def __init__(self):
        for attribute in [
            'strength', 'dexterity', 'constitution', 
            'intelligence', 'wisdom', 'charisma',]:
                setattr(
                    self, attribute, self.ability())
                    
        self.hitpoints = modifier(self.constitution) + 10
        
    def ability(self):
        dice = [d(6) for die in range(4)]
        dice.remove(min(dice))
        return sum(dice)
        

def d(dienum):
    return randint(1, dienum)


def modifier(score):
    return (score - 10) // 2
