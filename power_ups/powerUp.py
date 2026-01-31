def Peek(deck: list) -> str:
    return f"The next card in the deck is: {deck[-1]}"

# def xRay(dealerHand: list) -> str:
#     return f"The dealers other card is: {dealerHand[-1]}"

def Insurance():
    # lock losses to 50%
    return "Cut your losses in half this hand!"    

def Duplicate(deck: list): 
    return deck.pop()

def DrawTwo(deck: list):
    resultOne = deck.pop()
    resultTwo = deck.pop()
    while True:
        response = input("The first card is: ", resultOne, " The second card is: ", resultTwo, " Pick which card you want(1/2): ")
        if response == 1:
            print("The card: ", resultOne, "will be added to your hand")
            return resultTwo
        elif response == 2:
            print("The card: ", resultTwo, "Will be added to your hand")
            return resultOne
        else:
            print("Invalid option")

def Mulligan(deck: list):
    return deck.pop()


