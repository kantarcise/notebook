"""

You are given an array of strings tokens that represents an arithmetic expression 
in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

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

Use a stack

compartmentalize the code.

you can use the same stack for both operations and operands.

It is possible to use dictionaries aswell.

"""


class Solution:

    def evalRPN(self, tokens) -> int:
        # we have string tokens which all should be casted to integers
        # we have operators to calculate the results.
        
        # a list based stack
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop()) 
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]


    # using a dictionary and lambda functions

    def evalRPN_(self, tokens) -> int:
        stack = []
        ops = {'+':lambda x, y: x+y, '-':lambda x, y: x-y, '*':lambda x, y: x*y, '/':lambda x, y: x/y}
        for s in tokens:
            try:
                stack.append( float( s ) )
            except:
                stack.append( int( ops[s]( stack.pop(-2), stack.pop(-1) ) ) )
        return int( stack[-1] )

if __name__ == "__main__":
    sol = Solution()

    print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
