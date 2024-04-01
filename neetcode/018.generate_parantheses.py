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

    Well-formed parentheses combinations == equal # '(' and ')'.

    Ensure at any point, the number of closing ')' parentheses 
        does not exceed the number of opening '(' parentheses.

    We can use backtracking (a common technique for generating 
        combinations recursively.

    The generateParenthesis method uses a backtracking algorithm 
        and a stack to keep track of the current combination. 
        It recursively generates combinations, adding '(' when 
        possible and ')' when it meets the criteria.

"""

class Solution:

    def generateParenthesis(self, n: int):
        """
        The rule for all parantheses are that they should be closed.
        we have the number of pairs.
        we can select randomly the number of open-close pairs.

        Open parantheses count should match the close 
        parantheses at any given point.

        if pair is 1 answer is ["()"]

        if pair is 2 answer could be ["()()"] or ["(())"]

        First element should always be open parathesis.
        remaining elements from the number of pairs should 
        be either open or close.

        We can only add a closing paranthesis if we 
        have an open paranthesis previously.

        Let's use backtracking

            Rule 1 : n open n close
            Rule 2 : close < open

        Only add open parantheses if open < n
        Only add a closing paranthesis if closed < open
        Valid If open == closed == n
        """

        # let's make a stack with list
        stack = []
        result = []

        def backtrack(open_n, closed_n):
            # base case
            if open_n == closed_n == n:
                result.append("".join(stack))   
                return
            if open_n < n:
                # we can add more opens
                stack.append("(")
                # backtrack from this point
                backtrack(open_n + 1, closed_n)
                # backtrack to the previous state of the stack
                #  before proceeding to the next iteration.
                stack.pop()

            if closed_n < open_n:
                # we can add more closes
                stack.append(")")
                # backtrack from this point too
                backtrack(open_n, closed_n +1)
                # backtrack to the previous state of the stack
                #  before proceeding to the next iteration.
                stack.pop()

        backtrack(0,0)
        return result

    def generateParenthesis_(self, n: int):
	    
        # We can also approach this with decreasing 
        # the number of paranthesis we can have

        s = []
        result = []
        
        def dfs(my_stack, number_left, number_right):
            # base case
            if number_left == 0 and number_right == 0:
                result.append("".join(my_stack))
                return

            # do things
            # add opening parenthesis if available
            if number_left > 0:
                my_stack.append("(")
                dfs(my_stack, number_left - 1, number_right + 1)
                my_stack.pop()

            # add closing parenthesis if available
            if number_right > 0:
                my_stack.append(")")
                dfs(my_stack, number_left, number_right - 1)
                my_stack.pop()

        dfs(s, n, 0)
        return result

    def generateParenthesis__(self, n: int):
        # this is faster because it has no stack.
        """
        The idea is to add ')' only after valid '('
        
        We use two integer variables left & right to 
        see how many '(' & ')' are in the current string.

        If left < n then we can add '(' to the current string
        If right < left then we can add ')' to the current string
        """
        
        # s will be an empty string at start
        def dfs(left, right, s):
            
            # base case to end it
            if len(s) == n * 2:
                res.append(s)
                return
            
            if left < n:
                # after this dfs returns, it will come back
                dfs(left + 1, right, s + "(")
            
            if right < left:
                # after this dfs returns, it will come back
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

    print(sol.generateParenthesis__(3))
    print(sol.generateParenthesis__(1))
