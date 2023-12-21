"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of 
the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n). 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3. 

Constraints:

0 <= n <= 30

Takeaway:

Dynamic PRogramming for the boys.

"""

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        memo = [0] * n
        memo[0] , memo[1] = 1, 1 
        for i in range(2, n):
            memo[i] = memo[i-1] + memo[i-2]
        return  memo[n-1]                    

    def fib_(self, n: int) -> int:
        # from a homie, tuple swap
        if n == 0: 
            return 0
        if n <= 2: 
            return 1 
        if n > 2: 
            a, b = 1, 1
            for i in range(n - 2):
                a, b = b, a + b
            return b
