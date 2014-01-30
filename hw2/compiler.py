'''
Created on Jan 29, 2014

@author: luisramg
'''
from scanner_ryan import *
import sys

if __name__ == '__main__':
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    if len(sys.argv) < 1:
        print "Usage compiler stutest.in"
        sys.exit(2)
    
    input_file = sys.argv[1]
    print "scanning " + str(input_file)
    tokens = scan_file(input_file)
    for token in tokens:
        print token