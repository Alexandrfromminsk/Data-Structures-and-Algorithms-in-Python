import unittest
from Exercises.solutions.inverse_int import inverse_int

class TestInverseInt(unittest.TestCase):

    def test_simple_int(self):
        self.assertEqual(inverse_int(123),321);
        self.assertEqual(inverse_int(2), 2);
        self.assertEqual(inverse_int(1234), 4321);
        self.assertEqual(inverse_int(0), 0);

    def test_with_zeroes(self):
        self.assertEqual(inverse_int(9000),9);
        self.assertEqual(inverse_int(700), 7);

    def test_negative(self):
        self.assertEqual(inverse_int(-123),-321);

    def test_negative_with_zeroes(self):
        self.assertEqual(inverse_int(-102300),-3201);


if __name__ == '__main__':
    unittest.main()
