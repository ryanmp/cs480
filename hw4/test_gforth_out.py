import unittest
import random
from scanner import *
from generator import *
from tree import *

class TestExpressionProduction(unittest.TestCase):
    #@unittest.skip("skipping tests for now")        
    def test_gforth_script(self):
        _input = "[[+ 1 2]]"
        expected_output = "1 2 + CR bye"
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
    
    def test_gforth_print_string(self):
        _input = '[[stdout "hello world"]]'
        expected_output = 's" hello world" type CR bye'
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
        
        