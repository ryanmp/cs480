from scanner import *
from tree import *

user_options = []

'''
Description:

the next 19 functions define the grammar for IBTL
blank lines separate production rules
'''

def T(x):
	if (len(x) > 2):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			ret = S(x[1:-1])
			if (ret != None):
				new_node = Node("T->[S]")
				new_node.add_child(ret[1])
				return 'T->[S],' + ret[0], new_node

def S(x):
	if (len(x) == 2):
		if (x[0][0] == 'bracket-l' and x[1][0] == 'bracket-r'):
			return 'S->[ ]', Node("S->[ ]")

	if (len(x) >= 2):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			ret = S(x[1:-1])
			if (ret != None):
				new_node = Node("S->[S]")
				new_node.add_child(ret[1])
				return 'S->[S],' + ret[0], new_node

	if (len(x) >= 2):
		for i in range(1,len(x)-1):
			ret1 = S(x[i:])
			ret2 = S(x[:i])
			if (ret1 != None and ret2 != None):
				new_node = Node("S -> SS")
				new_node.add_child(ret1[1])
				new_node.add_child(ret2[1])
				return 'S -> SS,' + ret1[0] + ret2[0], new_node

	if (len(x) > 0):
		ret = expr(x)
		if ret != None:
			new_node = Node("S -> expr")
			new_node.add_child(ret[1])
			return 'S->expr,' + ret[0], new_node

def expr(x):
	ret = oper(x)
	if ret != None:
		new_node = Node("expr->oper")
		new_node.add_child(ret[1])
		return 'expr->oper,' + ret[0], new_node

	ret = stmts(x)
	if ret != None:
		new_node = Node("expr->stmts")
		new_node.add_child(ret[1])
		return 'expr->stmts,' + ret[0], new_node

def oper(x):
	if len(x) >= 5:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):

			if x[1][0] == 'assignment_op':
				ret1 = name([x[2]]) 
				ret2 = oper(x[3:-1])
				if (ret1 != None and ret2 != None):
					new_node = Node(('assignment_op','start'))
					oper_node = Node(('assignment_op','end'))
					new_node.add_child(oper_node)
					new_node.add_child(ret1[1])
					new_node.add_child(ret2[1])
					return 'oper->[:= name oper],' + ret1[0] + ret2[0], new_node

			ret1 = binops([x[1]])
			y = x[2:-1]
			for i in range(1,len(y)):
				ret2 = oper(y[i:])
				ret3 = oper(y[:i])
				if (ret1 != None and ret2 != None and ret3 != None):
					new_node = Node("oper->[binops oper oper]")
					new_node.add_child(ret1[1])
					new_node.add_child(ret2[1])
					new_node.add_child(ret3[1])
					return 'oper->[binops oper oper],' + ret1[0] + ret2[0] + ret3[0], new_node

	if len(x) >= 3:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			# handles the weird special case of proftest4.in and splitting a negative
			if x[1][0] in ['int_number','real_number']:
				if x[2][0] == 'bracket-r':
					if (x[1][1][0] == '-'):
						new_node = Node("oper->[unops oper]")
						new_node1 = Node(('minus-unop','-'))
						new_node2 = Node((str(x[1][0]),str(x[1][1][1:])))
						new_node.add_child(new_node1)
						new_node.add_child(new_node2)
						return ' ', new_node
			ret1 = unops([x[1]])
			ret2 = oper(x[2:-1]) # fixed problem case: '[[ sin [+ 1 2] ]]'
			if (ret1 != None and ret2 != None):
				new_node = Node("oper->[unops oper]")
				new_node.add_child(ret1[1])
				new_node.add_child(ret2[1])
				return 'oper->[unops oper],' + ret1[0] + ret2[0], new_node

	ret = constants(x)
	if ret != None:
		new_node = Node("oper->constants")
		new_node.add_child(ret[1])
		return 'oper->constants,' + ret[0], new_node

	ret = name(x)
	if ret != None:
		new_node = Node("oper->name")
		new_node.add_child(ret[1])
		return 'oper->name,' + ret[0], new_node


def binops(x):
	if x[0][0] in ['arithmatic_op','exponent_op','relational_op','log_op']:
		new_node = Node(x[0])
		return 'binops->'+x[0][1]+',', new_node
	if x[0][0] == 'minus-sign':
		new_node = Node(('minus-binop','-'))
		return 'binops->'+x[0][1]+',', new_node

		
