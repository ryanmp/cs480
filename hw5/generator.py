from scanner import *
from parser import *
from tree import *

import string
import os

semantic_errors = []

def determine_invalid_type(node, parent):
	result = ''
	op_types = ['constants->floats', 'constants->ints','constants->bools']

	if node.children > 0:
		type_node = node.children[0]
		
		if type_node.data not in op_types:
			
			if type_node.children > 0:
				token_data = type_node.children[0].data
				if type(token_data) == tuple:
					result = "\n\ttype error: expected a float or integer, but was given: '" + token_data[1] + "' of type " + token_data[0]
	return result

def type_checker(x):
	out = []
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

	semantic_errors = type_checker(x)

	list_x = post_order_trav(x)
	isPrintStmt = False
	nestedIf = False
	
	foundStrConst = False
	foundRealConst = False
	
	#print list_x
	
	
	isPrintStmt = isPrintOp(list_x)
	foundRealConst = detectFloat(list_x)
	
	list_x.reverse()

	to_transform = ['real_number','int_number','minus-binop','minus-unop','string','if_stmt','ID','assignment_op','whilestmts','varlist','keyword']

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
	
	int_float_only_ops = ['*','-','/','%','>','<','>=','<=','and','or','not','sin','cos','tan','^']


	f_idx = 0	# conditional anonymous function name indexer
	k = -1 # index to keep track of the items in list_x and use it to evaluate stdout if found in next token
	m = 0 # state to detect inner ifs
	
	setting_var = False #checking to see if var is being set
	in_varlist = 0 #checking to see if var is being declared
	
	for idx, i in enumerate(list_x):

		k += 1
		
		if (type(i) == tuple):

			if i[0] in to_transform: #by type

				#if then
				if i[0] == 'if_stmt' and i[1] in ['if_then','if_then_else']:
					f_idx += 1
					if nestedIf == False:
						ret +=  ': foo'+ str(f_idx)+' ' # the idx is so that we can have multiple foos that match for nested conditionals
						
					nestedIf = True
					m += 1
				
				if i[0] == 'if_stmt' and i[1] in ['e','a']:
					m -= 1
					
					if m <= 0:
						nestedIf = False
						ret +=  'endif ; foo'+ str(f_idx)+' '	
					else:
						ret += 'endif '
					
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
				
				# start variable logic
				if (setting_var == False and in_varlist == False):
					if i[0] == 'ID':

						if ( len(list_x) > k+1 ): # to avoid error
							if (list_x[k+1][1] == "stdout"):

								print_eval = getPrintVar(i[1])
																
								if (symbol_table[i[1]] == 'real'):
									ret += i[1] + ' f@ ' + print_eval + ' '
								elif (symbol_table[i[1]] in ['int','string']):
									ret += i[1] + ' @ ' + print_eval + ' '								
								else:
									semantic_errors.append("\n\tUndefined variable: '" + i[1] + "' undeclared or referenced before assignment")
							else:
								if (symbol_table[i[1]] == 'real'):
									ret += i[1] + ' f@ ' 
								elif (symbol_table[i[1]] in ['int','string']): 
									ret += i[1] + ' @ '
						
									if (symbol_table[i[1]] == 'string' and list_x[k+1][1] in int_float_only_ops):
										semantic_errors.append("\n\ttype error: type of variable '" + i[1] + "' is not a valid type for '" + list_x[k+1][1] +"'")
																			 
								else:
									semantic_errors.append("\n\tUndefined variable: '" + i[1] + "' undeclared or referenced before assignment")
									print_error_messages(semantic_errors)
									return -1
									#ret += i[1] + ' ' #not semantically correct... but whatev
									

				elif (setting_var == False and in_varlist != 0):
					if i[0] == 'ID':
						symbol_table[i[1]] =  list_x[idx-1][1]
						if list_x[idx-1][1] == 'real':		
							ret += 'FVARIABLE ' + i[1] + ' '
						elif list_x[idx-1][1] in ['int','string']:	
							ret += 'VARIABLE ' + i[1] + ' '
						else:
							semantic_errors.append("\n\tUndefined variable: '" + i[1] + "' undeclared or referenced before assignment")
							
				elif (setting_var == True and in_varlist == 0):
					if i[0] == 'ID':

						type_id_in_symbol_table = symbol_table[i[1]] 
						type_id_in_assignment_op = list_x[k-1][0]
						 
						if is_assignment_invalid(type_id_in_symbol_table, type_id_in_assignment_op) == True:
							semantic_errors.append("\n\ttype error: '" + i[1] + "' assignment of the wrong type")
							
						if (symbol_table[i[1]] == 'real'):
							ret += i[1] + ' f! '
						elif (symbol_table[i[1]] in ['int','string']):
							ret += i[1] + ' ! '
						else:
							semantic_errors.append("\n\tUndefined variable: '" + i[1] + "' undeclared or referenced before assignment")
							print_error_messages(semantic_errors)
							#ret += i[1] + ' ' #not semantically correct... but whatev
							return -1

				#end variable logic
				
				if i[0] == 'assignment_op':
					if i[1] == 'start':
						setting_var = True
					if i[1] == 'end':
						setting_var = False
						#ret += '! '

				if i[0] == 'whilestmts':
					if i[1] == 'start':
						ret += ": loop1 BEGIN "
					if i[1] == 'end':
						ret += "UNTIL ; loop1 "

				if i[0] == 'varlist':
					if i[1] == 'start':
						in_varlist += 1
					if i[1] == 'end':
						in_varlist -= 1

	
			elif i[1] in direct_translations: #by value
				if (foundRealConst == True and isIntStackOp(i[1]) == True):
					ret += convertToStackFloat(i[1])
				else:
					ret += direct_translations[i[1]] + ' '
				
				if (k > 0 and k < len(list_x)-1):
					if list_x[k+1][1] == 'stdout':
						ret += getgForthPrintOp(False,foundRealConst)
			else: 
				print "error.. no gforth translation rule present for:",i," exiting..."
				return -1

	
	if isPrintStmt == True:
		ret += getgForthPrintOp(foundStrConst,foundRealConst)
	
	if len(semantic_errors) > 0:
		print_error_messages(semantic_errors)
	
	return ret

