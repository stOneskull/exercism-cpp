def best_hands(hands):
    if len(hands) == 1: return hands
    board = {hand: score(hand) for hand in hands}
    return calc(board)


def score(hand):
    cardnums = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    cards, suits = [], []
    for card in hand.split():
        cards.append(int(cardnums.get(card[:-1], card[:-1])))
        suits.append(card[-1])

    cardcount = {card: cards.count(card) for card in cards}
        
    cards.sort()
    high, low = max(cards), min(cards)
    
    straight = len(set(cards)) == 5 and high - low in (4, 12)
    flush = len(set(suits)) == 1

    if flush and straight:
        if high == 14 and low == 2:
            high = 5
        return 1, [high]

    elif 4 in cardcount.values():
        for card, quant in cardcount.items():
            if quant == 4:
                quad = card
            else:
                other = card         
        return 2, [quad, other]

    elif len(cardcount) == 2:
        for card, quant in cardcount.items():
            if quant == 3:
                trip = card
            else:
                pair = card
        return 3, [trip, pair]
        
    elif flush: 
        return 4, reversed(cards)
		
    elif straight:
        if high == 14 and low == 2:
            high = 5
        return 5, [high]

    elif len(cardcount) == 3:
        if 3 in cardcount.values():
            for card, quant in cardcount.items():
                if quant == 3:
                    cards = list(set(cards))
                    cards.remove(card)
                    return 6, [card, max(cards), min(cards)]
                    
        pairs = list(reversed(sorted(
            card for card in set(cards)
             if cards.count(card) == 2)))
        for card in cards:
            if cards.count(card) == 1:
                pairs.append(card)
        return 7, pairs

    elif len(cardcount) == 4:
        order = [
            card for card in cards if cards.count(card) == 1]
        for card in cards:
            if cards.count(card) == 2:
                order.append(card)
        return 8, reversed(order)

    return 9, reversed(cards)


def calc(board):
    tophand = min(v[0] for v in board.values())
    highs = [
        hand for hand in board if board[hand][0] == tophand]
    if len(highs) == 1: return highs
    
    while True:
        high = kick(board, highs)
        if high == highs or high is None: break
        highs = high
    return highs
    
    
def kick(board, hands):
    kickers = zip(*[board[hand][1] for hand in hands])
    for tup in kickers:
        if max(tup) == min(tup): continue
        winners = [
            i for i, kicker in enumerate(tup) if kicker == max(tup)]
        return [hands[i] for i in winners]

