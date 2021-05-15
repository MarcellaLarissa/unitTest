import wordCount
    
class TestClass:
    #Test leading space
    def test_one(self):
        assert wordCount.howMany(" Hi guys!") == 2

    #Test newline
    def test_two(self):
        assert wordCount.howMany("\n") == 0
        

