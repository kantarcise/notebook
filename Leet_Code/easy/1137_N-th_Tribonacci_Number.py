"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

    Input: n = 4
    
    Output: 4
    
    Explanation:
    
        T_3 = 0 + 1 + 1 = 2

        T_4 = 1 + 1 + 2 = 4

Example 2:

    Input: n = 25
    
    Output: 1389537

Constraints:

    0 <= n <= 37

    The answer is guaranteed to fit within a 
        32-bit integer, ie. answer <= 2^31 - 1.

Takeaway:

    Tuple unpacking OR dp
"""

class Solution:
    def tribonacci_(self, n: int) -> int:
        # dp solution
        
        # edge cases
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        
        tri = [0] * (n+1)
        tri[0] = 0
        tri[1] = 1
        tri[2] = 1
        
        for i in range(3, n+1):
            tri[i] = tri[i-1] + tri[i-2] + tri[i-3]
            
        return tri[n]
    
    def tribonacci(self, n: int) -> int:
        # can we solve it in O(1) space ?
        # sure!
        
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        
        for i in range(3, n + 1):
            
            # 0, 1, 1 
            # a and b will basically just move 
            # c will be the total of all 3
            a, b, c = b, c, a + b + c
        
        return c
    
sol = Solution()
print(sol.tribonacci(25))
