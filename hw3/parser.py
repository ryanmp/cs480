from scanner import *
from tree import *

derivation = [] # an extra list to be used later
user_options = []

'''

info:

the next 19 functions define the grammar for IBTL
blank lines separate production rules

'''

def T(x,d):
	if (len(x) > 2):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			
			#create root node
			tree = Node('T')
			child1 = Node('[')
			child2 = Node(']')
			tree.add_child(child1)
			tree.add_child(child2)
			parent = child1#Node('')
			#parent = Node('')
			#parent = tree.get_child_at(0)
			ret = S(x[1:-1],d,tree,parent)
			if (ret != None):
				if '-p' in user_options: #display tree else display grammar productions
					return ret
				else:  
					return 'T->[S],' + ret
		
def S(x,d,tree,parent):
	if (len(x) == 2):
		if (x[0][0] == 'bracket-l' and x[1][0] == 'bracket-r'):
			if '-p' in user_options:
				child_1 = Node('[')
				child_2 = Node(']')
				# get immediate parent child
				#child1 = tree.get_child_at(0)
				level = tree.get_parent_depth(parent)
				if (level == 0):
					child1 = tree.get_child_at(0)
				else:
					child1 = tree.get_first_child_at_parent_level(parent,level)
							
				child1.add_child(child_1)
				child1.add_child(child_2)
				return tree
			else:
				return 'S->[ ]'

	if (len(x) >= 2):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			#parent = Node('')
			if '-p' in user_options: #display tree else display grammar productions
				child_1 = Node('[')
				child_2 = Node(']')
				# get immediate parent child
				
				if parent.depth > 0:
					child1 = tree.get_first_child_at_parent(parent)
				else:
					child1 = tree.get_child_at(0)
				
				child1.add_child(child_1)
				child1.add_child(child_2)
				#parent = child1
				parent = child1
			ret = S(x[1:-1],d,tree,parent)
			if (ret != None):
				if '-p' in user_options: #display tree else display grammar productions
					return ret
				else: 
					return 'S->[S],' + ret

	if (len(x) >= 2):
		for i in range(1,len(x)-1):
			ret1 = S(x[i:],d,tree,parent)
			ret2 = S(x[:i],d,tree,parent)
			if (ret1 != None and ret2 != None):
				# TODO: add parse tree logic
				return 'S -> SS,' + ret1 + ret2

	if (len(x) > 0):
		ret = expr(x,d,tree,parent)
		if ret != None:
			if '-p' in user_options: #display tree else display grammar productions
				return ret
			else: 
				return 'S->expr,' + ret

def expr(x,d,tree,parent): 
	ret = oper(x,d,tree,parent)
	if ret != None:
		if '-p' in user_options: #display tree else display grammar productions
			return ret
		else: 
			return 'expr->oper,' + ret

	ret = stmts(x,d)
	if ret != None:
		# TODO: add parse tree logic 
		return 'expr->stmts,' + ret

def oper(x,d,tree,parent):
	if len(x) >= 5:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):

			if x[1][0] == 'assignment_op':
				ret1 = name([x[2]],d) 
				ret2 = oper(x[3:-1],d,tree,parent)
				if (ret1 != None and ret2 != None):
					# TODO: add parse tree logic
					return 'oper->[:= name oper],' + ret1 + ret2

			ret1 = binops([x[1]],d)
			y = x[2:-1]
			for i in range(1,len(y)):
				ret2 = oper(y[i:],d,tree,parent)
				ret3 = oper(y[:i],d,tree,parent)
				if (ret1 != None and ret2 != None and ret3 != None):
					if '-p' in user_options: #display tree else display grammar productions
						child_1 = Node(ret1)
						child_2 = Node(ret2)
						child_3 = Node(ret3)
						# get immediate parent node
						parent_child = tree.get_first_child_at_parent(parent)				
						parent_child.add_child(child_1)
						parent_child.add_child(child_3)
						parent_child.add_child(child_2)
						
						return tree
					else:
						return 'oper->[binops oper oper],' + ret1 + ret2 + ret3

	if len(x) >= 4:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			ret1 = unops([x[1]],d)
			ret2 = oper([x[2]],d,tree,parent)
			if (ret1 != None and ret2 != None):
				# TODO: add parse tree logic
				return 'oper->[unops oper],' + ret1 + ret2

	ret = constants(x,d)
	if ret != None:
		if '-p' in user_options: #display tree else display grammar productions
			return ret
		else: 
			return 'oper->constants,' + ret

	ret = name(x,d)
	if ret != None:
		if '-p' in user_options: #display tree else display grammar productions
			return ret
		else: 
			return 'oper->name,' + ret


