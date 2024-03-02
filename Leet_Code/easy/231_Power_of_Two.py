"""
Given an integer n, return true if it is a 
power of two. Otherwise, return false.

An integer n is a power of two, if there 
exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

Constraints:

  -2^31 <= n <= 2^31 - 1
 
Takeaway:

  Obviously loops. Bitwise operation magic.

Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    def isPowerOfTwo_(self, n: int) -> bool:
        if n == 0: return False
        
        for i in range(31):
            if 2 ** i == n:
                return True
        return False
            
    def isPowerOfTwo__(self, n: int) -> bool:
        # fast   
        if n == 0:
            return False
        
        return '1' not in bin(n)[3:]
    
    def isPowerOfTwo(self, n: int) -> bool:
        # fastest
        return n>0 and n&(n - 1) == 0
