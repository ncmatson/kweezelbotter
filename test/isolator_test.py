import test_config
import unittest
from dictionary import Dictionary
from isolator   import Isolator

TEST_DICTIONARY = '../test/support/test_dict.txt'

class IsolatorTestCase(unittest.TestCase):
    """ Tests for Isolator """

    def setUp(self):
        dictionary    = Dictionary(TEST_DICTIONARY).model
        self.isolator = Isolator(dictionary)

    def test_isolates_sequence(self):
        sequence = self.isolator.isolate_phoneme("kwee")
        self.assertEqual(sequence, ["K", "W", "IY2"])

if __name__ == "__main__":
    unittest.main()
