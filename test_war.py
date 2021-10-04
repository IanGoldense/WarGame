from Classes import *
import unittest


#########

class BigTest(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = Deck()


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


class TestDeck(unittest.TestCase):

    def is_deck(self):
        test_deck = Deck()
        self.assertEqual(type(test_deck), 5)


###########
#if __name__ == "__main__":
#    unittest.main()
