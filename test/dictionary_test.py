import test_config
import unittest
from dictionary import Dictionary

TEST_DICTIONARY = '../test/support/test_dict.txt'

class DictionaryTestCase(unittest.TestCase):
    """ Tests for Dictionary """

    def setUp(self):
        self.dictionary = Dictionary(TEST_DICTIONARY)
        self.model      = self.dictionary.model

    def test_initialization(self):
        self.assertEqual(self.model["ABBOT"], "AE1 B AH0 T")
        self.assertEqual(len(self.model), 22)

    def test_filters_for_string(self):
        string              = "kwee"
        filtered_dictionary = self.dictionary.filter(string)

        self.assertEqual(len(filtered_dictionary), 4)
        for k, v in filtered_dictionary.items():
            self.assertIn(string.upper(), k)

if __name__ == "__main__":
    unittest.main()
