import unittest
import random
from scanner import *
from parser_v2 import *
from tree import *

class TestExpressionProduction(unittest.TestCase):    
    def test_correct_sintax(self):
        _input = [
        "[[if x y z]]",
        "[[]]",
        "[[[]]]",
        "[[stdout 5.2]]",
        "[[:= x 6]]",
        "[[sin x]]",
        "[[let [[x bool]]]]",
        "[[let [ [x bool] [y int] ] ]]",
        "[ [while x y] ]",
        "[ [while x y z ] ]",
        '[[+ 1 3]]',
        '[[+ 1 [+ 1 1]]]',
        '[[+ 1 [* [+ 2 3] 7]]]',
        '[[:= x [- x 1]]]',
        '[[+ 1 x][+ 1 1]]',
        '[[][]]',
        '[[][][]]',
        '[[ := x [+ 1 1] ]]',
        '[[+ 1 [* [+ 2 3] 7]]]' # e.g. from class website
        ]
        
        expected_output = ['yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes',
                           'yes']
        
        actual_output = test(_input,False,False)
        
        self.assertEqual(expected_output, actual_output)
    
        