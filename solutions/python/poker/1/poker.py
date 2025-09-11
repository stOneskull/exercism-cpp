def best_hands(hands):

    if len(hands) == 1:
        return hands

    for hand in hands:
        cards = hand.split()

    cards_1 = hands[0].split()
