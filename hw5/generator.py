from scanner import *
from parser import *
from tree import *

import string
import os

invalid_types = []

def determine_invalid_type(node, parent):
	result = ''
	op_types = ['constants->floats', 'constants->ints','constants->bools']

	if node.children > 0:
		type_node = node.children[0]
		
		if type_node.data not in op_types:
			
			if type_node.children > 0:
				token_data = type_node.children[0].data
				if type(token_data) == tuple:
					result = chr(92) + " type error: expected a float or integer, but was given: '" + token_data[1] + "' of type " + token_data[0] + '\n'
	return result

def type_checker(x):
	out = []
	global invalid_types
	invalid_types = []
	
	ops = ['oper->[binops oper oper]', 'oper->[unops oper]']
	def inner(x):
		if (x != None):
			out.append(x.data)
			
			if (len(x.children) > 0):
				parent = x.data
				
				for node in x.children:				
					if (node != None):
						if node.data == "oper->constants":
							if parent in ops:
								result = determine_invalid_type(node,parent)
								if len(result) > 0:
									invalid_types.append(result)
						inner(node)
	inner(x)
	
	#for item in invalid_types:
	#	print item
		
	return invalid_types

def generator2(x):
	ret = ''

	if len(invalid_types) > 0:
		return ret
	
	list_x = post_order_trav(x)
	isPrintStmt = False
	nestedIf = False
	
	foundStrConst = False
	foundRealConst = False
	
	#print list_x
	
	
	isPrintStmt = isPrintOp(list_x)
	foundRealConst = detectFloat(list_x)
	
	list_x.reverse()

	to_transform = ['real_number','int_number','minus-binop','minus-unop','string','if_stmt','ID','assignment_op','whilestmts']

	direct_translations = {
		#no changes
		'true':'true',
		'false':'false',
		'<':'<',
		'>':'>',
		'>=':'>=',
		'<=':'<=',
		'+':'+',
		'*':'*',
		'/':'/',
		'and':'and',
		'or':'or',
		'=':'=',

		#changes
		'!=':'<>',
		'%':'mod',
		'not':'negate',
		'tan':'ftan',
		'cos':'fcos',
		'sin':'fsin',
		'^':'f**',
		'stdout':''
	}

	idx = 0	# conditional anonymous function name indexer
	k = -1 # index to keep track of the items in list_x and use it to evaluate stdout if found in next token
	m = 0 # state to detect inner ifs
	var_definitions = {} #symbol table or list of ids with their types (id, type)
	setting_var = False #checking to see if var is being set or used

	
	for i in list_x:
		k += 1
		
		if (type(i) == tuple):
			if i[0] in to_transform: #by type

				#if then
				if i[0] == 'if_stmt' and i[1] in ['if_then','if_then_else']:
					idx += 1
					if nestedIf == False:
						ret +=  ': foo'+ str(idx)+' ' # the idx is so that we can have multiple foos that match for nested conditionals
						
					nestedIf = True
					m += 1
				
				if i[0] == 'if_stmt' and i[1] in ['e','a']:
					m -= 1
					
					if m <= 0:
						nestedIf = False
						ret +=  'endif ; foo'+ str(idx)+' '	
					else:
						ret += 'endif '
						idx -= 1
					
				if i[0] == 'if_stmt' and i[1] in ['f', 'c']:
					ret +=  'if '
				if i[0] == 'if_stmt' and i[1] in ['b']:
					ret +=  'else '

				if i[0] == 'int_number':
					ret += i[1] + ' '
					if foundRealConst == True:
						ret += 's>f '				

				if i[0] == 'minus-unop':
					if foundRealConst == True:
						ret += 'fnegate' + ' '
					else:
						ret += 'negate' + ' '

				if i[0] == 'minus-binop':
					if foundRealConst == True:
						ret += 'f-' + ' '
					else:
						ret += '-' + ' '

				if i[0] == 'real_number':
					foundRealConst = True
					if (i[1].find("E") != -1):
						tmp = i[1].replace("E", "e")
						ret += tmp + ' '
					elif (i[1].find("e") != -1):
						ret += i[1] + ' '
					else:	
						ret += i[1] + 'e' + ' '

				if i[0] == 'string':
					ret += "s\" " +i[1] +"\" "
					foundStrConst = True
					if (k > 0):
						if list_x[k+1][1] == 'stdout':
							ret += getgForthPrintOp(foundStrConst,foundRealConst)
				
				if (setting_var == False):
					if i[0] == 'ID':
						if (i[1] in var_definitions and list_x[k+1][1] == "stdout"):
							print_eval = getPrintVar(var_definitions, i[1])
							ret += i[1] + ' @ ' + print_eval + ' '
						elif (i[1] in var_definitions and var_definitions[i[1]] == 'real'):
							ret += i[1] + ' f@ '	
						elif (i[1] not in var_definitions):
							ret += i[1] + ' @ '	
						
				else:
					if i[0] == 'ID':
						# is it type float?
						# if so we have set the variable like this...
						if (i[1] in var_definitions and var_definitions[i[1]] == 'real'):
							ret += 'FVARIABLE'+' '+i[1]+' '+i[1] + ' f'
						else:
							ret += 'VARIABLE'+' '+i[1]+' '+i[1] + ' '
						
				if i[0] == 'assignment_op':
					if i[1] == 'start':
						setting_var = True
					if i[1] == 'end':
						setting_var = False
						ret += '! '

				if i[0] == 'whilestmts':
					if i[1] == 'start':
						ret += ": loop1 BEGIN "
					if i[1] == 'end':
						ret += "UNTIL ; loop1 "
	
			elif i[1] in direct_translations: #by value
				if (foundRealConst == True and isIntStackOp(i[1]) == True):
					ret += convertToStackFloat(i[1])
				else:
					ret += direct_translations[i[1]] + ' '
				
				if (k > 0 and k < len(list_x)-1):
					if list_x[k+1][1] == 'stdout':
						ret += getgForthPrintOp(False,foundRealConst)
			
			elif i[0] in ['keyword']:
				#detect let statements
				if (k > 0):
					if list_x[k+1][0] == 'ID':
						var_def = getIdAndType(list_x, k)
						if var_def:
							var_definitions[var_def[0]] = var_def[1]
						
			else: 
				print "error.. no gforth translation rule present for:",i," exiting..."
				return -1

	
	if isPrintStmt == True:
		ret += getgForthPrintOp(foundStrConst,foundRealConst)
	
	return ret

