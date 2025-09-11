# Score categories

YACHT = lambda dice: (50 if len(set(dice)) == 1 else 0)
ONES = lambda dice: sum(die for die in dice if die == 1)
TWOS = lambda dice: sum(die for die in dice if die == 2)
THREES = lambda dice: sum(die for die in dice if die == 3)
FOURS = lambda dice: sum(die for die in dice if die == 4)
FIVES = lambda dice: sum(die for die in dice if die == 5)
SIXES = lambda dice: sum(die for die in dice if die == 6)
FULL_HOUSE = lambda dice: sum(
    die for die in dice if len(set(dice)) == 2 
    and str(dice.count(list(set(dice))[0])) in '23'
    )
FOUR_OF_A_KIND = lambda dice: (
    4 * list(set(dice))[0] if len(set(dice)) == 1 
    else sum(die for die in dice if dice.count(die) == 4)
    )
LITTLE_STRAIGHT = lambda dice: (30 if dice == [1,2,3,4,5] else 0)
BIG_STRAIGHT = lambda dice: (30 if dice == [2,3,4,5,6] else 0)
CHOICE = lambda dice: sum(dice)

def score(dice, category):
    dice.sort()
    return category(dice)