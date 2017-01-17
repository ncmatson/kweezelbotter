import test_config
import unittest
from subset import Subset

class SubsetUnitTestCase(unittest.TestCase):
    def setUp(self):
       self.s = Subset('deer')

    def test_inits_word(self):
        self.assertEqual(self.s.word, 'deer')

    def test_calculate_max_chunks(self):

        self.s.calculateChunkPatterns()

        self.assertEqual(self.s.patterns, [[2,2], [4]])

    def test_chunk_given_patterns(self):
        patterns = [[2,2], [4]]

        chunks = self.s.applyPatterns(patterns)

        self.assertEqual(chunks, [['de', 'er'], ['deer']])

if __name__ == "__main__":
    unittest.main()
