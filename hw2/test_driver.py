import unittest
import random
from test_scanner import *
from scanner_ryan import *
from parser import *
class TestScanner(unittest.TestCase):

    #def setUp(self):
        
    def test0_1_scanner(self):
        expected = "passed all tests"
        actual = test_all()
        self.assertEqual(expected, actual)        
    
class TestSpecialCases(unittest.TestCase):
    #def setUp(self):
            
    def test0_2_keywords_only(self):
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
         
    def test0_3_comment_lines(self):
        # Arrange
        _input = "// this is a comment line "
        
        # Act
        expected_tokens = []
        actual_tokens = scanner(_input)
        
        # Assert
        self.assertEqual(expected_tokens, actual_tokens[0])
    
    def test0_4_test_real_numbers(self):
        _input = "1.2345 12345.0 .1234 0.1234"
        expected_tokens = [
                           ('real_number', '1.2345'),
                           ('real_number', '12345.0'),
                           ('real_number', '.1234'),
                           ('real_number', '0.1234')]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])    
        
    def test0_5_test_constant_string(self):
        _input = '[stdout "hello world !@#$%^&*()[]"]'
        expected_tokens = [
                           ('bracket-l','['),
                           ('keyword','stdout'),
                           ('string', 'hello world !@#$%^&*()[]'),
                           ('bracket-r',']')]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])
    
    def test0_6_test_identifiers_vs_keywords(self):
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
        
    def test0_7_test_assignment_operator(self):
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
    
class TestExpressions(unittest.TestCase):
    def test0_8_test_unary_operators(self):
        _input = '[sin x]'
        expected_tokens = [('bracket-l','['),
                       ('trig_op','sin'),
                       ('ID','x'),
                       ('bracket-r',']')]
        actual_tokens = scanner(_input)
        self.assertEqual(expected_tokens, actual_tokens[0])
                           
        expected_output = [()]
        
    def test0_9_test_binary_expressions(self):
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
        
class TestInvalidTokens(unittest.TestCase):
    def test1_10_test_possible_invalid_string_constants(self):
        _input = '"hello world'
        expected_output = []
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])
    
    def test1_11_test_possible_invalid_identifier_name(self):
        _input = '2varName'
        expected_output = [('int_number', '2'), ('ID', 'varName')]
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])

class TestScientificNotation(unittest.TestCase):
    def test1_12_test_positive_exponent(self):
        _input = "1.0e3 1.123e123"
        expected_output = [('real_number', '1.0e3'),
                           ('real_number', '1.123e123')]
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])
    
    def test1_13_test_invalid_exponent(self):
        _input = "1.0e 1"
        expected_output = []
        actual_output = scanner(_input)
        self.assertEqual(expected_output, actual_output[0])
   

class TestExpressionProduction(unittest.TestCase):

    def test1_14_test_single_brackets(self):
        _input = "[+ 1 2]"
        expected_output = (['[','+',1,2,']'], 3) # return (tree, result)
        actual_output = parse_line(_input)
        self.assertEqual(expected_output, actual_output)
    
    #TODO: add test nested brackets
    '''
    def test1_15_test_nested_brackets(self):
        _input = "[]"
        expected_output = (['[','[','+',3,2,']',']'], 5) # return (tree, result)
        actual_output = parse_line(_input)
        self.assertEqual(expected_output, actual_output)
    '''
    
if __name__ == '__main__':
    
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestScanner)
    module = __import__("test_driver")
    suite = unittest.TestLoader().loadTestsFromModule(module)

    print "Test Driver\n"
    unittest.TextTestRunner(verbosity=2).run(suite)
            
   





