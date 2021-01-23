from numpy import random

suits = [1, 2, 3, 4]
cards = [14, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13]


deck = [(s, v) for s in suits, for c in cards]

class Dealer:
    def __init__(self, cards_shown):
        self.cards_shown = cards_shown

    def addCard(self, deck, round):
        if round = 1:
            return [deck[random.randint(len(deck))], 
                    deck[random.randint(len(deck))], 
                    deck[random.randint(len(deck))]]
        elif round = 2:
            return deck[random.randint(len(deck))]
        elif round = 3:
            return deck[random.randint(len(deck))]

    def Showdown(self, hands):
        for i in hands:
            #gotta check the value of each hand from top to bottom