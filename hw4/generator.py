from scanner import *
from parser import *
from tree import *

def generator(x):
	list_x = post_order_trav(x)
	isPrintStmt = False
	foundStrConst = False
	foundRealConst = False
	
	ret = ''
	#print list_x
	isPrintStmt = isPrintOp(list_x)
	foundRealConst = detectFloat(list_x)
	
	list_x.reverse()

	to_transform = ['real_number','int_number','minus-binop','minus-unop','string']

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
	intStackOps = ['<','>','>=','<=','+','*','/','<>','negate']
	
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
		ret = 'type '
	else:
		if isRealConst == True:
			ret = 'f. '
		else:
			ret = '. '
	return ret 

def detectFloat(x):
	for i in x:
		if (type(i) == tuple):
			if i[0] == 'real_number':
				return True
	return False


def generate_gforth_script(x):
	parser_out = parser(x)
	parse_tree = parser_out[1]
	print_tree(parse_tree)
	gforth_code = generator(parse_tree)
	output = gforth_code + 'CR bye'
	return output


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
		'[[stdout [+ [sin 2] [cos 1.2]]]]'

	]
	test(ts)

test_generator()

	

