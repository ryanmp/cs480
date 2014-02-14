# sudo easy_install -U treelib
from treelib import Tree, Node

from scanner import *

import sys

# let's put this in our tree: 1 * 2 + 5 / 2

'''

	 +
	/ \
   *   /
  / \  / \
 1	2  5  2		


'''

'''
def basic_foo():
	tree = Tree()
	tree.create_node("+","root")
	tree.create_node("*", "leaf.1", parent = "root")
	tree.create_node("/", "leaf.2", parent = "root")

	tree.create_node("1", "leaf.1.1", parent = "leaf.1")
	tree.create_node("2", "leaf.1.2", parent = "leaf.1")

	tree.create_node("5", "leaf.2.1", parent = "leaf.2")
	tree.create_node("2", "leaf.2.2", parent = "leaf.2")

	tree.show()


	prefix_out = []
	for node in tree.expand_tree(mode=Tree.DEPTH, reverse=False):
		#print tree[node].identifier
		prefix_out.append( tree[node].tag )



	postfix_out = []
	for node in tree.expand_tree(mode=Tree.DEPTH, reverse=True):
		# print tree[node]
		postfix_out.append( tree[node].tag )
	postfix_out.reverse() # i think this is right... I need to double check it though...


	print (prefix_out)
	print (postfix_out)
'''


'''


def T(x,t,i):
	if (x[0] == 'bracket-l' and x[-1] == 'bracket-r'):
		t.create_node("T","root")
		i += 1
		t.create_node("[", str(i), parent = "root")
		i += 1
		t.create_node("S", str(i), parent = "root")
		S(x[1:-1],t,str(i), i)
		i += 1
		t.create_node("]", str(i), parent = "root")
		
def S(x,t,_par, i):
	i += 1
	t.create_node("expr", str(i), parent = _par)
	E(x,t,str(i), i)

def E(x,t,_par, i):
	i += 1
	t.create_node("oper", str(i), parent = _par)
	O(x,t,str(i), i)

def O(x,t,_par, i):
	t.create_node("[", "leaf.2.1.1.1", parent = _par)
	t.create_node("binops", "leaf.2.1.1.2", parent = _par)
	t.create_node("oper", "leaf.2.1.1.3", parent = _par)
	t.create_node("oper", "leaf.2.1.1.4", parent = _par)
	t.create_node("]", "leaf.2.1.1.5", parent = _par)

'''


#rules
# oper -> binop oper oper | constants | name
#oper = [[('binop',False), ('oper',False), ('oper',False)], [('constants',False)]]
#constants = [('int_number',True)]
#binop = [('arithmatic_op',True)]

'''
t1 = ['bracket-l','ID','bool_const','bracket-r']
l = []
def typefoo(x,l):

	if x == 'bool_const':
		l.append('bool_const')
	elif x == 'int':
		l.append( 'int' )
	elif x == 'float':
		l.append( 'float' )
	elif x == 'string':
		l.append( 'string')
	else: print x,l,"ERROR1!"
	#sys.exit()

def name(x,l):

	if x == 'ID':
		l.append( 'ID' )
	else: print x,l,"ERROR2!"


def varlist(x, l):

	if (x[0] == 'bracket-l' and x[3] == 'bracket-r'):
		if (len(x) == 4):
				name(x[1],l)
				typefoo(x[2],l)
		if (len(x) > 4):
			name(x[0],l)
			varlist(x[1:],l)

scanner (t1, l)
print l
'''








