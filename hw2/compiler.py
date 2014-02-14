from parser import *
import sys

if __name__ == '__main__':
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    if len(sys.argv) < 1:
        print "Usage: compiler stutest.in"
        sys.exit(2)
    
    input_file = sys.argv[1]
    print "parsing " + str(input_file)
    parse_tree = parse_file(input_file)
    print parse_tree
    