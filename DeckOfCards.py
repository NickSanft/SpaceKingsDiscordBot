import CardUtils
import random

class Deck:

    def __init__(self):
        self.cards = [ Card( rank, suit, rank + " of " + suit) for rank in CardUtils.getRanks() for suit in CardUtils.getSuits()]
        self.cards.append(Card("Joker","Red","Red Joker"))
        self.cards.append(Card("Joker","Black","Black Joker"))

        random.shuffle(self.cards)
    
    def drawCard(self):
        return self.cards.pop()
        

        

class Card:
    def __init__(self, suit, value, description):
        self.suit = suit
        self.value = value
        self.description = description

if __name__ == "__main__":
    deck = Deck()

    card = deck.drawCard()
    print(card.suit)
    print(card.value)
    print(card.description)