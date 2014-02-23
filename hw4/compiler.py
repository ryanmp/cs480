import sys
import string
from parser_v2 import *
from tree import *
files = []
options = []    

usage = """
Usage:
    compiler [option] [files] 
    option '-g' Display grammar only
    option '-t' Display parse tree only
    option '-b' Display both parse tree and grammar

"""

def prepare_files(argv):
    global options
    for arg in argv:
        if arg[0] == '-':
            #collect user options
            options.append(arg)
        elif arg != argv[0]:
            #collect files
            files.append(arg)

def read_file(input_file):        
    content = ""
    f = open(input_file)
    
    lines_raw = f.readlines()
    for i in range(0,len(lines_raw)):
        content+=lines_raw[i]
    
    return content    

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print usage
        sys.exit(2)
    
    prepare_files(sys.argv)
    
    for selected_file in files:
        print '\n',"input: parsing " + str(selected_file)
        print "-----------------------------"
        content = read_file(selected_file)
        print content
        
        print '\n',"output: "
        print "-----------------------------"
        output = parse_file(content, options)
            
        if output:
            if '-t' in options:
                #print_tree(output)
                print_tree(output[1])
            if '-g' in options:
                output = output[0].split(',')
                for item in output:
                    print '\t',item
            if '-b' in options:
                print "parse tree:\n"
                print_tree(output[1])
                print "\ngrammar derivation:\n"
                output = output[0].split(',')
                for item in output:
                    print '\t',item
            if '-g' in options:
                print "gforth code:\n"
        else:
            print "Error: Sintax error\n"
