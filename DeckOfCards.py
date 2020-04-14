import random
import re

regularSuits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "Jack", "Queen", "King"]
successRanks = ['Ace', 'Jack', 'Queen', 'King']


class Deck:

    def __init__(self):
        self.cards = [Card(rank, suit, rank + " of " + suit)
                      for rank in ranks for suit in regularSuits]
        self.cards.append(Card("Joker", "Red", "Red Joker"))
        self.cards.append(Card("Joker", "Black", "Black Joker"))

        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()


class Card:
    def __init__(self, rank, suit, description):
        self.suit = suit
        self.rank = rank
        self.description = description

    def isSuccess(self):

        if any(re.findall('|'.join(successRanks), self.rank)):
            return True
        return False

    def isFailure(self):
        return self.rank == "Joker"

    def isQueenOfHearts(self):
        return self.suit == "Hearts" and self.rank == "Queen"


if __name__ == "__main__":
    deck = Deck()

    card = deck.drawCard()
    print(card.suit)
    print(card.rank)
    print(card.description)
