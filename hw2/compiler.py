'''
Created on Jan 29, 2014

@author: luisramg
'''
from scanner_ryan import *
import sys

if __name__ == '__main__':
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    if len(sys.argv) < 1:
        print "Usage: compiler stutest.in"
        sys.exit(2)
    
    input_file = sys.argv[1]
    print "scanning " + str(input_file)
    tokens = scan_file(input_file)
    i = 0
    for token_line in tokens:
    	i+=1
    	print "\nTokens in Line " + str(i) + ":\n"
    	if len(token_line[0])==0:
    		print '\t No tokens or comment line found'
    		
    	for token in token_line[0]:
    		print '\t' + str(token)
    		
