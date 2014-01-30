import unittest
import random
from test_scanner import *
from scanner_ryan import *

class TestScanner(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))
    
    def test1_scanner(self):
        expected = "passed all tests"
        actual = test_all()
        self.assertEqual(expected, actual)        
    
class TestSpecialCases(unittest.TestCase):
    def setUp(self):
        self.seq = range(19)
    
    def test2_keywords_only(self):
        # Arrange
        _input = "bool let real string stdout int if while"
        
        # Act
        expected_tokens = [
            ('keyword', 'bool'), 
            ('keyword', 'let'), 
            ('keyword', 'real'), 
            ('keyword', 'string'), 
            ('keyword', 'stdout'), 
            ('keyword', 'int'), 
            ('keyword', 'if'), 
            ('keyword', 'while')]
        
        actual_tokens = scanner(_input)
        
        # Assert
        self.assertEqual(expected_tokens, actual_tokens[0])
     
     #def test_keywords_recognized_before_than_ids:
    
    def test3_comment_lines(self):
        # Arrange
        _input = "// this is a comment line "
        
        # Act
        expected_tokens = []
        actual_tokens = scanner(_input)
        
        # Assert
        self.assertEqual(expected_tokens, actual_tokens[0])
           

if __name__ == '__main__':
    
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestScanner)
    module = __import__("test_driver")
    suite = unittest.TestLoader().loadTestsFromModule(module)

    print "Testing Scanner\n"
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    print "Additional Testing\n"
        
   