def binops(x,d):
	if x[0][0] in ['arithmatic_op','exponent_op','relational_op','log_op']:
		if '-p' in user_options: #display tree else display grammar productions
			return x[0][1]
		else:
			return 'binops->'+x[0][1]+','

def unops(x,d):
	if x[0][0] in ['trig_op','log_op']:
		# TODO: add parse tree logic
		return 'unops->'+x[0][1]+','

def constants(x,d):
	ret = strings(x,d)
	if ret != None:
		if '-p' in user_options: #display tree else display grammar productions
			return ret
		else:  
			return 'constants->strings,' + ret

	ret = ints(x,d)
	if ret != None:
		if '-p' in user_options: #display tree else display grammar productions
			return ret
		else: 
			return 'constants->ints,' + ret

	ret = floats(x,d)
	if ret != None:
		if '-p' in user_options: #display tree else display grammar productions
			return ret
		else:  
			return 'constants->floats,' + ret

def strings(x,d):
	if (len(x) == 1):
		# TODO: add parse tree logic
		if x[0][0] == 'string': return 'strings->STRINGS'

def name(x,d):
	if (len(x) == 1):
		if x[0][0] == 'ID':
			if '-p' in user_options: #display tree else display grammar productions
				return x[0][1]
			else: 
				return 'name->NAME,'

def ints(x,d):
	if (len(x) == 1):
		if x[0][0] == 'int_number':
			if '-p' in user_options: #display tree else display grammar productions
				return x[0][1]
			else: 
				return 'ints->INTS,'

def floats(x,d):
	if (len(x) == 1):
		if x[0][0] == 'real_number':
			if '-p' in user_options: #display tree else display grammar productions
				return x[0][1]
			else:  
				return 'floats->FLOATS'

def stmts(x,d):
	ret = ifstmts(x,d)
	if ret != None:
		# TODO: add parse tree logic 
		return 'stmts->ifstmts,' + ret

	ret = whilestmts(x,d)
	if ret != None:
		# TODO: add parse tree logic 
		return 'stmts->whilestmts,' + ret

	ret = letstmts(x,d)
	if ret != None:
		# TODO: add parse tree logic 
		return 'stmts->letstmts,' + ret

	ret = printstmts(x,d)
	if ret != None:
		# TODO: add parse tree logic 
		return 'stmts->printstmts,' + ret

def printstmts(x,d):
	if (len(x) >= 4):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if x[1][0] == 'keyword' and x[1][1] =='stdout':
				ret = oper(x[2:-1],d)
				if ret != None:
					# TODO: add parse tree logic 
					return 'printstmts->[stdout oper],' + ret

def ifstmts(x,d):
	if len(x) >= 5:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if (x[1][0] == 'keyword' and x[1][1] == 'if'):
				if (len(x) == 6):
					ret1 = expr([x[2]],d)
					ret2 = expr([x[3]],d)
					ret3 = expr([x[4]],d)
					if (ret1 != None and ret2 != None and ret3 != None):
						# TODO: add parse tree logic
						return 'ifstmts->[if expr expr expr],' + ret1 + ret2 + ret3

				if (len(x) == 5):
					ret1 = expr([x[2]],d)
					ret2 = expr([x[3]],d)
					if (ret1 != None and ret2 != None):
						# TODO: add parse tree logic
						return 'ifstmts->[if expr expr],' + ret1 + ret2

def whilestmts(x,d):
	if len(x) >= 5:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if (x[1][0] == 'keyword' and x[1][1] == 'while'):
				ret1 = expr([x[3]],d)
				ret2 = exprlist(x[3:-1],d)
				if (ret1 != None and ret2 != None):
					# TODO: add parse tree logic
					return 'whilestmts->[while expr exprlist],' + ret1 + ret2

