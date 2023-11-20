"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of 
its prime factors are limited to 2, 3, and 5.

Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7. 

Constraints:

-231 <= n <= 231 - 1

Takeaway:



"""

class Solution:
    def isUgly_(self, n: int) -> bool:
        # my first approach
        # is prime
        # 7 8 9 11
        def find_all_factors(n:int) -> list[int]:
            # not complete
            (_, __) = divmod(n, 2) # (n/2 , 0 or 1)
            pass
        
        if n == 1:
            return True
        result = find_all_factors(n)
        return max(result) < 5
    
    def isUgly__(self, n:int) -> bool:
        # my second approach, wrong..
        if n == 1:
            return True
        if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:   
            return True
        else:
            return False
        
    def _isUgly(self, n: int) -> bool:
        # time limit exceeded
        if n == 1:
            return True

        # Check divisibility by 2, 3, and 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1
    
    def isUgly(self, num: int) -> bool:
        # to be ugly, have to be positive
        if (num == 0):
            return False
        # divide until you find all possible powers for the allowed primes.
        while ((num % 5) == 0):
            num //= 5
        while ((num % 3) == 0):
            num //= 3
        while ((num % 2) == 0):
            num //= 2
      # this way, for n = 1, will return True aswell  
      return (num == 1)
