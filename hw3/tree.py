
# our tree class!
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.depth = 0

    def add_child(self, obj):
    	obj.depth = self.depth + 1
        self.children.append(obj)
     
    def get_child_at(self, index):
        return self.children[index]   

    def get_first_child_at_parent(self,obj):
        if len(obj.children) > 0:
            return obj.children[0]
        else:
            return self.children[0]
    
    def get_first_child_at_parent_level(self,obj,level):
        if level == 0:
            return self.children[0]#obj.children[0]
        
        else:
            if level >= 1:
                if len(obj.children)>0: 
                    return obj.children[0]
                else:
                    return self.children[0]
            else:
                return self.children[0] 
            
#             leafs = []
#             def _get_leaf_nodes( node):
#                 if node is not None:
#                     if len(node.children) == 0:# and node.depth == level:
#                         leafs.append(node)
#                     for n in node.children:
#                         _get_leaf_nodes(n)
#             _get_leaf_nodes(obj)
#             
#             if len(leafs) > 0:
#                 return leafs[0]
#             else:
#             if level == 1:
#                 return self.children[0]
            #if level == 2:
            #    return self.children[0][0]
            
    def get_parent_depth(self,obj):
        return obj.depth
    
# umm.. not perfect, but whatev,
def print_tree(t):
	if (t != None):
		if (int(t.depth) > 0):
			print spacer2(int(t.depth-1)) + spacer(int(1)) + str(t.data)
		else: print str(t.data)
		if (len(t.children) > 0):
			print spacer2(int(t.depth)) + "|"
			for i in t.children:
				if (i != None): 
					print_tree(i)

# print_tree returning string version (used for testing)                  
def get_tree_str(t,output):
    if (t != None):
        if (int(t.depth) > 0):
            output += spacer2(int(t.depth-1)) + spacer(int(1)) + str(t.data) #+ '\n'
        else: output += str(t.data) #+ '\n'
        
        if (len(t.children) > 0):
            output += spacer2(int(t.depth)) + "|"
            for i in t.children:
                if (i != None): 
                    output =get_tree_str(i,output)
    return output


# needed for print_tree
def spacer(x):
	l = ""
	if (x > 0):
		l = "@"
		for i in xrange(x):
			l += "--"
		return l
	return l

# needed for print_tree
def spacer2(x):
	l = ""
	if (x > 0):
		l = "|"
		for i in xrange(x):
			l += "  "
		return l
	return l

'''

let's put this in our tree for testing:

1 * 2 + 5 / 3

	 +
	/ \
   *   /
  / \  / \
 1	2  5  3		


'''

tree = Node('+')
l = Node('*')
r = Node('/')
tree.add_child(l)
tree.add_child(r)

ll = Node('1')
lr = Node('2')
l.add_child(ll)
l.add_child(lr)

rl = Node('5')
rr = Node('3')
r.add_child(rl)
r.add_child(rr)




def pre_order_trav(t):
	out = []
	def inner(t):
		if (t != None):
			out.append(t.data)
			if (len(t.children) > 0):
				for i in t.children:
					if (i != None): 
						inner(i)
	inner(t)
	return out

def post_order_trav(t):
	out = []
	def inner(t):
		if (t != None):
			if (len(t.children) > 0):
				for i in t.children:
					if (i != None): 
						inner(i)
			out.append(t.data)
	inner(t)
	return out
    
def print_test_tree_version1():
    # this version includes the grammar and 
    # parse tree for [[+ x y]]
    root = Node('T')
    tree2 = root
    
    # first level
    child1 = Node('[')
    child2 = Node('S')
    child3 = Node(']')
    tree2.add_child(child1)
    tree2.add_child(child2)
    tree2.add_child(child3)
    
    # second level
    child4 = Node('[')
    child5 = Node('S')
    child6 = Node(']')
    child2.add_child(child4)
    child2.add_child(child5)
    child2.add_child(child6)
    
    # third level
    child7 = Node('expr')
    child5.add_child(child7)
    
    # 4th level
    child8 = Node('oper')
    child7.add_child(child8)
    
    # 5th level
    child9 = Node('[')
    child10 = Node('binops')
    child11 = Node('oper')
    child12 = Node('oper')
    child13a = Node(']')
    
    child8.add_child(child9)
    child8.add_child(child10)
    child8.add_child(child11)
    child8.add_child(child12)
    child8.add_child(child13a)
    
    # 6th level
    child13 = Node('+')
    child14 = Node('const')
    child15 = Node('const')
    child10.add_child(child13)
    child11.add_child(child14)
    child12.add_child(child15)
    
    # 7th level
    child16 = Node('int')
    child17 = Node('int')
    child14.add_child(child16)
    child15.add_child(child17)
    
    # 8th level
    child18 = Node('x')
    child19 = Node('y')
    child16.add_child(child18)
    child17.add_child(child19)
    print_tree(tree2)

    
def print_test_tree_version2():
    # this version prints only the terminals (I think this is similar to the sample shown in class)
    # simplied version of tree2 -> for [[+ x y]]
    root = Node('T')
    tree2 = root
    
    # first level
    child1 = Node('[')
    child3 = Node(']')
    tree2.add_child(child1)
    tree2.add_child(child3)
    
    # 2nd level
    child9 = Node('[')
    child13a = Node(']')
    child1.add_child(child9)
    child1.add_child(child13a)
    
    # 3th level
    child13 = Node('+')
    child18 = Node('x')
    child19 = Node('y')
    
    child9.add_child(child13)
    child9.add_child(child18)
    child9.add_child(child19)
    print_tree(tree2)

def test_print_tree():    
    print "tree:"
    print_tree(tree)
    print "pre order traversal:", pre_order_trav(tree)
    print "post order traversal:", post_order_trav(tree)
    
    print_test_tree_version1()
    print_test_tree_version2()