def exprlist(x,d):
	ret1 = expr(x,d)
	if ret1 != None:
		# TODO: add parse tree logic 
		return 'exprlist->expr,' + ret1

	for i in range(0,len(x)):
		ret1 = expr(x[i:],d)
		ret2 = exprlist(x[:i],d)
		if (ret1 != None and ret2 != None):
			# TODO: add parse tree logic
			return 'exprlist->expr exprlist,' + ret1 + ret2


def letstmts(x,d):
	if (len(x) >= 6):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if (x[1][0] == 'keyword' and x[1][1] == 'let'):
				if (x[2][0] == 'bracket-l' and x[-2][0] == 'bracket-r'):
					ret1 = varlist(x[3:-2],d)
					if (ret1 != None):
						# TODO: add parse tree logic 
						return 'letstmts->[let [varlist]],' + ret1

def varlist(x,d):
	if (len(x) >= 4):
		if (x[0][0] == 'bracket-l' and x[3][0] == 'bracket-r'):
			if (len(x) == 4):
				ret1 = name([x[1]],d)
				ret2 = _type([x[2]],d)
				if (ret1 != None and ret2 != None):
					# TODO: add parse tree logic
					return 'varlist->[name type],' + ret1 + ret2

			if (len(x) >= 4):
				ret1 = name([x[1]],d)
				ret2 = _type([x[2]],d)
				ret3 = varlist(x[4:],d)
				if (ret1 != None and ret2 != None and ret3 != None):
					# TODO: add parse tree logic
					return 'varlist->[name type] varlist,' + ret1 + ret2 + ret3

def _type(x,d):
	if x[0][0] == 'keyword':
		if x[0][1] in ['bool','int','real', 'string']:
			# TODO: add parse tree logic
			return 'type->'+x[0][1]+','

'''

end of grammar... 

'''

def parse_file(file_content, uoptions):
	for option in uoptions:
		user_options.append(option)
		
	output = parser(file_content)
	return output

#set user options (mainly used for testing in the 
def set_user_options(uoptions):
	for opt in uoptions:
		user_options.append(opt)	

# scans and then parses x, uncomment lines for verbose
def parser(x):
	#print "scanning the following:"
	#print x, '\n'
	scanner_out = scanner(x)

	if ("-t" in user_options):
		print "list of tokens:"
		for token in scanner_out[0]:
			print '\t',token

	if (scanner_out[1]):
		#print "parsing..."
		parser_in = scanner_out[0]
		parser_out = T(parser_in,derivation)
		return parser_out

	else:
		return "scanner_failed" 
	
def tests():
	print "are any of the following in the grammar?"

	# should all be yes
	ts = [
		"[[if x y z]]",
		"[[]]",
		"[[[]]]",
		"[[stdout 5.2]]",
		"[[:= x 6]]",
		"[[sin x]]",
		"[[let [[x bool]]]]",
		"[[let [ [x bool] [y int] ] ]]",
		"[ [while x y] ]",
		"[ [while x y z ] ]",
		'[[+ 1 3]]',
		'[[+ 1 [+ 1 1]]]',
		'[[+ 1 [* [+ 2 3] 7]]]',
		'[[:= x [- x 1]]]',
		'[[+ 1 x][+ 1 1]]',
		'[[][]]',
		'[[][][]]',
		'[[ := x [+ 1 1] ]]',

		'[[+ 1 [* [+ 2 3] 7]]]' # e.g. from class website
		

		]

	print ''
	for t in ts:
		if (parser(t) != None):
			print t, "yes"
		else: print t, "no"

	# should all be no
	ts = [
		"[[if x y z w]]",
		"[]",
		'[[+ 1 1 1]]',
		"[][]",
		"[1  x  [1 5]]" # e.g. from class website
		]

	print ''
	for t in ts:
		if (parser(t) != None):
			print t, "yes"
		else: print t, "no"


	# error/edge cases
	# for finding bugs
	ts = [
		'[[while [= 5 x] [:= x [- x 1]]]]' # e.g. from class website
		]

	print ''
	for t in ts:
		if (parser(t) != None):
			print t, "yes"
		else: print t, "no"



#tests()


