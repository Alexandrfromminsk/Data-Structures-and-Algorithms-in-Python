import unittest
from Exercises.solutions.palindrome import palindrome

class TestPalindrome(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(palindrome('axccxa'),True)
        self.assertEqual(palindrome('asdfdsa'), True)
        self.assertEqual(palindrome('r'), True)
        self.assertEqual(palindrome('ee'), True)
        self.assertEqual(palindrome('ax3cc3xa'), True)
        self.assertEqual(palindrome('!(ax3cc3xa(!'), True)

    def test_non_palindrome(self):
        self.assertEqual(palindrome('Asddsa'),False)
        self.assertEqual(palindrome('fsagfsdgf'), False)

if __name__ == '__main__':
    unittest.main()
