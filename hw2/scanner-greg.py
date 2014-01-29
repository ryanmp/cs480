#!/usr/bin/python
# FSA implementation

# Constants
def is_bool_const(input):
    bools = ['true','false']
    class State:
        N0 = 0
        N1 = 1
        N2 = 2
        N3 = 3
    
    current_state = State.N0
    i=0
    current_char = input[i]

    
    if current_state == State.N0:
	if current_char == bools[0][0] and len(input) == len(bools[0]):
            current_state = State.N1
        elif current_char == bools[1][0] and len(input) == len(bools[1]):
            current_state = State.N2
        else:
            current_state = State.N3
            return False
        
    i+=1
    current_char = input[i]
    
    while (current_state == State.N1 or current_state == State.N2) and current_char.isalpha():
        if current_state == State.N1: # look for true
            if (current_char == bools[0][i]):
                i+=1
            else:
                return False
                
        if current_state == State.N2: # look for false
            if (current_char == bools[1][i]):
                i+=1
            else:
                return False
            
        if i < len(input):
            current_char = input[i]            
        else:
            return True

    return False
    
def is_str_const(input):
    return True
    
def is_int_const(input):
    return True
    
def is_real_const(input):
    return True
    
# Binary Operators
def is_rel_op(input):
    return True
    
def is_add_sub_op(input):
    return True
    
def is_mul_div_mod_op(input):
    return True
    
def is_exp_op(input):
    return True

# Trigonometry
def is_trig_op(input):
    return True

# Logical Operators
def is_bool_op(input):
    return True

# Assignment Operator
def is_assignment_op(input):
    return True

# Keywords
def is_keyword(input):
    return True

# Special symbols
def is_bracket(input):
    return True

# Identifiers or variable names
def is_identifier(input):
    class State:
        N0 = 0
        N1 = 1
        N2 = 2
    
    current_state = State.N0
    i=0
    current_char = input[i]
    
    if current_state == State.N0 and current_char.isalpha():
        current_state = State.N1;
            
    i+=1
    current_char = input[i]
    
    while current_state == State.N1 and (current_char.isalpha() or current_char.isdigit() or current_char == '_'):
        current_state = State.N1    
        i+=1
        if i < len(input):
            current_char = input[i]            
        else:
            return True

    current_state = State.N2
    return False
    


# testing FSA
input = "variable_name"
print "is_identifier(" + input + ") = " + str(is_identifier(input))

input = "true"
print "is_bool_const(" + input + ") = " + str(is_bool_const(input))

input = "false"
print "is_bool_const(" + input + ") = " + str(is_bool_const(input))

input = "trues"
print "is_bool_const(" + input + ") = " + str(is_bool_const(input))

print "done"
