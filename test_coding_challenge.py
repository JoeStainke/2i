import unittest
import coding_challenge

class TestCodingChallenge(unittest.TestCase):

    def test_function_name(self):
        self.assertEqual(coding_challenge.sum_pairs([3, 4, 5, 6], 1), 0)
        self.assertEqual(coding_challenge.sum_pairs([0, 15, 32, 2000, 15000], 15), 1)
        self.assertEqual(coding_challenge.sum_pairs([1, 1, 10, 32, 41], 42), 2)

if __name__ == '__main__':
    unittest.main()