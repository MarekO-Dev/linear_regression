import unittest

class TestNumbers(unittest.TestCase):

    def test_two_equal_two(self):
        self.assertIs(290, 290)
        self.assertIsNot(1, 5)


if __name__ == "__main__":
    unittest.main()