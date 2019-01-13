import unittest
from Exercises.solutions.ways_to_decode import ways_to_decode

class TestWaysToDecode(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(ways_to_decode("555"),1)
        self.assertEqual(ways_to_decode("AAbabab"), "b")
        self.assertEqual(ways_to_decode("azazazaza"),"a")
        self.assertEqual(ways_to_decode("azazazazz"), "z")
        self.assertEqual(most_frequent_char("aaa cc b !! cdsf"), " ")
        self.assertEqual(most_frequent_char("ababab"), "b")



if __name__ == "__main__":
    unittest.main()