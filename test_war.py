import Classes
from Classes import *
import unittest
import main


#########

class BigTest(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()


class TestDeck(unittest.TestCase):

    def test_is_deck(self):
        test_deck = Classes.Deck()
        self.assertEqual(type(test_deck), Classes.Deck)

    def test_shuffle_deck(self):
        '''

        :return:
        '''
        test_deck = Classes.Deck()
        Classes.Deck.shuffle()
        self.assertNotEqual(test_deck.deal_one(), 'Ace of Clubs')


###########
if __name__ == "__main__":
    unittest.main()
