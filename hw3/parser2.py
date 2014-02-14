from scanner import *

derivation = [] # an extra list to be used later


'''

info:

the next 19 functions define the grammar for IBTL
blank lines separate production rules

'''

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
	ret = oper(x,d)
	if ret != None: return 'expr->oper,' + ret

	ret = stmts(x,d)
	if ret != None: return 'expr->stmts,' + ret

def oper(x,d):
	if len(x) >= 5:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):

			if x[1][0] == 'assignment_op':
				ret1 = name([x[2]],d) 
				ret2 = oper(x[2:-1],d)
				if (ret1 != None and ret2 != None):
					return 'oper->[:= name oper],' + ret1 + ret2

			ret1 = binops([x[1]],d)
			y = x[2:-1]
			for i in range(1,len(y)):
				ret2 = oper(y[i:],d)
				ret3 = oper(y[:i],d)
				if (ret1 != None and ret2 != None and ret3 != None):
					return 'oper->[binops oper oper],' + ret1 + ret2 + ret3

	if len(x) >= 4:
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			ret1 = unops([x[1]],d)
			ret2 = oper([x[2]],d)
			if (ret1 != None and ret2 != None):
				return 'oper->[unops oper],' + ret1 + ret2

	ret = constants(x,d)
	if ret != None: return 'oper->constants,' + ret

	ret = name(x,d)
	if ret != None: return 'oper->name,' + ret


def binops(x,d):
	if x[0][0] in ['arithmatic_op','exponent_op','relational_op','log_op']:
		return 'binops->'+x[0][1]+','

def unops(x,d):
	if x[0][0] in ['trig_op','log_op']:
		return 'unops->'+x[0][1]+','

def constants(x,d):
	ret = strings(x,d)
	if ret != None: return 'constants->strings,' + ret

	ret = ints(x,d)
	if ret != None: return 'constants->ints,' + ret

	ret = floats(x,d)
	if ret != None: return 'constants->floats,' + ret

def strings(x,d):
	if x[0][0] == 'string': return 'strings->STRINGS'

def name(x,d):
	if x[0][0] == 'ID': return 'name->NAME,'

def ints(x,d):
	if x[0][0] == 'int_number': return 'ints->INTS,'

def floats(x,d):
	if x[0][0] == 'real_number': return 'floats->FLOATS'

def stmts(x,d):
	ret = ifstmts(x,d)
	if ret != None: return 'stmts->ifstmts,' + ret

	ret = whilestmts(x,d)
	if ret != None: return 'stmts->whilestmts,' + ret

	ret = letstmts(x,d)
	if ret != None: return 'stmts->letstmts,' + ret

	ret = printstmts(x,d)
	if ret != None: return 'stmts->printstmts,' + ret

def printstmts(x,d):
	if (len(x) >= 4):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if x[1][0] == 'keyword' and x[1][1] =='stdout':
				ret = oper(x[2:-1],d)
				if ret != None: return 'printstmts->[stdout oper],' + ret

def ifstmts(x,d):
	if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
		if (x[1][0] == 'keyword' and x[1][1] == 'if'):
			if (len(x) == 6):
				ret1 = expr([x[2]],d)
				ret2 = expr([x[3]],d)
				ret3 = expr([x[4]],d)
				if (ret1 != None and ret2 != None and ret3 != None):
					return 'ifstmts->[if expr expr expr],' + ret1 + ret2 + ret3

			if (len(x) == 5):
				ret1 = expr([x[2]],d)
				ret2 = expr([x[3]],d)
				if (ret1 != None and ret2 != None):
					return 'ifstmts->[if expr expr],' + ret1 + ret2

def whilestmts(x,d):
	if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
		if (x[1][0] == 'keyword' and x[1][1] == 'while'):
			ret1 = expr([x[2]],d)
			ret2 = exprlist(x[2:],d)
			if (ret1 != None and ret2 != None):
				return 'whilestmts->[while expr exprlist],' + ret1 + ret2

def exprlist(x,d):
	ret1 = expr(x,d)
	if ret1 != None: return 'exprlist->,expr' + ret1

	for i in range(0,len(x)-1):
		ret1 = expr(x[i:],d)
		ret2 = exprlist(x[:i],d)
		if (ret1 != None and ret2 != None):
			return 'exprlist->expr exprlist,' + ret1 + ret2


def letstmts(x,d):
	if (len(x) >= 6):
		if (x[0][0] == 'bracket-l' and x[-1][0] == 'bracket-r'):
			if (x[1][0] == 'keyword' and x[1][1] == 'let'):
				if (x[2][0] == 'bracket-l' and x[-2][0] == 'bracket-r'):
					ret1 = varlist(x[3:-2],d)
					if (ret1 != None): return 'letstmts->[let [varlist]],' + ret1

def varlist(x,d):
	if (len(x) >= 4):
		if (x[0][0] == 'bracket-l' and x[3][0] == 'bracket-r'):
			if (len(x) == 4):
				ret1 = name([x[1]],d)
				ret2 = _type([x[2]],d)
				if (ret1 != None and ret2 != None):
					return 'varlist->[name type],' + ret1 + ret2

			if (len(x) >= 4):
				ret1 = name([x[1]],d)
				ret2 = _type([x[2]],d)
				ret3 = varlist(x[4:],d)
				if (ret1 != None and ret2 != None and ret3 != None):
					return 'varlist->[name type] varlist,' + ret1 + ret2 + ret3

def _type(x,d):
	if x[0][0] == 'keyword':
		if x[0][1] in ['bool','int','real', 'string']:
			return 'type->'+x[0][1]+','

'''

end of grammar... 

'''



# scans and then parses x, uncomment lines for verbose
def parser(x):
	#print "scanning the following:"
	#print x, '\n'
	scanner_out = scanner(x)

	#print "list of tokens:"
	#print scanner_out[0], '\n'

	if (scanner_out[1]):
		#print "parsing..."
		parser_in = scanner_out[0]
		parser_out = T(parser_in,derivation)
		return parser_out

	else:
		print "scanner_failed" 
	
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
		"[ [while x y z s] ]",
		'[[+ 1 3]]',
		'[[+ 1 [+ 1 1]]]',
		'[[+ 1 [* [+ 2 3] 7]]]',
		'[[:= x [- x 1]]]'

		]

	print ''
	for t in ts:
		if (parser(t) != None):
			print t, "yes"
		else: print t, "no"

	# should all be no
	ts = [
		"[[if x y z w]]",
		"[]"

		]

	print ''
	for t in ts:
		if (parser(t) != None):
			print t, "yes"
		else: print t, "no"

tests()


