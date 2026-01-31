import random

def givePowerUpRandomizer():
    powerUps = ["peek", "xray", "mulligan", "insurance", "duplicate", "drawTwo"]  # maybe add more
    selection = random.choice(powerUps)

    if selection == "peek":
        print("Peek powerup: lets you see the next card in the deck")
    elif selection == "xray":
        print("X-ray powerup: lets you see the dealer's hidden card")
    elif selection == "mulligan":
        print("Mulligan powerup: lets you redraw your last card")
    elif selection == "insurance":
        print("Insurance powerup: saves 50'%' percent of the bet if bet lost")
    elif selection == "duplicate":
        print("Duplicate powerup: duplicates your next card")
    elif selection == "drawTwo":
        print("Draw Two powerup: draw two cards and keep the best")
    else:
        print(f"Unknown powerup: {selection}")

    return selection
