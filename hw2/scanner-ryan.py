input = '1++6*3^44 1.23'

# add any keywords - umm, I don't know what language we are translating, so I'll just
# pick a few random ones for now...
keywords = [
'bool',
'let',
'real',
'string',
'stdout',
'if',
'then',
'while',
'for'
]

boolean_constants = ['true','false']
logical_operators = ['and','or','not']
trig_operators = ['sin','cos','tan']

 # x: input string
 # on return:
 #	([list of tokens],successful tokenization?)
def scanner(x):
	print x
	x += ' '
	x = list(x)
	output = []

	i = -1 #current char
	count_loops = 0
	success = True

	while(True):
		count_loops += 1

		#we got all the way through the string, break!
		if i >= len(x)-1:
			break

		#we aren't going to finish... tokenizing error occured
		if count_loops >= len(x):
			success = False
			break

		#skip spaces and newlines
		if CharType(x[i]) == 'skippable':
			i += 1

		#brackets, parens...
		if CharType(x[i]) == 'bracket':
			output.append(("bracket",x[i]))
			i += 1

		#assignment op :=
		if CharType(x[i]) == 'colon':
			if CharType(x[i+1]) == 'equals':
				i += 2
				output.append(('assignment_op',''))

		#relational ops
		if CharType(x[i]) == 'equals':
			i += 1
			output.append(('relational_op','equals'))
		if CharType(x[i]) == 'exclamation':
			if CharType(x[i+1]) == 'equals':
				i += 2
				output.append(('relational_op','!='))
		if CharType(x[i]) == 'lt':
			if CharType(x[i+1]) == 'equals':
				i += 2
				output.append(('relational_op','<='))
			else:
				i += 1
				output.append(('relational_op','<'))
		if CharType(x[i]) == 'gt':
			if CharType(x[i+1]) == 'equals':
				i += 2
				output.append(('relational_op','>='))
			else:
				i += 1
				output.append(('relational_op','>'))

		#string constant
		if CharType(x[i]) == 'quote':
			i += 1
			if CharType(x[i]) == 'quote': # it's an empty string
				i += 1
				output.append('string','')
			else: # not an empty string
				tempVal = x[i]
				while (CharType(x[i]) != 'quote'):
					if (i > len(x)-2): #didn't find a closing quote!
						success = False
						return (output, success)
					i += 1
					tempVal += x[i]
				tempVal = tempVal[:-1] #step back one char
				i += 1
				output.append(('string',tempVal))

		#keyword, misc keywords, OR id -> (variable names?)
		if CharType(x[i]) == 'alphabet':
			tempVal = x[i]
			while (CharType(x[i]) in ['digit','alphabet','underscore']) and (i < len(x)-1):
				i += 1
				tempVal += x[i]
			tempVal = tempVal[:-1] #step back one char
			if tempVal in keywords:
				output.append(('keyword',tempVal))
			elif tempVal in boolean_constants:
				output.append(('bool_const',tempVal))
			elif tempVal in logical_operators:
				output.append(('log_op',tempVal))
			elif tempVal in trig_operators:
				output.append(('trig_op',tempVal))
			else:
				output.append(('ID',tempVal))

		#numbers
		if CharType(x[i]) in ['digit','period']:
			
			#real .xxx
			if CharType(x[i]) == 'period':
				tempVal = x[i]
				i += 1
				while (CharType(x[i]) == 'digit') and (i < len(x)-1):
					i += 1
					tempVal += x[i]
				tempVal = tempVal[:-1] #step back one char
				output.append(('real_number',tempVal))

			#real x.xx & int
			else:
				isReal = 0
				tempVal = x[i]
				while (CharType(x[i]) in ['digit','period']) and (i < len(x)-1):
					if CharType(x[i]) == 'period':
						isReal += 1
					i += 1
					tempVal += x[i]
				tempVal = tempVal[:-1] #step back one char

				if (isReal == 0): output.append(('int_number',tempVal))
				elif (isReal == 1): output.append(('real_number',tempVal))
				else: return (output, False)

		#arithmatic op
		if CharType(x[i]) == 'arithmatic':
			output.append(('arithmatic_op',x[i]))
			i += 1

		#exponent op
		if CharType(x[i]) == 'exponent':
			output.append(('exponent_op','^'))
			i += 1


    
	return (output, success)


def CharType(x):
	if ord(x) >= 65 and ord(x) <= 122:
		if ord(x) != 94:
			return 'alphabet'
	if ord(x) >= 48 and ord(x) <= 57:
		return 'digit'
	if ord(x) == 46:
		return 'period'
	if ord(x) in [43,45,42,47,37]: # + - * / %
		return 'arithmatic'
	if ord(x) in [40,41,91,93,123,125]:
		return 'bracket' # ( ) [ ] { }
	if ord(x) in [10,32]:
		return 'skippable' # space and newline
	if ord(x) == 95:
		return 'underscore'
	if ord(x) == 58:
		return 'colon'
	if ord(x) == 34:
		return 'quote'
	if ord(x) == 33:
		return 'exclamation'
	if ord(x) == 60:
		return 'lt'
	if ord(x) == 62:
		return 'gt'
	if ord(x) == 61:
		return 'equals'
	if ord(x) == 94:
		return 'exponent'

	return 'ERROR'
		


