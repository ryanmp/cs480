from scanner import *
from parser import *
from tree import *




def generator(x):

	list_x = post_order_trav(x)
	list_x.reverse()
	ret = ''

	for i in list_x:

		if (type(i) == tuple):
			ret += i[1] + ' '



	return ret

def generate_gforth_script(x):
	parser_out = parser(x)
	parse_tree = parser_out[1]
	gforth_code = generator(parse_tree)
	output = gforth_code + '. CR bye'
	return output

def test_generator():
	t = '[[+ 2 [- 8 8]]]'
	scanner_out = scanner(t)
	
	parser_out = parser(t) # calls scanner internally
	
	parse_tree = parser_out[1]
	
	print_tree(parse_tree)
	
	gforth_code = generator(parse_tree)
	
	print gforth_code

