############
# War Game #
############

#########
# imports
#########

import random

##################
# Global Variables
##################

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}


#########
# Classes
#########

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create card object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()


# player
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        # remove card from the top of the player's deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # cards.extend()
        if isinstance(new_cards, list):
            # if type(new_cards) == type([]):     # if new cards are a list i.e. multiple cards
            self.all_cards.extend(new_cards)
        else:
            # for a single card
            self.all_cards.append(new_cards)

    def show_hand(self):
        for i in range(len(self.all_cards)):
            print(self.all_cards[i])

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'
