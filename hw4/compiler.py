import sys
import string
import os.path

from parser import *
from tree import *
from generator import *
files = []
options = []    

usage = """
Usage:
    compiler [option] [files] 
    option '-g' Display grammar only
    option '-t' Display parse tree only
    option '-b' Display both parse tree and grammar
    option '-f' Display gforth code only

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


def print_verbose(selected_file,content):
	print '\n',"input: parsing " + str(selected_file)
	print "-----------------------------"
	print content
	print '\n',"output: "
	print "-----------------------------"


if __name__ == '__main__':
	if len(sys.argv) < 1:
		print usage
		sys.exit(2)
        
	global options
	prepare_files(sys.argv)
	gfcode = ''
    
   
	for selected_file in files:
		content = read_file(selected_file)
		
		if '-f' in options:
			# if multiple files, combine each script into one fs file
			# for better output
			gfcode = '\n' + chr(92) + ' input file: ' + str(selected_file)
			#gfcode += 's\" ' + str(selected_file) + '\" type CR'
			gfcode += generate_gforth_script(content)
			print gfcode	
	

		else:
			print_verbose(selected_file,content)
			output = parse_file(content, options)
		            
			if output:
				if '-t' in options:
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

			else:
				print " Error: Syntax error\n"
			
	if '-f' in options:
		print ' CR bye'
		
            
