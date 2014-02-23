import unittest
import random
from test_parse_tree import *
from parser_v2 import *   
    
if __name__ == '__main__':
    
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestScanner)
    module_parse_tree = __import__("test_parse_tree")
    
    suite_parse_tree = unittest.TestLoader().loadTestsFromModule(module_parse_tree)
    
    print "\nTest Driver"
    print "===========\n"
    
    print "Test Parse Tree"
    print "---------------"
    unittest.TextTestRunner(verbosity=2).run(suite_parse_tree)



