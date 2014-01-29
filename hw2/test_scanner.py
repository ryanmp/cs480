from scanner_ryan import *

# input: "tobetested",pass,type
# where pass is True or False (it should pass or fail)
# and type, should come from 

def test_word(_in,_pass,_type):
	t = scanner(_in)
	assert(t[1]==_pass)
	#additional checks if passed=true
	if (_pass):
		assert(t[0][0][0]==_type)
		assert(t[0][0][1]==_in)

def test_all():

	#good words
	test_word('1.253431',True,'real_number')
	test_word('113535',True,'int_number')
	test_word('Crazy123_Var__a',True,'ID')

	#bad words
	test_word('1.423.23',False,'')
	test_word('.090..',False,'')

	# what about 1AtestGoodOrBadVar ? not a valid id, but should it parse
	# as a int_number and then an ID

	print "passed all tests"