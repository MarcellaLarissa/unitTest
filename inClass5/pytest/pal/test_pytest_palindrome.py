import palindrome
    
class TestClass:
    #Test upper case
    def test_one(self):
        assert palindrome.isPalindrome("Racecar") == False

    #Test leading space
    def test_two(self):
        assert palindrome.isPalindrome(" racecar") == False
        

