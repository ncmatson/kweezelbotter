import os
import sys

os.chdir('../kweezelbotter')
sys.path.append(os.getcwd())

import unittest
from kweezelbotter.kweezelbotter import Kweezelbotter

TEST_DICTIONARY = 'support/test_dict.txt'
TEST_WORD       = "kweezelbotter"

class KweezelbotterTestCase(unittest.TestCase):
    """Tests for Kweezelbotter"""

    def setUp(self):
        self.kweezelbotter = Kweezelbotter(TEST_WORD)

    def test_initializes_correctly(self):
        self.assertEqual(self.kweezelbotter.dictionary, "./dict/dict.txt")
        self.assertEqual(self.kweezelbotter.word, TEST_WORD)

    def test_sets_dictionary(self):
        self.kweezelbotter.set_dictionary(TEST_DICTIONARY)
        self.assertEqual(self.kweezelbotter.dictionary, TEST_DICTIONARY)

    def test_chunks_word_correctly(self):
        chunks = self.kweezelbotter.chunk_word("kweezelbotter")
        self.assertEqual(len(chunks), 4)
        self.assertEqual(chunks[0], "kwee")
        self.assertEqual(chunks[1], "zel")
        self.assertEqual(chunks[2], "bot")
        self.assertEqual(chunks[3], "ter")

    def test_isolates_phone_sequence(self):
        sequence = self.kweezelbotter.isolate_sequence("kwee", TEST_DICTIONARY)
        self.assertEqual(len(sequence), 3)
        self.assertEqual(sequence[0], 'K')
        self.assertEqual(sequence[1], 'W')
        self.assertEqual(sequence[2], 'IY2')

if __name__ == '__main__':
    unittest.main()
