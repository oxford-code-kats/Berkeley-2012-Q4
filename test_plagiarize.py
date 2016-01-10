import unittest
from plagiarize import dissimilarity

class TestPlagiarize(unittest.TestCase):

    def test_empty_strings_returns_zero(self):
        a = ""
        b = ""
        result = dissimilarity(a, b)
        self.assertEqual(result, 0)
    
    def test_one_char_returns_one(self):
        a = "a"
        b = ""
        result = dissimilarity(a, b)
        self.assertEqual(result, 1)

    def test_two_similar_chars_give_zero(self):
        a = "a"
        b = "a"
        result = dissimilarity(a, b)
        self.assertEqual(result, 0)

    def test_two_different_chars_return_two(self):
        a = "a"
        b = "b"
        result = dissimilarity(a, b)
        self.assertEqual(result, 2)

    def test_two_of_differing_lengths(self):
        a = "a"
        b = "aa"
        result = dissimilarity(a, b)
        self.assertEqual(result, 1)

    # def test_with_lists(self):
        # a_tuple = ("", "a", "a", "a", "a") 
        # b_tuple = ("", "", "a", "b", "aa") 
        # result_tuple = (0, 1, 0, 2, 1) 
           # pa_list, b_list, answer_list)
        # for i in zip(a_list, b_list, answer_list):
            # result = dissimilarity(i[0], i[1])
            # self.assertEqual(result, i[2])

if __name__ == '__main__':
    unittest.main()

