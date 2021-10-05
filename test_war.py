#########
# Imports
#########

import Classes
from Classes import *
import unittest


#########

class BigTest(unittest.TestCase):

    def setUp(self) -> None:
        print('running unitTest setup')


class TestDemo(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


class TestDeck(unittest.TestCase):

    def test_is_deck(self):
        test_deck = Classes.Deck()
        self.assertEqual(type(test_deck), Classes.Deck, "Class was not a Deck")

    def test_shuffle_deck(self):
        """
        generates a deck object and shuffles it. deals a number of cards and verifies they
        are not the cards from the top of an unshuffled deck.
        :return: pass/fail
        """

        # generate a player and a deck for each.
        clean_deck = Classes.Deck()
        shuffled_deck = Classes.Deck()
        top_three = Player('organized hand player')
        shuffled_three = Player('shuffled hand player')

        shuffled_deck.shuffle()

        for _ in range(3):
            top_three.add_cards(clean_deck.deal_one())
            shuffled_three.add_cards(shuffled_deck.deal_one())

        self.assertNotEqual(top_three, shuffled_three, 'shuffled hand equal to clean hand')


class TestPlayer(unittest.TestCase):

    def test_is_player(self):
        test_player = Classes.Player('test player')
        self.assertEqual(type(test_player), Classes.Player, "class was not a Player")

   # def test_receive_card(self):
   #     pass
   #
   # def test_receive_multi_card(self):
   #     pass
   #
   # def test_show_hand(self):
   #     pass




###########
if __name__ == "__main__":
    unittest.main()
