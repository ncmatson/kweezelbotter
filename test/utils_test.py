import test_config
import unittest
from utils import Utils

class UtilsTestCase(unittest.TestCase):

    def test_flattens_list(self):
        test_list = ["cat", ["cat", "dog", ["cat", "dog", "bird"]]]
        flat_list = Utils.flatten(test_list)

        self.assertEqual(flat_list, ["cat", "cat", "dog", "cat", "dog", "bird"])

    def test_maxes_by_length(self):
        long_string  = "cats"
        short_string = "at"
        l, s         = Utils.max_by_length(long_string, short_string)

        self.assertEqual(l, long_string)
        self.assertEqual(s, short_string)

if __name__ == "__main__":
    unittest.main()
