# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:34:25 2022

@author: adenn
"""


def arithmetic_arranger(problem_list, display_solutions = False):
    
    #check for correct number of problems
    if len(problem_list) > 5:
        error = 'Error: Too many problems.'
        return error
    
    line1 = line2 = line3 = line4 = ''
    for problem in problem_list:
        
        #check for unallowed operators
        if (problem.find('*')!=-1) or (problem.find('/')!=-1):
            error = "Error: Operator must be '+' or '-'."
            return error
        
        #split according to operator
        if problem.find('-')!=-1:
            sign='-'
        elif problem.find('+')!=-1:
            sign='+'
        operands = problem.split(sign)
        operand1 = operands[0].strip()
        operand2 = operands[1].strip()
        
        #check for digits only
        if not (operand1.isdigit() and operand2.isdigit()):
            error = 'Error: Numbers must only contain digits.'
            return error
        
        #check for correct length of digits
        if (len(operand1)>4) or (len(operand2)>4):
            error = 'Error: Numbers cannot be more than four digits.'
            return error
        
        #determine final printed result format width based on largest operand
        if len(operand1)>len(operand2):
            res_width=len(operand1)+2
        else:
            res_width=len(operand2)+2
        
        #account for the + or - operation
        if sign == '-':
            answer = int(operand1) - int(operand2)
        else:
            answer = int(operand1) + int(operand2)
        
        #determine the amount of blank spaces needed for pretty print
        operand1_space = (res_width - len(operand1)) * ' '
        operand2_space = (res_width - len(operand2) -1) * ' '
        answer_space = (res_width - len(str(answer))) * ' '
        
        if problem_list.index(problem) == len(problem_list) - 1:
            problemspace = ''
        else:
            problemspace = '    '
        
        #construct the final writeout
        line1 = line1 + operand1_space + operand1 + problemspace
        line2 = line2 + sign + operand2_space + operand2 + problemspace
        line3 = line3 + (res_width * '-') + problemspace
        line4 = line4 + answer_space + str(answer) + problemspace
        
    #display the result accounting for the result parameter
    '''
    print(line1)
    print(line2)
    print(line3)
    if display_solutions == True:
        print(line4)
    '''
    
    arranged_problems = line1+'\n'+line2+'\n'+line3
    if display_solutions == True:
      arranged_problems = arranged_problems + '\n' + line4
    
    return arranged_problems
        
