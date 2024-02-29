import unittest
from magic import answer
from main import add_two


class TestMain(unittest.TestCase):
    def test_add_two(self):
        """Add two.."""
        self.assertEqual(add_two(1, 2), 3)

    def test_add_answer(self):
        self.assertEqual(add_two(1, answer), 2)


if __name__ == "__main__":
    unittest.main()
