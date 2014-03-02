import unittest
import random
from scanner import *
from generator import *
from tree import *

class TestExpressionProduction(unittest.TestCase):
    @unittest.skip("skipping test for now")        
    def test_gforth_script(self):
        _input = "[[+ 1 2]]"
        expected_output = "1 2 + CR bye"
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
    @unittest.skip("skipping test for now")
    def test_gforth_print_string(self):
        _input = '[[stdout "hello world"]]'
        expected_output = 's" hello world"  type CR bye'
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
    @unittest.skip("skipping test for now")
    def test_gforth_print_int(self):
        _input = '[[stdout 1234]]'
        expected_output = '1234  . CR bye'
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
        
    @unittest.skip("skipping test for now")
    def test_gforth_print_expr(self):
        _input = '[[stdout [+ 1 2]]]'
        expected_output = '1 2 +  . CR bye'
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
        
    @unittest.skip("skipping test for now")
    def test_gfort_print_stack_float(self):
        _input = '[[cos 2][sin 1.2]]'
        expected_output = '2 s>f fcos 2.2e fsin CR bye'
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
    
    @unittest.skip("skipping test for now")
    def test_gforth_test_negative_float(self):
        _input = '[[- 2.0]]'
        expected_output = '2.0e fnegate CR bye'
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
    
    #@unittest.skip("skipping test for now")
    def test_gforth_test_if_then(self):
        _input = '[[if [< 1 2] [stdout 1]]]'
        expected_output = ': BR 2 < if 1 . then ; 1 BR'
        actual_output = generate_gforth_script(_input)
        
        self.assertEqual(expected_output, actual_output)
        
        
        
        
        
    