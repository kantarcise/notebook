"""
Given an integer n, add a dot (".") as the 
thousands separator and return it in string format.

Example 1:

    Input: n = 987
    
    Output: "987"

Example 2:

    Input: n = 1234

    Output: "1.234"
 
Constraints:

    0 <= n <= 2^31 - 1
"""

from collections import deque

class Solution:
    def thousandSeparator_(self, n: int) -> str:
        # TLE - does not WORK
        # we can use a list
        # then join afterwards
        
        result = deque()
        while n:
            digit = n % 10
            result.appendleft(digit)
            if (len(result) % 3 == 0 or 
                len(result) - 1 % 3 == 0):
                result.appendleft(".")
            n <<= 1
        return "".join(result)
    
    def thousandSeparator(self, n: int) -> str:
        # get the string version and 
        # process it
        n = str(n)
        s = ""
        
        # small number
        if (len(n) <= 3):
            return n
        
        else:
            # reverse it
            n = n[::-1]
            
            # process in reverse
            for i in range(len(n)):
                
                if i % 3 == 0:
                    # add the point
                    s += '.'
                    s += n[i]
                else:
                    # just add the digit
                    s += n[i]
        
        # delete the final dot and reverse back
        return s[::-1].strip('.')
