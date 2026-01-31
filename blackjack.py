import random

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

deck = list(cards.keys()) * 4

def deal_card():
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

def blackjack():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print("\n--- Blackjack ---\n")
    show_hand(player_hand, "Player")
    print(f"Dealer shows: {dealer_hand[0]}\n")

    while hand_value(player_hand) < 21:
        move = input("Hit or Stand? (h/s): ").lower()
        if move == "h":
            player_hand.append(deal_card())
            show_hand(player_hand, "Player")
        else:
            break

    if hand_value(player_hand) > 21:
        print("You busted, the dealer smoked yo buns!!")
        return

    show_hand(dealer_hand, "Dealer")
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        show_hand(dealer_hand, "Dealer")

    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    print("--- Final Results ---\n")
    show_hand(player_hand, "Player")
    show_hand(dealer_hand, "Dealer")

    if dealer_total > 21 or player_total > dealer_total:
        print("\nYou won!\n")
    elif player_total < dealer_total:
        print("\nYou lost!\n")
    else:
        print("\nDraw!\n")

if __name__ == "__main__":
    blackjack()
