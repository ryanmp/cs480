'''
Created on Feb 12, 2014
'''
import sys
from scanner_ryan import *
tokens = []
lexemes = []
operations = []
evaluation = 0

def parse_file(input_file):    
    print "scanning " + str(input_file)
    
    output = []
    f = open(input_file)
    lines_raw = f.readlines()
    for i in range(0,len(lines_raw)):
        tree = parse_line(lines_raw[i])
        output.append(tree)

    return output


def parse_line(input_line):
    global tokens
    tokens = []
    tokens = scanner(input_line)[0]
    tokens.reverse()
    nodes = expression()
    return nodes


def expression():
    global tokens
    global lexemes
    global evaluation
    
    current_token = tokens.pop() # get next token
    if current_token[0] == 'bracket-l': # if we get '[' we got a new expression
        lexemes.append(current_token[1]) 

        current_token = tokens.pop() # get next token if any
            
        while current_token[0] != 'bracket-r':
            #TODO: Implement next production grammar with recursion:
            #if current_token[0] == 'bracket-l':
            #    lexemes.append(current_token[1])    
            #    return expression()
            
            if current_token[0] == 'int_number':
                num_value = eval(current_token[1])
                lexemes.append(num_value)
            elif current_token[1] in ['+','-','*']:
                lexemes.append(current_token[1])
                operations.append(current_token[1])    
            else:
                lexemes.append(current_token[0]) 
                
            current_token = tokens.pop() # get next token if any
            
            if current_token[0] == 'bracket-r':
                lexemes.append(current_token[1]) 
        
        # reached end of the expression
        if current_token[0] == 'bracket-r':
            # evaluate expression
            if operations[0] == '+': 
                evaluation = lexemes[2] + lexemes[3]
    
    parse_tree = (lexemes, evaluation)
                        
    return parse_tree

