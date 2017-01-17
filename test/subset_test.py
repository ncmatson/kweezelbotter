import test_config
import unittest
from subset import Subset

class SubsetUnitTestCase(unittest.TestCase):

    def test_inits_word(self):
        s = Subset('deer')
        self.assertEqual(s.word, 'deer')

    def test_calculate_max_chunks(self):
        s = Subset('deer')

        scores = s.calculateChunkPatterns()

        self.assertEqual(scores, [[2,2], [4]])

    def test_chunk_given_patterns(self):
        patterns = [[2,2], [4]]
        s = Subset('deer')

        chunks = s.applyPatterns(patterns)

        self.assertEqual(chunks, [['de', 'er'], ['deer']])

if __name__ == "__main__":
    unittest.main()
