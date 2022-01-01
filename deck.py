# deck.py
# 
# the class describing the card deck
# #
import random

class Deck:
    def __init__(self):
        self.harts = [x for x in range(1, 14)]
        self.spades = [x for x in range(1, 14)]
        self.diamonds = [x for x in range(1, 14)]
        self.clubs = [x for x in range(1, 14)]
        self.card_deck = list(zip(self.clubs, self.diamonds, self.harts, self.spades))

        # shuffle the deck
        random.shuffle(self.card_deck)
    
    def get_card(self):
        if len(self.card_deck) == 0:
            print("out of cards..")
            return None
        the_card = self.card_deck.pop()
        if the_card > 9 and the_card < 13:
            return 10
        elif the_card == 13:
            return 11
        else:
            return the_card