# disambiguates 'minus-sign'
def unops(x):
	if x[0][0] in ['trig_op','log_op']:
		new_node = Node(x[0])
		return 'unops->'+x[0][1]+',', new_node
	if x[0][0] == 'minus-sign':
		new_node = Node(('minus-unop','-'))
		return 'unops->'+x[0][1]+',', new_node

def constants(x):
	ret = strings(x)
	if ret != None:
		new_node = Node("constants->strings")
		new_node.add_child(ret[1])
		return 'constants->strings,' + ret[0], new_node

	ret = ints(x)
	if ret != None:
		new_node = Node("constants->ints")
		new_node.add_child(ret[1])
		return 'constants->ints,' + ret[0], new_node

	ret = floats(x)
	if ret != None:
		new_node = Node("constants->floats")
		new_node.add_child(ret[1])
		return 'constants->floats,' + ret[0], new_node

	ret = bools(x)
	if ret != None:
		new_node = Node("constants->bools")
		new_node.add_child(ret[1])
		return 'constants->bools,' + ret[0], new_node

def strings(x):
	if (len(x) == 1):
		if x[0][0] == 'string':
			new_node = Node(x[0])
			return 'strings->STRINGS', new_node

def name(x):
	if (len(x) == 1):
		if x[0][0] == 'ID':
			new_node = Node(x[0])
			return 'name->NAME,', new_node

def ints(x):
	if (len(x) == 1):
		if x[0][0] == 'int_number':
			new_node = Node(x[0])
			return 'ints->INTS,', new_node

def floats(x):
	if (len(x) == 1):
		if x[0][0] == 'real_number':
			new_node = Node(x[0])
			return 'floats->FLOATS', new_node

def bools(x):
	if (len(x) == 1):
		if x[0][0] == 'bool_const':
			new_node = Node(x[0])
			return 'bool->BOOL_', new_node

def stmts(x):
	ret = ifstmts(x)
	if ret != None: 
		new_node = Node("stmts->ifstmts")
		new_node.add_child(ret[1])
		return 'stmts->ifstmts,' + ret[0], new_node

	ret = whilestmts(x)
	if ret != None:
		new_node = Node("stmts->whilestmts")
		new_node.add_child(ret[1])
		return 'stmts->whilestmts,' + ret[0], new_node

	ret = letstmts(x)
	if ret != None:
		new_node = Node("stmts->letstmts")
		new_node.add_child(ret[1])
		return 'stmts->letstmts,' + ret[0], new_node

	ret = printstmts(x)
	if ret != None:
		new_node = Node("stmts->printstmts")
		new_node.add_child(ret[1])
		return 'stmts->printstmts,' + ret[0], new_node

def printstmts(x):
	if (len(x) >= 4):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if x[1][0] == 'keyword' and x[1][1] =='stdout':
				ret = oper(x[2:-1])
				if ret != None:
					#new_node = Node("printstmts->[stdout oper]")
					#new_node.add_child(ret[1])
					
					#new_node = Node("printstmts->[stdout oper]")
					
					new_node = Node(('printstmts','start'))
					start_node = Node(('printstmts','end'))
					new_node.add_child(start_node)
					
					
					new_node_token = Node(x[1])
					
					new_node.add_child(new_node_token)
					new_node.add_child(ret[1])
					
					return 'printstmts->[stdout oper],' + ret[0], new_node

def ifstmts(x):

	if len(x) >= 5:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if (x[1][0] == 'keyword' and x[1][1] == 'if'):
				
				if (len(x) >= 6): #if then else
					for i in range(3,len(x)):
						for j in range(i,len(x)):
							ret1 = expr(x[2:i]) 
							ret2 = expr(x[i:j])
							ret3 = expr(x[j:-1])
							if (ret1 != None and ret2 != None and ret3 != None):
								new_node = Node(('if_stmt','if_then_else'))
								tmp_node = Node(('if_stmt','a'))
								new_node.add_child(tmp_node)
								new_node.add_child(ret3[1])
								tmp_node = Node(('if_stmt','b'))
								new_node.add_child(tmp_node)
								new_node.add_child(ret2[1])
								tmp_node = Node(('if_stmt','c'))
								new_node.add_child(tmp_node)
								new_node.add_child(ret1[1])
								tmp_node = Node(('if_stmt','d'))
								new_node.add_child(tmp_node)
								return 'ifstmts->[if expr expr expr],' + ret1[0] + ret2[0] + ret3[0], new_node

				if (len(x) >= 5): #if then
					for i in range(3,len(x)):
						ret1 = expr(x[2:i])
						ret2 = expr(x[i:-1])
						if (ret1 != None and ret2 != None):
							new_node = Node(('if_stmt','if_then'))
							tmp_node = Node(('if_stmt','e'))
							new_node.add_child(tmp_node)
							new_node.add_child(ret2[1])
							tmp_node = Node(('if_stmt','f'))
							new_node.add_child(tmp_node)
							new_node.add_child(ret1[1])
							tmp_node = Node(('if_stmt','g'))
							new_node.add_child(tmp_node)
							return 'ifstmts->[if expr expr],' + ret1[0] + ret2[0], new_node

