"""
You are given an array of strings tokens that represents 
an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents 
the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

Takeaway:

This is called postfix notation. 

Stacks are classic approach.

using int(b / a) instead of  (b // a)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # pop - append 0(1)
        
        result = 0
        for elem in tokens:
            if elem == "+":
                stack.append(stack.pop() + stack.pop())
            elif elem == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif elem == "*":
                stack.append(stack.pop() * stack.pop())
            elif elem == "/":
                a, b = stack.pop(), stack.pop()
                # this is a trick 
                stack.append(int(b / a))
                
            else:
                # add the item to the stack
                stack.append(int(elem))
        
        # print(stack)
        return stack[0]
