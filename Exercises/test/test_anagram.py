import unittest
from Exercises.solutions.anagram import anagram

class TestAnagram(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(anagram("azaza", "zz aaa"), True)
        self.assertEqual(anagram("aza()za", "zz! aaa"), True)
        self.assertEqual(anagram("С новым годом!", "говно с дымом"), True)

    def test_negative(self):
        self.assertEqual(anagram("fhrihlyg", "ohiod"), False)
        self.assertEqual(anagram("aazzz", "aaazzz"), False)

if __name__=="__main__":
    unittest.main()