import random
import power_ups.powerUp

# Create the card deck
cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
player_hand = []
dealer_hand = []
player_powerUps = ["drawTwo"]
player_points = 1000

# Function to pick a random card
def deal_card():
    return deck.pop()

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
    insuranceCheck = False
    # Initiate bet amount
    while True:
        for power in player_powerUps:
            if power == "insurance":
                insuranceUse = input("Use insurance power(Lose max 50% of bet)?(y/n): ")
                if insuranceUse == "y":
                    player_powerUps.remove(power)
                    insuranceCheck = True
                    print("Insurance Power is on for this round!!\n")
                break

        print(f"You have {player_points} points.")
        bet = input("Enter your bet amount (Win -> Bet x 2): ")
        if bet.isdigit() and 0 < int(bet) <= player_points:
            if insuranceCheck:
                betLose = int(bet) / 2
                betLose = int(betLose)
                betWin = int(bet)
            else:
                betLose = betWin = int(bet)
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
        for power in player_powerUps:
            if power == "peek":
                peekUse = input("Use peek power(See next card)?(y/n): ")
                if peekUse == "y":
                    player_powerUps.remove(power)
                    print(power_ups.powerUp.Peek(deck))
                break
        for power in player_powerUps:
            if power == "xray":
                xrayUse = input("Use Xray power(See dealer's other card)?(y/n): ")
                if xrayUse == "y":
                    player_powerUps.remove(power)
                    print("Showing Dealer's Full Hand:")
                    show_hand(dealer_hand, "Dealer")
                break
        for power in player_powerUps:
            if power == "drawTwo":
                drawTwoUse = input("Use DrawTwo power(See two cards and pick the better one.(y/n): )")
                if drawTwoUse == "y":
                    player_powerUps.remove(power)
                    new_card = power_ups.powerUp.DrawTwo(deck)
                    player_hand.append(new_card)
                    show_hand(player_hand, "Player")
                break

        move = input("Hit or Stand? (h/s): ").lower()
        if move == "h":
            player_hand.append(deal_card())
            show_hand(player_hand, "Player")
            if hand_value(player_hand) >= 21:
                break
            for power in player_powerUps:
                if power == "duplicate":
                    duplicateUse = input("Use Duplicate power(Duplicate last card)?(y/n): ")
                    if duplicateUse == "y":
                        player_powerUps.remove(power)
                        duplicated_card = player_hand[-1]
                        player_hand.append(duplicated_card)
                        print("\nCard duplicated!")
                        show_hand(player_hand, "Player")
                    break
        else:
            break

    # If player is over 21 they bust
    if hand_value(player_hand) > 21:
        player_points -= betLose
        print("\nYou busted, the dealer smoked yo buns!!")
        if insuranceCheck:
            print("Luckily, you only lost half of your bet because of that Insurance!! Good clutch up.")
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
        player_points += betWin
        print("\nYou won!\n")
        print(f"You now have {player_points} points.\n")
    elif player_total < dealer_total:
        player_points -= betLose
        print("\nYou lost!\n")
        if insuranceCheck:
            print("Luckily, you only lost half of your bet because of that Insurance!! Good clutch up.")
        print(f"You now have {player_points} points.\n")
    else:
        print("\nDraw!\n")
        print(f"You still have {player_points} points.\n")

# Main stuff to run the program
if __name__ == "__main__":
    print("\nWelcome to Black Jack Hacked: An EPIC version of BlackJack(With PowerUps)!")
    print("\nPlease review the basic rules of BlackJack before you play:")
    print("\tGet closer to 21 than the dealer without going over!")
    print("\tNumber cards are the value of their number, Duh, how didn't you know that already???")
    print("\t10, Jack, Queen, King count as 10 and Aces can be 1 or 11!")
    print("\nPowerUps:")
    print("\tPeek: Let's you see the next card in the deck")
    print("\tXray: Let's you see the Dealer's other current card")
    print("\tInsurance: Ensures you only lose at most half of your bet")
    print("\tDuplicate: Get a second of the last card you drew")
    print("\tDrawTwo: Draw two cards and pick which one you would prefer more")
    print("\tMulligan: Let's you redraw your last card\n")
    replay = True
    while replay:
        deck = list(cards.keys()) * 4
        random.shuffle(deck)
        if player_points <= 0:
            print(f"\nYou are out of points!\n")
            print("You suck! Get some bread. Game over.")
            break
        blackjack()
        while True:
            play_again = input("Play again? (y/n): ").lower()
            if play_again == "y":
                break
            elif play_again == "n":
                print("Thanks for playing! Goodbye.")
                replay = False
                break
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.\n")
                continue
