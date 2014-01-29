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
	return t # just in case we need it

def test_sentence(_in,_pass):
	# to be finished... this might be a bit simpler than test_word,
	# maybe just a call to: scanner(whole sentence)
	t = scanner(_in)
	if (_pass):
		assert(t[1]) 
	else:
		assert(t[1] == False)
	return t

def test_all():
	test_list_of_words()
	test_list_of_sentences()
	print "passed all tests"

def test_list_of_words():
	#good words
	test_word('1.253431',True,'real_number')
	test_word('113535',True,'int_number')
	test_word('Crazy123_Var__a',True,'ID')

	#key words that should be recognized
	test_word('true',True,'bool_const')
	test_word('true',True,'bool_const')
	test_word('and',True,'log_op')
	test_word('or',True,'log_op')
	test_word('not',True,'log_op')
	test_word('sin',True,'trig_op')
	test_word('cos',True,'trig_op')
	test_word('tan',True,'trig_op')

	test_word('bool',True,'keyword')
	test_word('let',True,'keyword')
	test_word('real',True,'keyword')
	test_word('string',True,'keyword')
	test_word('stdout',True,'keyword')
	test_word('if',True,'keyword')
	test_word('then',True,'keyword')
	test_word('while',True,'keyword')
	test_word('for',True,'keyword')

	#the following should not register as any of the above
	#keyword types, but instead as IDs

	ids_to_check = []
	ids_to_check.append(test_word('True',True,'ID'))
	ids_to_check.append(test_word('FALSE',True,'ID'))
	ids_to_check.append(test_word('anD',True,'ID'))
	ids_to_check.append(test_word('Sin',True,'ID'))
	ids_to_check.append(test_word('Cos',True,'ID'))
	ids_to_check.append(test_word('Tan',True,'ID'))
	ids_to_check.append(test_word('BOOL',True,'ID'))
	# etc....

	#we will also check to ensure all the IDs have been added to
	#the symbol table

	for i in xrange(len(ids_to_check)):
		assert(ids_to_check[i][0][0][1] in symbol_table)
	
	#bad words
	test_word('1.423.23',False,'')
	test_word('.090..',False,'')
	test_word('?',False,'')

	# what about 1AtestGoodOrBadVar ? not a valid id, but should it parse
	# as a int_number and then an ID

#any sentence made of valid words should pass,
#we will call these, 'good sentences'
def test_list_of_sentences():
	#good sentences
	###############

	test_sentence('if [bool x = True] then y = 5.234',True)
	test_sentence('1+4*8^3/4%1.534-.13409',True)

	#bad sentences
	##############

	#umm... should this parse as float, .0984 float .9089,
	#or read it as a single number and fail because it contains two
	#decimals?
	#i'm guessing it should fail
	test_sentence('.0984.9089 + .9083-.89384',False)








