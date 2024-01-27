"""
Given a string s containing only three types of 
characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.

    Any right parenthesis ')' must have a corresponding left parenthesis '('.

    Left parenthesis '(' must go before the corresponding right parenthesis ')'.

    '*' could be treated as a single right parenthesis ')' or a single 
    left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true


Constraints:

    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.


Takeaway:

Using a counter for left and right is cool.

"""

class Solution:
    def checkValidString_(self, s: str) -> bool:
        # neet
        # we basicall y have a joker! 
        # "*" can be both left or right
        
        # we have to have matching number of 
        # right or left paranthesis
        
        # This is the O(n) solution
        
        left_min, left_max = 0, 0 
        
        for c in s:
            if c == "(":
                # it will increase the left count for sure
                left_min, left_max = left_min + 1, left_max + 1
            elif c == ")":
                # wwe have to decrease counts
                left_min, left_max = left_min - 1, left_max - 1
            else:
                # it could be right, could be left
                left_min, left_max = left_min - 1, left_max + 1
                
            if left_max < 0:
                # this should not happen, because if it does
                # we encountered too many rights from the start
                return False
            
            if left_min < 0:
                # reset
                left_min = 0
        
        # we expect left min to be 0
        return left_min == 0
                
    def checkValidString(self, s: str) -> bool:
        # we need to know,
        # how many ')' we are waiting for.
        
        # If we meet too many ')', we can return false directly.
        # If we wait for no ')' at the end, then we are good.


        # Explanation:
        # We count the number of ')' we are waiting for,
        # and it's equal to the number of open parenthesis.
        # This number will be in a range and we count it as [cmin, cmax]

        # cmax counts the maximum open parenthesis,
        # which means the maximum number of unbalanced '(' that COULD be paired.
        # cmin counts the minimum open parenthesis,
        # which means the number of unbalanced '(' that MUST be paired.
        
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0