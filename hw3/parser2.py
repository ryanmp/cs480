from treelib import Tree, Node
from scanner import *
import sys

t1 = "[[stdout x]]"

derivation = []

def T(x,d):
	if (len(x) > 2):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			
			ret = S(x[1:-1],d)
			if (ret != None): return 'T->[S],' + ret
		
def S(x,d):
	if (len(x) == 2):
		if (x[0][0] == 'bracket-l' and x[1][0] == 'bracket-r'):
			return 'S->[ ]'
	if (len(x) >= 2):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			
			ret = S(x[1:-1],d)
			if (ret != None): return 'S->[S],' + ret

	if (len(x) >= 2):
		for i in range(1,len(x)-1):

			ret1 = S(x[i:],d)
			ret2 = S(x[:i],d)
			if (ret1 != None and ret2 != None):
				return 'S -> SS,' + ret1 + ret2

	if (len(x) > 0):

		ret = expr(x,d)
		if ret != None: return 'S->expr,' + ret



def expr(x,d): 
	#return 'expr->oper,' + oper(x,d)

	ret = stmts(x,d)
	if ret != None: return 'expr->stmts,' + ret

def oper(x,d):
	#if (x[0] == 'bracket-l' and x[-1] == 'bracket-r'):
	#	if x[1] == 'assignment_op' and x[2] == 'ID' and x[3] 
	#		name(x[2]) 
	#		oper(x[3]) #??
	#
	# 3 rules still need implementing

	#return 'oper'
	print "here"
	y = 1

	ret = constants(x,d)
	if ret != None: return 'oper->constants,' + ret

	ret = name(x,d)
	if ret != None: return 'oper->name,' + ret

'''
def binops(x,d):
	history.append("<binops>")
'''
def constants(x,d):

	ret = strings(x,d)
	if ret != None: return 'constants->strings,' + ret

	ret = ints(x,d)
	if ret != None: return 'constants->ints,' + ret

	ret = floats(x,d)
	if ret != None: return 'constants->floats,' + ret

def strings(x,d):
	history.append("<strings>")

def name(x,d):
	if x[0][0] == 'ID': return 'NAME'

def ints(x,d):
	if x[0][0] == 'int_number': return 'INTS'

def floats(x,d):
	if x[0][0] == 'real_number': return 'FLOATS'


def stmts(x,d):

	#ret = ifstmts(x,d)
	#if ret != None: return 'stmts -> ifstmts,' + ret

	#ret = whilestmts(x,d)
	#if ret != None: return 'stmts -> whilestmts,' + ret

	#ret = letstmts(x,d)
	#if ret != None: return 'stmts -> letstmts,' + ret

	ret = printstmts(x,d)
	if ret != None: return 'stmts->printstmts,' + ret

def printstmts(x,d):
	if (len(x) >= 4):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if x[1][0] == 'keyword' and x[1][1] =='stdout':
				ret = oper(x[2:-1],d)
				if ret != None: return 'printstmts->[stdout oper],' + ret

def ifstmts(x,d):
	if (len(x) >= 2):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			# to implement
			print '2'

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



def parser(x):
	print "scanning the following:"
	print x, '\n'
	scanner_out = scanner(x)

	print "list of tokens:"
	print scanner_out[0], '\n'

	if (scanner_out[1]):
		print "parsing..."
		parser_in = scanner_out[0]
		print T(parser_in,derivation)
	else:
		print "didn't scan properly. exiting!"

	

#run = T(parser_in)
#print history
