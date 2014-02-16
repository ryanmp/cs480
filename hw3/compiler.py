import sys
import string
from parser import *

files = []
options = []    

usage = """
Usage:
    compiler [option] [files] 
    option '-h' Display help
    option '-t' Display tokens
    option '-g' Display grammar
    option '-p' Display parse tree (default)
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
        print '\n',"parsing " + str(selected_file)
        print "-----------------------------"
        content = read_file(selected_file)
        print content
        
        print '\n',"output "
        print "-----------------------------"
        output = parse_file(content, options)
        
        if output:
            output = output.split(',')
            for item in output:
                print '\t',item
                
