import test_config
import unittest
from subset import Subset

class SubsetUnitTestCase(unittest.TestCase):
    def setUp(self):
       self.s = Subset('deer')

       self.testPatterns = [[2, 2], [4], [1, 3], [3, 1], [1, 1, 2],
       [1, 2, 1], [2, 1, 1], [1, 1, 1, 1]]

       self.testChunkings = [['de', 'er'], ['deer'], ['d', 'eer'],
                             ['dee', 'r'], ['d', 'e', 'er'], ['d', 'ee', 'r'],
                             ['de', 'e', 'r'], ['d', 'e', 'e', 'r']]

    def test_inits_word(self):
        self.assertEqual(self.s.word, 'deer')

    def test_calculate_max_chunks(self):

        self.s.calculateChunkPatterns()

        self.assertEqual(self.s.patterns, self.testPatterns)

    def test_chunk_given_patterns(self):
        self.s.applyPatterns(self.testPatterns)

        self.assertEqual(self.s.chunkings, self.testChunkings)

if __name__ == "__main__":
    unittest.main()
