import unittest
from Exercises.solutions import inverse_int

class TestInverseInt(unittest.TestCase):

    def test_simple_int(self):
        self.AssertTrue(inverse_int(123),321)


if __name__ == '__main__':
    unittest.main()
