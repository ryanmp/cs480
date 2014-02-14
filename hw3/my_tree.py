
# our tree!
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.depth = 0

    def add_child(self, obj):
    	obj.depth = self.depth + 1
        self.children.append(obj)


# an example

r = Node(1) # root

a1 = Node(2)
a2 = Node(3)
r.add_child(a1)
r.add_child(a2)

b1 = Node(4)
a1.add_child(b1)


# not finished yet... 
def print_tree(t):
	if (t != None):
		print spacer(int(t.depth)) + str(t.data)

		if (len(t.children) > 0):
			print spacer2(int(t.depth)) + "|"
			for i in t.children:
				if (i != None): 
					print_tree(i)

# needed for print_tree
def spacer(x):
	l = ""
	if (x > 0):
		l = "|"
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

#todo
# implement rpn and pn traversal of tree...