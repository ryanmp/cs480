import unittest
import random
from scanner import *
from generator import *
from tree import *

class TestExpressionProduction(unittest.TestCase):    
    def test_gforth_script(self):
        _input = "[[+ 1 2]]"
        expected_output = "1 2 + . CR bye"
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
    
        