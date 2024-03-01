import unittest
from magic import answer
from main import add


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_answer(self):
        self.assertEqual(add(1, answer), 421)


if __name__ == "__main__":
    unittest.main()
