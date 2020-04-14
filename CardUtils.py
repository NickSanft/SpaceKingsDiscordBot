import re

def getRanks(): 
    return [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]
def getSuits(): 
    return [ "Clubs", "Diamonds", "Hearts", "Spades" ]

def isSuccess(suit: str):
    successRanks = ['Ace','Jack','Queen','King']
    if any(re.findall('|'.join(successRanks),suit)):
        return True
    return False

def isFailure(suit: str):
    return suit == 'Joker'