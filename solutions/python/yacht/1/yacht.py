# Score categories
# Change the values as you see fit

def score(dice, category):

    print(category)
    print(str(category))

    scores = dict(
YACHT = (50 if len(set(dice)) == 1 else 0),
ONES = sum(die for die in dice if die == 1 and dice.count(1) >= 3),
TWOS = sum(die for die in dice if die == 2 and dice.count(2) >= 3),
THREES = sum(die for die in dice if die == 3 and dice.count(3) >= 3),
FOURS = sum(die for die in dice if die == 4 and dice.count(4) >= 3),
FIVES = sum(die for die in dice if die == 5 and dice.count(5) >= 3),
SIXES = sum(die for die in dice if die == 6 and dice.count(6) >= 3),
FULL_HOUSE = sum(die for die in dice 
    if len(set(dice)) == 2 
    and str(dice.count(set(dice)[0])) in '23'),
FOUR_OF_A_KIND = (4 * die for die in dice if dice.count(die) >= 4),
LITTLE_STRAIGHT = (30 if len(set(dice)) == 5 and 1 in set(dice) else 0),
BIG_STRAIGHT = (30 if len(set(dice)) == 5 and 6 in set(dice) else 0),
CHOICE = sum(dice)
)
    
    score = scores[str(category)[6:]]
    print(score)

    return score