def Peek(deck: list) -> string:
    return "The next card in the deck is: ", deck.pop()

def xRay(dealerHand: list) -> string:
    return "The dealers next card is: ", deck.pop()

def Insurance(betAmt: int):
    return "Cut your losses in half this hand!"    

def Duplicate(deck: list, playerHand: list): 
    result = deck.pop()
    playerHand.append(result)
    playerHand.append(result)

def DrawTwo(deck: list):
    resultOne = deck.pop()
    resultTwo = deck.pop()

    return resultOne, resultTwo

def Mulligan(deck: list):
    resultOne = deck.pop()
    resultTwo = deck.pop()

    return resultOne, resultTwo


