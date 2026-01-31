import random

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

deck = list(cards.keys()) * 4

def deal_hand():
    return random.choice(deck)

def hand_value(hand):
    value = sum(cards[card] for card in hand)
    aces = hand.count("A")
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def show_hand(hand, owner):
    print(f"{owner}'s hand: {hand} (Value: {hand_value(hand)})")

