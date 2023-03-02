import unittest
from clean_text import cleanText

# cleanText() takes a string a reutrns only Japanese characters

class TestClass(unittest.TestCase):
    def test_cleanText_0(self):
        assert cleanText("私はジョニーです") == "私はジョニーです"
    def test_cleanText_1(self):
        assert cleanText("My name is Jonny.") == ""
    def test_cleanText_2(self):
        assert cleanText("My name is Jonny, in Japanese ジョニー") == "ジョニー"
    def test_cleanText_3(self):
        assert cleanText("100") == ""
    def test_cleanText_4(self):
        assert cleanText("!?!?!?!") == ""
		
if __name__=='__main__':
	unittest.main()
	