def whilestmts(x):
	if len(x) >= 5:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if (x[1][0] == 'keyword' and x[1][1] == 'while'):
				y = x[2:-1]
				for i in range(0,len(y)):
					ret1 = expr(y[i:])
					ret2 = exprlist(y[:i])
					if (ret1 != None and ret2 != None):
						#new_node = Node("whilestmts->[while expr exprlist]")
						new_node = Node(("whilestmts",'start'))
						end_node = Node(("whilestmts",'end'))
						new_node.add_child(end_node)
						new_node.add_child(ret2[1])
						new_node.add_child(ret1[1])
						return 'whilestmts->[while expr exprlist],' + ret1[0] + ret2[0], new_node

def exprlist(x):
	ret1 = expr(x)
	if ret1 != None:
		new_node = Node("exprlist->expr")
		new_node.add_child(ret1[1])
		return 'exprlist->expr,' + ret1[0], new_node

	for i in range(0,len(x)):
		ret1 = expr(x[i:])
		ret2 = exprlist(x[:i])
		if (ret1 != None and ret2 != None):
			new_node = Node("exprlist->expr exprlist")
			new_node.add_child(ret1[1])
			new_node.add_child(ret2[1])
			return 'exprlist->expr exprlist,' + ret1[0] + ret2[0], new_node


def letstmts(x):
	if (len(x) >= 6):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if (x[1][0] == 'keyword' and x[1][1] == 'let'):
				if (x[2][0] == 'bracket-l' and x[-2][0] == 'bracket-r'):
					ret1 = varlist(x[3:-2])
					if (ret1 != None):
						new_node = Node('')
						new_node.add_child(ret1[1])
						return 'letstmts->[let [varlist]],' + ret1[0], new_node

def varlist(x):
	if (len(x) >= 4):
		if (x[0][0] == 'bracket-l' and x[3][0] == 'bracket-r'):
			if (len(x) == 4):
				ret1 = name([x[1]])
				ret2 = _type([x[2]])
				if (ret1 != None and ret2 != None):
					#new_node = Node(('new_var',[x[1],x[2]]))

					new_node = Node(('varlist','start'))
					start_node = Node(('varlist','end'))
					new_node.add_child(start_node)

					new_node.add_child(ret1[1])
					new_node.add_child(ret2[1])
					return 'varlist->[name type],' + ret1[0] + ret2[0], new_node

			if (len(x) >= 4):
				ret1 = name([x[1]])
				ret2 = _type([x[2]])
				ret3 = varlist(x[4:])
				if (ret1 != None and ret2 != None and ret3 != None):
					new_node = Node(('varlist','start'))
					start_node = Node(('varlist','end'))
					new_node.add_child(start_node)
					new_node.add_child(ret1[1])
					new_node.add_child(ret2[1])
					new_node.add_child(ret3[1])
					return 'varlist->[name type] varlist,' + ret1[0] + ret2[0] + ret3[0], new_node

def _type(x):
	if x[0][0] == 'keyword':
		if x[0][1] in ['bool','int','real', 'string']:
			new_node = Node(x[0])
			#new_node = Node('')
			return 'type->'+x[0][1]+',',new_node

'''
end of grammar... 
'''

def parse_file(file_content, uoptions):
	for option in uoptions:
		user_options.append(option)
	output = parser(file_content)
	return output

def parser(x):
	scanner_out = scanner(x)
	if (scanner_out[1]):
		parser_in = scanner_out[0]
		parser_out = T(parser_in)
		return parser_out
	else:
		print chr(92) + " scanner_failed" 



