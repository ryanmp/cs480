from treelib import Tree, Node
from scanner import *
import sys

scanner_in = "[[+ x 5]]"
scanner_out = scanner(scanner_in)[0] # just the tokens
parser_in = [i[0] for i in scanner_out] # just the token types

history = []
derivation = []

def T(x,d):
	if (len(x) >= 2):
		if (x[0] == 'bracket-l' and x[-1] == 'bracket-r'):
			return 'T->[S],' + S(x[1:-1],d)
		
def S(x,d):
	if (len(x) == 2):
		if (x[0] == 'bracket-l' and x[1] == 'bracket-r'):
			return 'S->[ ]'
	if (len(x) >= 2):
		if (x[0] == 'bracket-l' and x[-1] == 'bracket-r'):
			return 'S->[S],' + S(x[1:-1],d)
	if (len(x) >= 2):
		for i in range(1,len(x)-1):
			return 'S -> SS,' + S(x[i:],d) + S(x[:i],d)
	if (len(x) > 0):
		return 'S->expr,' + expr(x,d)
	print "f-word!"


def expr(x,d): 
	#d = oper(x,d)
	#d = stmts(x,d)

	return 'expr'
'''
def oper(x,d):
	history.append("<oper>")
	#if (x[0] == 'bracket-l' and x[-1] == 'bracket-r'):
	#	if x[1] == 'assignment_op' and x[2] == 'ID' and x[3] 
	#		name(x[2]) 
	#		oper(x[3]) #??
	#
	# 3 rules still need implementing

	d = constants(x,d)
	d = name(x,d)

def binops(x,d):
	history.append("<binops>")

def constants(x,d):
	history.append("<constants>")
	d = strings(x,d)
	d = ints(x,d)
	d = floats(x,d)

def strings(x,d):
	history.append("<strings>")

def name(x,d):
	history.append("name")

def ints(x,d):
	history.append("ints")

def floats(x,d):
	history.append("floats")

def stmts(x,d):
	history.append("stmts")
	d = ifstmts(x,d)
	d = whilestmts(x,d)
	d = letstmts(x,d)
	d = printstmts(x,d)

def printstmts(x,d):
	history.append("printstmts")
	# to implement

def ifstmts(x,d):
	history.append("ifstmts")
	# to implement

def whilestmts(x,d):
	history.append("whilestmts")
	# to implement

def exprlist(x,d):
	history.append("exprlist")
	# to implement

def letstmts(x,d):
	history.append("letstmts")
	# to implement

def varlist(x):
	history.append("varlist")
	# to implement

def type(x):
	history.append("type")
	if x in ['bool_const','int_number','real_number', 'string']:
		d.append('x')
'''



def parser(x,derivation):
	scanner_out = scanner(x)[0] # just the tokens
	parser_in = [i[0] for i in scanner_out] # just the token types
	print T(parser_in,derivation)
	

#run = T(parser_in)
#print history
