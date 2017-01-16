import test_config
import unittest
from utils import Utils

class UtilsTestCase(unittest.TestCase):

    def test_flattens_list(self):
        test_list = ["cat", ["cat", "dog", ["cat", "dog", "bird"]]]
        flat_list = Utils.flatten(test_list)

        self.assertEqual(flat_list, ["cat", "cat", "dog", "cat", "dog", "bird"])

if __name__ == "__main__":
    unittest.main()