def isIntStackOp(x):
	intStackOps = ['<','>','>=','<=','+','*','/','<>','negate','-']
	
	if x in intStackOps:
		return True
	else:
		return False

def convertToStackFloat(x):	
	ret = ''
	ret += 'f' + x + ' '	
	return ret 

def isPrintOp(x):
	y = []
	for i in x:
		if (type(i) == tuple):
			y.append(i)

	if len(y) > 0:
		y.reverse()
		if y[0][1] == 'stdout':
			return True
		
	return False


def getIdAndType(list_x, k):
	var_def = ()
	valid_types = ['real','int','string']
	
	if (type(list_x[k]) == tuple and type(list_x[k+1]) == tuple):
		if list_x[k][1] not in valid_types:
			return var_def
	
		type_str = list_x[k][1]
		id_str = list_x[k+1][1]
		var_def = (id_str,type_str)

	return var_def

# determine proper print op for a given id in a symbol table or variable definitions list
def getPrintVar(var_list, id):
	tmp_type = var_list[id]
	if tmp_type == 'int':
		print_eval = getgForthPrintOp(False, False)
	elif tmp_type == 'real':
		print_eval = getgForthPrintOp(False, True)
	elif tmp_type == 'string':
		print_eval = getgForthPrintOp(True, False)
	
	return print_eval
	

def getgForthPrintOp(isStrConst,isRealConst):
	if isStrConst == True:
		ret = 'type CR'
	else:
		if isRealConst == True:
			ret = 'f. CR'
		else:
			ret = '. CR'
	return ret 

def detectFloat(x):
	for i in x:
		if (type(i) == tuple):
			if i[0] == 'real_number':
				return True
	return False


