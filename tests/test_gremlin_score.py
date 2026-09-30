import unittest

from scripts.gremlin_score import calculate_score


class GremlinScoreTests(unittest.TestCase):
    def test_score(self):
        self.assertEqual(calculate_score(3, 1), 75)

    def test_empty_score(self):
        self.assertIsNone(calculate_score(0, 0))

    def test_negative_count(self):
        with self.assertRaises(ValueError):
            calculate_score(-1, 0)


if __name__ == "__main__":
    unittest.main()
