import unittest
from magic import answer_to_life
from main import add


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_answer(self):
        self.assertEqual(add(1, answer_to_life), 43)


if __name__ == "__main__":
    unittest.main()
