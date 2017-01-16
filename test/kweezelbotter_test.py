import test_config
import unittest
from kweezelbotter import Kweezelbotter

TEST_DICTIONARY = '../test/support/test_dict.txt'
TEST_WORD       = "kweezelbotter"

class KweezelbotterTestCase(unittest.TestCase):
    """Tests for Kweezelbotter"""

    def setUp(self):
        self.kweezelbotter = Kweezelbotter()

    def test_chunks_word_correctly(self):
        chunks = self.kweezelbotter.chunk(TEST_WORD)
        self.assertEqual(chunks, ["kwee", "zel", "bot", "ter"])

    def test_pronounces_word(self):
        pronunciation = self.kweezelbotter.pronounce(TEST_WORD)
        self.assertEqual(pronunciation, "K W IY2 Z EH0 L B AH0 T T EH0 R")

if __name__ == '__main__':
    unittest.main()
