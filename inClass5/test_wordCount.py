import unittest
import wordCount

class TestCase(unittest.TestCase):

    #test leading space
    def test_wordCount(self):
        #startChar = wordCount.words[0]
        #self.assertEqual(wordCount.howMany(" hi al"), " ")
        self.assertEqual(wordCount.howMany(" hi al"), 2)
        
    #test newline only
    def test_wordCount_1(self):
        #startChar = input("Write sentence")[0]
        self.assertEqual(wordCount.howMany("\n"), 0)


if __name__ == '__main__':
    unittest.main()