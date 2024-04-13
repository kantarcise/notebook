"""
Implement pow(x, n), which calculates x raised to 
the power n (i.e., xn).

Example 1:

    Input: x = 2.00000, n = 10
    
    Output: 1024.00000

Example 2:

    Input: x = 2.10000, n = 3
    
    Output: 9.26100

Example 3:

    Input: x = 2.00000, n = -2
    
    Output: 0.25000
    
    Explanation: 
        
        2-2 = 1/22 = 1/4 = 0.25

Constraints:

    -100.0 < x < 100.0
    
    -2^31 <= n <= 2^31-1
    
    n is an integer.
    
    Either x is not zero or n > 0.
    
    -10^4 <= xn <= 10^4

Takeaway:

    If the power is negative, just return 1 / result

    you can solve the problem, using recursion

    condition is based on the power and it getting halved.

    If you are writing a while block, you have 
    to exit it at some point.
"""

class Solution:

    def myPow_(self, x: float, n: int) -> float:
        # cool idea
        # does not work
        
        # if n is negative
        # x ^ n  = 1 / x ^ n
        
        if n == 0:
            return 1
        if x == 0 :
            return 0
        
        result = 1
        while x > 1:
            result *= self.myPow(x, n//2)
        
        # deal with negative case
        return result if x>0 else 1 / result

    def myPow(self, x, n) -> float:
        # if n is negative
        # x ^ n => 1 / x ^ n
        
        def helper(x, n):
            if n == 0: return 1
            if x == 0: return 0
            
            result = helper(x, n//2)
            result *= result
            return x * result if n % 2 == 1 else result
        
        sol = helper(x, abs(n))
        return sol if n >= 0 else 1 / sol
