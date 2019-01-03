import unittest
from Exercises.solutions.chunks import chunks

class TestChunk(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(chunks([1, 2, 3, 4, 5, 6], 3), [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(chunks([1,2,3,4,5],2),[[1,2],[3,4],[5]])
        self.assertEqual(chunks([1, 2, 3], 1), [[1],[2],[3]])
        self.assertEqual(chunks([1, 2, 3, 4, 5],0), [1, 2, 3, 4, 5])
        self.assertEqual(chunks([1, 2, 3, 4, 5], 7), [[1, 2, 3, 4, 5]])

if __name__=="__main__":
    unittest.main()