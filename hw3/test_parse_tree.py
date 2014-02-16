import unittest
import random
from scanner import *
from parser import *

class TestExpressionProduction(unittest.TestCase):

    def test_single_brackets(self):
        _input = "[[+ 1 2]]"
        expected_output = () # return (tree, result)
        actual_output = parser(_input)
        self.assertEqual(expected_output, actual_output)
    
    #TODO: add test nested brackets
    '''
    def test1_15_test_nested_brackets(self):
        _input = "[]"
        expected_output = (['[','[','+',3,2,']',']'], 5) # return (tree, result)
        actual_output = parse_line(_input)
        self.assertEqual(expected_output, actual_output)
    '''
                
   