# just another function for demoing
def generator(x):
	parser_out = parser(x)
	output = ""
	#output = '\n' + chr(92) + ' input content: ' + str(x) + '\n' 
	
	if parser_out:	
		parse_tree = parser_out[1]
		
		#print_tree(parse_tree)

		type_errors = type_checker(parse_tree)
	
		for item in type_errors:
			output += item
		 
		#output += chr(92) + ' -------------------------------' + '\n' 
	
		gforth_code = generator2(parse_tree)
		output += " " + gforth_code# + ' CR'
		print output

	else:
		output += chr(92) + ' parsing failed on: ' + x
		print output + '\n' 


def generate_gforth_script(x):
	
	parser_out = parser(x)
	output = ""
	#output = '\n' + chr(92) + ' input content: ' + str(x) + '\n' 
	
	if parser_out:	
		parse_tree = parser_out[1]
		
		print_tree(parse_tree)

		type_errors = type_checker(parse_tree)
	
		for item in type_errors:
			output += item
		 
		#output += chr(92) + ' -------------------------------' + '\n' 
	
		gforth_code = generator2(parse_tree)
		#print gforth_code
		output += str(gforth_code) + ' '
		return output
	else:
		output += chr(92) + ' parsing failed on: ' + x
		return output + '\n'



def test(ts):
	test_results = []
	for t in ts:
		scanner_out = scanner(t)
		parser_out = parser(t)

		if parser_out:
			parse_tree = parser_out[1]
			#print_tree(parse_tree)
			gforth_code = generator2(parse_tree)
			print t, '  ->  ', gforth_code
		else:
			print 'parsing failed on: ',t


def test_generator():
	ts = [

		'[[+ 2 [- 8 8]]]',
		'[[> 1 2]]',
		'[[<= .02 1.102]]',
		'[[!= 4 2][= 1 1]]',
		'[[and true false]]',
		'[[not true]]',
		'[[^ 1e3 2e1]]',
		'[[sin 2][cos 1.2]]',
		'[[- 2]]',
		'[[* 1.2E-1 1.5e2]]',
		'[[+ 2 1.0]]',
		'[[- 1.0]]',
		'[[stdout [/ 1 2]]]',
		'[[stdout [+ 2 1.0]]]',
		'[[stdout "hello world"]]',
		'[[stdout 1234]]',
		'[[stdout 12.34]]',
		'[[stdout [+ 1 2]]]',
		'[[stdout [+ 2 [- 8 8]]]]',
		'[[stdout [* 1.2E-1 1.5e2]]]',
		'[[stdout [+ [sin 2] [cos 1.2]]]]',
		'[[if true [if true true] [* 1 3]]]',
		'[[+ [* 1 2] [- 3 4]]]',
		'[[+ 3 "test"]]',
		'[[+ [+ 1 "two"] "three"]]',
		'[[* 1 "2"]]',
		'[[sin "2"]]',
		'[[if true [stdout "true"]]]',
		'[[if false [stdout [+ 1 2]]]]',
		'[[if false [stdout [+ 1 [- 1 2.0]]]]]',
		'[[if true 1 2]]',
		'[[if true [stdout "true"] [stdout "false"]]]',
		'[[if true [if false false] [if true true]]]',
		'[[if true true] [if false false]]',
		'[[if true [stdout "true"]] [if false [stdout "false"]]]',
		'[[:= x 2][stdout[+ 7 x]]]',
		'[[let [[x int]]] [:= x 10] [stdout x]]',
		'[[let [[y real]]] [:= y 1.0] [stdout y]]',
		'[[let [[z string]]] [:= z "hello world"] [stdout z]]'
		#'[ [:= x 5] [while [< x 1][stdout "."][:= x [+ x 1]] ]]'
	]

	ts2 = [
		'[[:= x 2][stdout[+ 7 x]]]',
		#'[[let [[x int]]] [:= x 10] [stdout x]]',
		'[[let [[y real]]] [:= y 1.0] [stdout y]]'
		#'[[let [[z string]]] [:= z "hello world"] [stdout z]]'
	]

	test(ts2)

test_generator()

	

