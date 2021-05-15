import unittest
import palindrome

class TestCase(unittest.TestCase):

    #test if upper case allows match
    def test_wordCount(self):
        self.assertFalse(palindrome.isPalindrome("Noon"))
        
    #test basic palindrome
    def test_wordCount_1(self):
        self.assertTrue(palindrome.isPalindrome("racecar"))


if __name__ == '__main__':
    unittest.main()