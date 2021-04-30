import unittest
import calcApp

class TestCase(unittest.TestCase):
    #test add function
    def test_add(self):
   
        self.assertEqual(calcApp.add(10, 5), 15)

    def test_add_1(self):
   
        self.assertEqual(calcApp.add(10, 10), 20)  
        
    def test_add_2(self):
   
        self.assertEqual(calcApp.add(10, 2), 15)
        
    #test sub function
    def test_sub(self):
   
        self.assertEqual(calcApp.sub(10, 5), 5)
        
    def test_sub_1(self):
   
        self.assertEqual(calcApp.sub(5, 5), 0)
        
    def test_sub_2(self):
   
        self.assertEqual(calcApp.sub(10, 2), 15)
        
    #test mult function
    def test_mult(self):
   
        self.assertEqual(calcApp.mult(10, 5), 50)
        
    def test_mult_1(self):
   
        self.assertEqual(calcApp.mult(10, 2), 20)
        
    def test_mult_2(self):
   
        self.assertEqual(calcApp.mult(10, 2), 15)
        
    #test div function
    def test_div(self):
   
        self.assertEqual(calcApp.div(10, 5), 2)

    def test_div_1(self):
   
        self.assertEqual(calcApp.div(10, 2), 5)
        
    def test_div_2(self):
   
        self.assertEqual(calcApp.div(10, 2), 15)
if __name__ == '__main__':
    unittest.main()