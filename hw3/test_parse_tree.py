import unittest
import random
from scanner import *
from parser import *
from tree import *

class TestExpressionProduction(unittest.TestCase):
    #@unittest.skip("skipping scanner tests for milestone 3")    
    def test_single_initial_production(self):
        _input = "[[ ]]"
         
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
        child3 = Node('[')
        child4 = Node(']')
        child1.add_child(child3)
        child1.add_child(child4)
             
        expected_output = get_tree_str(expected_tree,"")
          
        set_user_options(['-p'])
         
        output = parser(_input)
        actual_output = get_tree_str(output,"")
 
        print '\n'
        print_tree(output)
         
        self.assertEqual(expected_output, actual_output)
    
    #@unittest.skip("skipping scanner tests for milestone 3")
    def test_test_single_expression_ints(self):
        _input = "[[+ x y]]"
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
         
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
         
        child3 = Node('[')
        child4 = Node(']')
        child1.add_child(child3)
        child1.add_child(child4)
         
        child5 = Node('+')
        child6 = Node('x')
        child7 = Node('y')
        child3.add_child(child5)
        child3.add_child(child6)
        child3.add_child(child7)
         
 
        print '\n'
 
        print_tree(expected_tree)
        expected_output = get_tree_str(expected_tree,"")
          
        set_user_options(['-p'])
         
        output = parser(_input)
        actual_output = get_tree_str(output,"")
 
        print '\n'
        print_tree(output)
         
        self.assertEqual(expected_output, actual_output)
        #self.assertEqual(expected_output, output)
         
    #@unittest.skip("skipping scanner tests for milestone 3")
    def test_nested_brackets(self):
        _input = "[[[ ]]]"
         
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
        child3 = Node('[')
        child4 = Node(']')
        child1.add_child(child3)
        child1.add_child(child4)
        child5 = Node('[')
        child6 = Node(']')
        child3.add_child(child5)
        child3.add_child(child6)
         
        print '\n'
        print_tree(expected_tree)    
         
        expected_output = get_tree_str(expected_tree,"")
          
        set_user_options(['-p'])
         
        output = parser(_input)
         
        print '\n'
        print_tree(output)
         
        actual_output = get_tree_str(output,"")
 
        self.assertEqual(expected_output, actual_output)
        
    #@unittest.skip("skipping scanner tests for milestone 3")
    def test_inside_brackets_in_series(self):
        _input = "[[ ][ ]]"
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
        child3 = Node('[')
        child4 = Node(']')
        child1.add_child(child3)
        child1.add_child(child4)
        child5 = Node('[')
        child6 = Node(']')
        child1.add_child(child5)
        child1.add_child(child6)
         
        print '\n'
        print_tree(expected_tree)    
         
        expected_output = get_tree_str(expected_tree,"")
          
        #set_user_options(['-g'])
        set_user_options(['-p'])
         
        output = parser(_input)
         
        print '\n'
        print_tree(output)
         
        actual_output = get_tree_str(output,"")
 
        #self.assertEqual(expected_output, output)
        self.assertEqual(expected_output, actual_output)
    
    #@unittest.skip("skipping scanner tests for milestone 3")   
    def test_multiple_nested_brackets(self):
        _input = "[[[[ ]]]]"
        
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
        child3 = Node('[')
        child4 = Node(']')
        child1.add_child(child3)
        child1.add_child(child4)
        child5 = Node('[')
        child6 = Node(']')
        child3.add_child(child5)
        child3.add_child(child6)
        child7 = Node('[')
        child8 = Node(']')
        child5.add_child(child7)
        child5.add_child(child8)
        
        print '\n'
        print_tree(expected_tree)    
        
        expected_output = get_tree_str(expected_tree,"")
         
        set_user_options(['-p'])
        
        output = parser(_input)
        
        print '\n'
        print_tree(output)
        
        actual_output = get_tree_str(output,"")
    
        self.assertEqual(expected_output, actual_output)
    
    #@unittest.skip("skipping scanner tests for milestone 3")
    def test_if_statements_with_ids(self):
        _input = "[[if x y z]]"
        
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
         
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
         
        child3 = Node('[')
        child4 = Node(']')
        child1.add_child(child3)
        child1.add_child(child4)
         
        child5 = Node('if')
        child6 = Node('x')
        child7 = Node('y')
        child8 = Node('z')
        
        child3.add_child(child5)
        child3.add_child(child6)
        child3.add_child(child7)
        child3.add_child(child8)
        
        print '\n'
        print_tree(expected_tree)    
        
        expected_output = get_tree_str(expected_tree,"")
         
        set_user_options(['-p'])
        
        output = parser(_input)
        
        print '\n'
        print_tree(output)
        
        actual_output = get_tree_str(output,"")
    
        self.assertEqual(expected_output, actual_output)
    
    #@unittest.skip("skipping scanner tests for milestone 3")    
    def test_while_statements_with_ids(self):
        _input = "[[while x y z]]"
        
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
         
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
         
        child3 = Node('[')
        child4 = Node(']')
        child1.add_child(child3)
        child1.add_child(child4)
         
        child5 = Node('while')
        child6 = Node('x')
        child7 = Node('y')
        child8 = Node('z')
        
        child3.add_child(child5)
        child3.add_child(child6)
        child3.add_child(child7)
        child3.add_child(child8)
        
        print '\n'
        print_tree(expected_tree)    
        
        expected_output = get_tree_str(expected_tree,"")
         
        set_user_options(['-p'])
        
        output = parser(_input)
        
        print '\n'
        print_tree(output)
        
        actual_output = get_tree_str(output,"")
    
        self.assertEqual(expected_output, actual_output)
    
    #@unittest.skip("skipping scanner tests for milestone 3")
    def test_let_statements(self):
        _input = "[[let [[x bool]]]]"
        
        expected_tree = Node('T')
        child1 = Node('[')
        child2 = Node(']')
         
        expected_tree.add_child(child1)
        expected_tree.add_child(child2)
         
        child3 = Node('[')
        child4 = Node(']')
        
        child1.add_child(child3)
        child1.add_child(child4)
         
        child5 = Node('let')
        child6 = Node('[')
        child7 = Node(']')
    
        child3.add_child(child5)
        child3.add_child(child6)
        child3.add_child(child7)
        
        child8 = Node('[')
        child9 = Node(']')
            
        child6.add_child(child8)
        child6.add_child(child9)
        
        child10 = Node('x')
        child11 = Node('bool')
        
        child8.add_child(child10)
        child8.add_child(child11)
        
        print '\n'
        print_tree(expected_tree)    
        
        expected_output = get_tree_str(expected_tree,"")
         
        set_user_options(['-p'])
        
        output = parser(_input)
        
        print '\n'
        print_tree(output)
        
        actual_output = get_tree_str(output,"")
    
        self.assertEqual(expected_output, actual_output)
        
        
    
    


   





