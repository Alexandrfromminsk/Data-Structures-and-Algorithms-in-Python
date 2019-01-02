import unittest
from Exercises.solutions.most_frequent_char import most_frequent_char

class TestMostFreqChar(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(most_frequent_char(""),"")
        self.assertEqual(most_frequent_char("AAbabab"), "b")
        self.assertEqual(most_frequent_char("azazazaza"),"a")
        self.assertEqual(most_frequent_char("azazazazz"), "z")
        self.assertEqual(most_frequent_char("aaa cc b !! cdsf"), " ")
        self.assertEqual(most_frequent_char("ababab"), "b")



if __name__ == "__main__":
    unittest.main()