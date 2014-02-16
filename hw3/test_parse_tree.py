import unittest
import random
from scanner import *
from parser import *
from tree import *

class TestExpressionProduction(unittest.TestCase):

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
    
    
    def test_test_single_expression(self):
        _input = "[[+ 1 2]]"
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
        child6 = Node('1')
        child7 = Node('2')
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
        


    


   





