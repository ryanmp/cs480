from scanner_ryan import *

def test_suite():

	#good words

	tp1 = scanner("1.253431")
	assert(tp1[1]==True)
	assert(tp1[0][0][0]=='real_number')
	assert(tp1[0][0][1]=='1.253431')

	tp2 = scanner("200")
	assert(tp2[1]==True)
	assert(tp2[0][0][0]=='int_number')
	assert(tp2[0][0][1]=='200')

	tp2 = scanner("200")
	assert(tp2[1]==True)
	assert(tp2[0][0][0]=='int_number')
	assert(tp2[0][0][1]=='200')

	tp3 = scanner("Crazy123_Var__a")
	assert(tp3[1]==True)
	assert(tp3[0][0][0]=='ID')
	assert(tp3[0][0][1]=='Crazy123_Var__a')

	#bad words

	tf1 = scanner("1.423.23")
	assert(tf1[1]==False)

	tf2 = scanner(".090..")
	assert(tf2[1]==False)
	# failed this test! fix the code ryan!

	tf3 = scanner("1badID")
	assert(tf3[1]==False)
	# this shouldn't be accepted, right?
	# if so...
	# failed this test! fix the code ryan!

	print "passed all tests"