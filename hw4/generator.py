from scanner import *
from parser import *
from tree import *

def generator(x):

	list_x = post_order_trav(x)
	list_x.reverse()
	ret = ''

	to_transform = ['real_number','int_number']

	direct_translations = {
		#no changes
		'true':'true',
		'false':'false',
		'<':'<',
		'>':'>',
		'>=':'>=',
		'<=':'<=',
		'+':'+',
		'-':'-',
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
		'^':'f**'
	}

	for i in list_x:
		if (type(i) == tuple):

			if i[0] in to_transform: #by type

				if i[0] == 'int_number':
					ret += i[1] + ' '
				# "do the transforms here"
				# such as 5E0 -> 5e0
				# this section will have a number of cases

			elif i[1] in direct_translations: #by value
				ret += direct_translations[i[1]] + ' '

			else: 
				print "error.. no gforth translation rule present for:",i," exiting..."
				return -1

	return ret


def generate_gforth_script(x):
	parser_out = parser(x)
	parse_tree = parser_out[1]
	gforth_code = generator(parse_tree)
	output = gforth_code + '. CR bye'
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
		'[[sin 2][cos 1.2]]'
	]
	test(ts)

test_generator()

	

