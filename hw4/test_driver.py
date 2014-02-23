import unittest
import random
from test_parse_tree import *
from parser import *   
    
if __name__ == '__main__':
    
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestScanner)
    #module_parse_tree = __import__("test_parse_tree")
    module_gforth_out = __import__("test_gforth_out")
    #suite_parse_tree = unittest.TestLoader().loadTestsFromModule(module_parse_tree)
    suite = unittest.TestLoader().loadTestsFromModule(module_gforth_out)
    
    print "\nTest Driver"
    print "===========\n"
    
    print "Test gforth Code"
    print "---------------"
    #unittest.TextTestRunner(verbosity=2).run(suite_parse_tree)
    unittest.TextTestRunner(verbosity=2).run(suite)



