import unittest
import random
from scanner import *
from parser import *
  
@unittest.skip("skipping scanner tests for milestone 3")    
class TestSpecialCases(unittest.TestCase):
    #def setUp(self):
            
    def test_keywords_only(self):
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
         
    def test_comment_lines(self):
        # Arrange
        _input = "// this is a comment line "
        
        # Act
        expected_tokens = []
        actual_tokens = scanner(_input)
        
        # Assert
        self.assertEqual(expected_tokens, actual_tokens[0])
    
    def test_real_numbers(self):
        _input = "1.2345 12345.0 .1234 0.1234"
        expected_tokens = [
                           ('real_number', '1.2345'),
                           ('real_number', '12345.0'),
                           ('real_number', '.1234'),
                           ('real_number', '0.1234')]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])    
        
    def test_constant_string(self):
        _input = '[stdout "hello world !@#$%^&*()[]"]'
        expected_tokens = [
                           ('bracket-l','['),
                           ('keyword','stdout'),
                           ('string', 'hello world !@#$%^&*()[]'),
                           ('bracket-r',']')]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])
    
    def test_identifiers_vs_keywords(self):
        _input = '[let [[a int][b real]]]'
        expected_tokens = [
                           ('bracket-l','['),
                           ('keyword','let'),
                           ('bracket-l','['),
                           ('bracket-l','['),
                           ('ID','a'),
                           ('keyword','int'),
                           ('bracket-r',']'),
                           ('bracket-l','['),
                           ('ID','b'),
                           ('keyword','real'),
                           ('bracket-r',']'),
                           ('bracket-r',']'),
                           ('bracket-r',']'),
                           ]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])
        
    def test_assignment_operator(self):
        _input = '[:= x 123][:= y 1.23][:= z .123]'
        expected_tokens = [
                           ('bracket-l','['),
                           ('assignment_op',''),
                           ('ID','x'),
                           ('int_number','123'),
                           ('bracket-r',']'),
                           
                           ('bracket-l','['),
                           ('assignment_op',''),
                           ('ID','y'),
                           ('real_number','1.23'),
                           ('bracket-r',']'),
                           
                           ('bracket-l','['),
                           ('assignment_op',''),
                           ('ID','z'),
                           ('real_number','.123'),
                           ('bracket-r',']'),
                           ]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])

@unittest.skip("skipping scanner tests for milestone 3")    
class TestExpressions(unittest.TestCase):
    def test_unary_operators(self):
        _input = '[sin x]'
        expected_tokens = [('bracket-l','['),
                       ('trig_op','sin'),
                       ('ID','x'),
                       ('bracket-r',']')]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])
                           
        expected_output = [()]
        
    def test_binary_expressions(self):
        _input = '[+ 1 [* 2 3]]'
        expected_tokens = [('bracket-l','['),
                       ('arithmatic_op','+'),
                       ('int_number','1'),
                       ('bracket-l','['),
                       ('arithmatic_op','*'),
                       ('int_number','2'),
                       ('int_number','3'),
                       ('bracket-r',']'),
                       ('bracket-r',']')]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])

@unittest.skip("skipping scanner tests for milestone 3")            
class TestInvalidTokens(unittest.TestCase):
    def test_possible_invalid_string_constants(self):
        _input = '"hello world'
        expected_output = []
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])
    
    def test_possible_invalid_identifier_name(self):
        _input = '2varName'
        expected_output = [('int_number', '2'), ('ID', 'varName')]
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])

@unittest.skip("skipping scanner tests for milestone 3")    
class TestScientificNotation(unittest.TestCase):
    def test_positive_exponent(self):
        _input = "1.0e3 1.123e123"
        expected_output = [('real_number', '1.0e3'),
                           ('real_number', '1.123e123')]
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])
    
    def test_invalid_exponent(self):
        _input = "1.0e 1"
        expected_output = []
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])
   