def is_assignment_invalid(type1, type2):
	if type1 == "real_number":
		type1 = "real"
	if type2 == "real_number":
		type2 = "real"
	if type1 == "int_number":
		type1 = "int"
	if type2 == "int_number":
		type2 = "int"
	
	if type1 != type2:
		return True
	else:
		return False
	
def print_error_messages(error_list):
	for item in error_list:
		print item

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
def getPrintVar(id):
	tmp_type = symbol_table[id]
	if tmp_type == 'int':
		print_eval = getgForthPrintOp(False, False)
	elif tmp_type == 'real':
		print_eval = getgForthPrintOp(False, True)
	elif tmp_type == 'string':
		print_eval = getgForthPrintOp(True, False)
	else:
		print_eval = ''
	return print_eval
	

def getgForthPrintOp(isStrConst,isRealConst):
	if isStrConst == True:
		ret = 'type CR '
	else:
		if isRealConst == True:
			ret = 'f. CR '
		else:
			ret = '. CR '
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
		
		#print_tree(parse_tree)

		type_errors = type_checker(parse_tree)
	
		for item in type_errors:
			output += item
		 
		#output += chr(92) + ' -------------------------------' + '\n' 
	
		gforth_code = generator2(parse_tree)

		if (gforth_code != -1):
			#print gforth_code
			output += str(gforth_code) + ' '
			return output
		else: 
			output += 'Semantic error. Exiting.'
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
		'[[if true [stdout "true"]]]',
		'[[if false [stdout [+ 1 2]]]]',
		'[[if false [stdout [+ 1 [- 1 2.0]]]]]',
		'[[if true 1 2]]',
		'[[if true [stdout "true"] [stdout "false"]]]',
		'[[if true [if false false] [if true true]]]',
		'[[if true true] [if false false]]',
		'[[if true [stdout "true"]] [if false [stdout "false"]]]',
		'[[:= under_score5x 2][stdout[+ 7 under_score5x]]]',
		'[[let [[x int]]] [:= x 10] [stdout x]]',
		'[[let [[y real]]] [:= y 1.0] [stdout y]]',
		'[[let [[z string]]] [:= z "hello world"] [stdout z]]'
		#'[ [:= x 5] [while [< x 1][stdout "."][:= x [+ x 1]] ]]'
	]

	# let's test varlist next...
	ts2 = [

		#'[[ [let [[x real]] ]  [:= x 1.1] [stdout x] ]]' 
		'[[ [let [[x real]]]  [:= x 1.1] [stdout x] ]]', 
		'[[let [[y real][x int]] ]]'

	]
	
	# semantic error cases:
	
	ts_invalid_id = [
		'[[let [[stdout int]]]]' 
	]
	
	ts_wrong_type = [
		'[[+ 3 "test"]]',
		'[[+ [+ 1 "two"] "three"]]',
		'[[* 1 "2"]]',
		'[[sin "2"]]',
		'[[let [[y string]]] [:= y "hi"][- 1 y]]'
	]
	
	ts_wrong_assignment = [
		'[[let [[y string]]] [:= y 23]]',
		'[[let [[y int]]] [:= y "hello"]]',
		'[[let [[y real]]] [:= y "hi"]]',
		'[[let [[y int]]] [:= y "hi"] [stdout y]]',
		
	]
	
	ts_undefined_var = [
		'[[stdout y]]',
		'[[if true [stdout x]]]',
		'[[+ 1 z]]',
		'[[- w]]',
		'[[:= x 2][stdout[+ 7 x]]]',
		'[[:= w z]]',
		'[[:= w "hello"]]'
	]
	
	test(ts_undefined_var)
	

#test_generator()

'''
VARIABLE x 0 x !

: loop1 BEGIN 
1 x @ + x ! 
x @ 5 > 
UNTIL ; loop1
x @ .

bye
'''

	

