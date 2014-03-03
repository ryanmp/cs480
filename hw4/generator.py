from scanner import *
from parser import *
from tree import *
import string
'''

if true
	then 7

: foo true if 7 endif ; foo	.

---

if true 
	then 3
else 
	4

[[if true 3 4]]

: foo true if 3 else 4 endif ; foo .

'''
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

def generator(x):
	ret = ''

	if len(invalid_types) > 0:
		return ret
	
	list_x = post_order_trav(x)
	isPrintStmt = False
	foundStrConst = False
	foundRealConst = False
	

	#print list_x
	isPrintStmt = isPrintOp(list_x)
	foundRealConst = detectFloat(list_x)
	
	list_x.reverse()

	to_transform = ['real_number','int_number','minus-binop','minus-unop','string','if_stmt']

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
		
	for i in list_x:
		if (type(i) == tuple):

			if i[0] in to_transform: #by type

				#if then
				if i[0] == 'if_stmt' and i[1] in ['if_then','if_then_else']:
					ret +=  ': foo '
				if i[0] == 'if_stmt' and i[1] in ['e','a']:
					ret +=  'endif ; foo '
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
				
			elif i[1] in direct_translations: #by value
				if (foundRealConst == True and isIntStackOp(i[1]) == True):
					ret += convertToStackFloat(i[1])
				else:
					ret += direct_translations[i[1]] + ' '
			
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
	for i in x:
		if (type(i) == tuple):
			if i[1] == 'stdout':
				return True
	return False

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


def generate_gforth_script(x):
	
	parser_out = parser(x)
	output = '\n' + chr(92) + ' input content: ' + str(x) + '\n' 
	
	if parser_out:	
		parse_tree = parser_out[1]
		
		#print_tree(parse_tree)

		type_errors = type_checker(parse_tree)
	
		for item in type_errors:
			output += item
		 
		output += chr(92) + ' -------------------------------' + '\n' 
	
		gforth_code = generator(parse_tree)
		output += gforth_code# + ' CR'
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
			gforth_code = generator(parse_tree)
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
		'[[if true 1]]',
		'[[if false 1 2]]',
		'[[+ [* 1 2] [- 3 4]]]',
		'[[+ 3 "test"]]',
		'[[+ [+ 1 "two"] "three"]]',
		'[[* 1 "2"]]',
		'[[sin "2"]]'
	]
	test(ts)

#test_generator()

	

