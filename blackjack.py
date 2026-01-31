import random

# Create the card deck
cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
player_hand = []
dealer_hand = []
player_points = 1000

# Function to pick a random card
def deal_card():
    return deck.pop(0)

# Function to return the full value of a hand
def hand_value(hand):
    value = sum(cards[card] for card in hand)
    aces = hand.count("A")
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Function to display the hand
def show_hand(hand, owner):
    print(f"{owner}'s hand: {hand} (Value: {hand_value(hand)})")

# Main blackjack gameplay function
def blackjack():
    global player_points
    # Initiate bet amount
    while True:
        print(f"You have {player_points} points.")
        bet = input("Enter your bet amount (Win -> Bet x 2): ")
        if bet.isdigit() and 0 < int(bet) <= player_points:
            bet = int(bet)
            break
        else:
            print("Invalid bet amount. Please try again.")

    # Initial Deal
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    # Display for start of game
    print("\n--- Blackjack ---\n")
    show_hand(player_hand, "Player")
    print(f"Dealer shows: {dealer_hand[0]}\n")

    # Loop for player to hit or stand
    while hand_value(player_hand) < 21:
        move = input("Hit or Stand? (h/s): ").lower()
        if move == "h":
            player_hand.append(deal_card())
            show_hand(player_hand, "Player")
        else:
            break

    # If player is over 21 they bust
    if hand_value(player_hand) > 21:
        player_points -= bet
        print("You busted, the dealer smoked yo buns!!\n")
        print(f"You now have {player_points} points.\n")
        return

    # Show the dealers hand and have it hit or stand for its turn
    show_hand(dealer_hand, "Dealer")
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        show_hand(dealer_hand, "Dealer")

    # Calculate final totals
    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    # Print final totals
    print("--- Final Results ---\n")
    show_hand(player_hand, "Player")
    show_hand(dealer_hand, "Dealer")

    # Establish winner and display that
    if dealer_total > 21 or player_total > dealer_total:
        player_points += bet
        print("\nYou won!\n")
        print(f"You now have {player_points} points.\n")
    elif player_total < dealer_total:
        player_points -= bet
        print("\nYou lost!\n")
        print(f"You now have {player_points} points.\n")
    else:
        print("\nDraw!\n")
        print(f"You still have {player_points} points.\n")

# Main stuff to run the program
if __name__ == "__main__":
    while True:
        deck = list(cards.keys()) * 4
        random.shuffle(deck)
        if player_points <= 0:
            print(f"\nYou are out of points!\n")
            print("You suck! Get some bread. Game over.")
            break
        blackjack()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break