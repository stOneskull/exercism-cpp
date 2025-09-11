YACHT = lambda dice: (50 if len(set(dice)) == 1 else 0)

ONES = lambda dice: sum(d for d in dice if d == 1)
TWOS = lambda dice: sum(d for d in dice if d == 2)
THREES = lambda dice: sum(d for d in dice if d == 3)
FOURS = lambda dice: sum(d for d in dice if d == 4)
FIVES = lambda dice: sum(d for d in dice if d == 5)
SIXES = lambda dice: sum(d for d in dice if d == 6)

FULL_HOUSE = lambda dice: sum(
    d for d in dice if len(set(dice)) == 2
    and dice.count(dice[0]) in (2, 3)
    )
FOUR_OF_A_KIND = lambda dice: (
    4 * dice[0] if len(set(dice)) == 1
    else sum(d for d in dice if dice.count(d) == 4)
    )
LITTLE_STRAIGHT = lambda dice: (
    30 if dice == [1,2,3,4,5] else 0
    )
BIG_STRAIGHT = lambda dice: (
    30 if dice == [2,3,4,5,6] else 0
    )
CHOICE = sum

def score(dice, category):
    dice.sort()
    return category(dice)
