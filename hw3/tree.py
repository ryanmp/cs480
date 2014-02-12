# sudo easy_install -U treelib
from treelib import Tree, Node

from scanner import *

# let's put this in our tree: 1 * 2 + 5 / 2

'''

	 +
	/ \
   *   /
  / \  / \
 1	2  5  2		


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



#rules
# oper -> binop oper oper | constants | name



oper = [[('binop',False), ('oper',False), ('oper',False)], [('constants',False)]]

constants = [('int_number',True)]
binop = [('arithmatic_op',True)]

tree = Tree()

scanner_in = "+ 1 2"
scanner_out = scanner(scanner_in)[0]


