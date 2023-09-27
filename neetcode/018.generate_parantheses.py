"""
Given n pairs of parentheses, write a function to generate
 all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]


Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

Takeaway:

Well-formed parentheses combinations have an equal number of 
opening '(' and closing ')' parentheses.

You need to ensure that at any point while generating combinations, the 
number of closing ')' parentheses does not exceed the number of 
opening '(' parentheses.

The code demonstrates a backtracking approach, which is a common technique
 for generating combinations recursively.

The generateParenthesis method uses a backtracking algorithm and a stack
 (stack) to keep track of the current combination. It recursively generates
  combinations, adding '(' when possible and ')' when it meets the criteria.

"""

import random

class Solution:

    def generateParenthesis(self, n: int):
        # the rule for all parantheses are that they should be closed.
        # we have the number of pairs.
        # we can select randomly the number of open close pairs.

        # basically, the open parantheses count should match the close parantheses 
        # at any given point

        # if pair is 1 
        # answer is ["()"]

        # if pair is 2
        # answer could be ["()()"] or ["(())"]

        # first element should always be open parathesis.
        # remaining elements from the number of pairs should be either open or close.

        # we can only add a closing paranthesis if we have an open paranthesis previously.

        # Let's use backtracking

        # Rule 1 : n open n close
        # Rule 2 : close < open

        # summary from neet
        # only add open parantheses if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n

        # let's make a stack with list
        stack = []

        result = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                result.append("".join(stack))   
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()

            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n +1)
                stack.pop()

        backtrack(0,0)
        return result

    # this is faster because it has no stack.
    def generateParenthesis_(self, n: int):
        """
        The idea is to add ')' only after valid '('
        We use two integer variables left & right to see how many '(' & ')' are in the current string
        If left < n then we can add '(' to the current string
        If right < left then we can add ')' to the current string"""
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                dfs(left + 1, right, s + "(")
            if right < left:
                dfs(left, right + 1, s + ")")


        res = []
        dfs(0, 0, "")
        return res

if __name__ == "__main__":
    sol = Solution()

    print(sol.generateParenthesis(3))
    print(sol.generateParenthesis(1))

    print(sol.generateParenthesis_(3))
    print(sol.generateParenthesis_(1))

