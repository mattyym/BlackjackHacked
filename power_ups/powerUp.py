def Peek(deck: list) -> string:
    return "The next card in the deck is: ", deck[-1]

def xRay(dealerHand: list) -> string:
    return "The dealers next card is: ", deck[-1]

def Insurance(betAmt: int):
    # lock losses to 50%
    return "Cut your losses in half this hand!"    

def Duplicate(deck: list): 
    return deck.pop()

def DrawTwo(deck: list):
    resultOne = deck.pop()
    resultTwo = deck.pop()
    response = input("The first card is: ", resultOne, " do you want to keep this card? No to draw again (Y/N)")
    if response == "N":
        print("The card: ", resultTwo, "will be added to your hand")
        return resultTwo
    else:
        print("The card: ", resultOne, "Will be added to your hand")
        return resultOne

def Mulligan(deck: list):
    return deck.pop()


