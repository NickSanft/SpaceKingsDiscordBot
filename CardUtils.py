import re

def getRanks(): 
    return [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]
def getSuits(): 
    return [ "Clubs", "Diamonds", "Hearts", "Spades" ]

def isSuccess(rank: str):
    successRanks = ['Ace','Jack','Queen','King']
    if any(re.findall('|'.join(successRanks),rank)):
        return True
    return False

def isFailure(rank: str):
    return rank == "Joker"

def isQueenOfHearts(suit: str, rank: str):
    print(str(suit == "Hearts"))
    print(str(rank == "Queen"))
    return suit == "Hearts" and rank == "Queen"
