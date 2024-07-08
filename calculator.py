# assignment: programming assignment 4
# author: Lynelle Goh
# date: 11/17/2022
# file: calculator.py is a program that can change an infix expression to postfix and evaluate infix expressions
# input: takes in infix expressions
# output: outputs the desired result, whether it be the evaluation or the postfix expression

from stack import Stack
from tree import ExpTree

def infix_to_postfix(infix):
    
    operator = ['+','-','*','/', '^', '(', ')']

    # remember PEMDAS
    precedence = {'+':1,'-':1, '*':2, '/':2}

    result_string = []
    result = []

    for i in infix:
        # add in the number
        if i not in operator:
            result_string.append(i)
        # write out priority for paranthesis
        elif i == '(':
            result.append('(')
        elif i ==')':
            while result and result[-1] != '(':
                result_string.append(result.pop())
            result.pop()
        else:
            # result must exist and result's last item must be ( and the precendece of i must be less than the precedence of the last object in result
            # we know that the last object in result is an operator because we just appended it
            while result and result[-1] != '(' and precedence[i]<=precedence[result[-1]]:
                result_string.append(result.pop())
            result.append(i)
    while result:
        result_string.append(result.pop())
    # separate the list with spaces and make it a string
    return " ".join(result_string)

def calculate(infix):
    
    postfix = infix_to_postfix(infix).split()
    
    # use our own evaluation from our expression tree
    tree = ExpTree.make_tree(postfix)
    return ExpTree.evaluate(tree)

            

# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0
    
    
