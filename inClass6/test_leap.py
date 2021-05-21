import unittest
import leap

class TestCase(unittest.TestCase):

    #test input is not none
    def test_leap(self):
        self.assertTrue(leap.leapyr(2000))
        
        #test return is not empty
    def test_leap_1(self):
        self.assertFalse(leap.leapyr(1900))        
        
   
if __name__ == '__main__':
    unittest.main()