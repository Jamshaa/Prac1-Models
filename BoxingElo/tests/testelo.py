import unittest
from boxingelo.elo_calculator import EloCalculator

class TestEloCalculator(unittest.TestCase):
    def setUp(self):
        self.elo = EloCalculator()

    def test_initial_rating(self):
        self.assertEqual(self.elo.get_rating("Ali"), 1500)

    def test_elo_update(self):
        self.elo.update_ratings("Ali", "Tyson")
        self.assertGreater(self.elo.get_rating("Ali"), 1500)
        self.assertLess(self.elo.get_rating("Tyson"), 1500)

if __name__ == "__main__":
    unittest.main()
