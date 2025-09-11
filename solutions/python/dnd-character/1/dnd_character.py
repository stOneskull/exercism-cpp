class Character:
    def __init__(self):
        for attribute in [
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma',
            ]:
                setattr(self, attribute, roll())
                
        self.hitpoints = modifier(self.constitution) + 10
        
    def ability(self):
        return roll()
                
        
def roll():
    from random import randint as d
    dice = [d(1, 6) for die in range(4)]
    dice.remove(min(dice))
    return sum(dice)


def modifier(score):
    return (score - 10) // 2
