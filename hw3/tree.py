
# our tree class!
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.depth = 0

    def add_child(self, obj):
    	obj.depth = self.depth + 1
        self.children.append(obj)

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

print "tree:"
print_tree(tree)
print "pre order traversal:", pre_order_trav(tree)
print "post order traversal:", post_order_trav(tree)
