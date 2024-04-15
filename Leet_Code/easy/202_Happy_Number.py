"""
Write an algorithm to determine if a 
number n is happy.

A happy number is a number defined by 
the following process:

    Starting with any positive integer, replace 
        the number by the sum of the squares 
        of its digits.
    
    Repeat the process until the number equals 
        1 (where it will stay), or it loops endlessly 
        in a cycle which does not include 1.

    Those numbers for which this process ends 
        in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

    Input: n = 19
    
    Output: True
    
    Explanation:
        
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

Example 2:

    Input: n = 2
    
    Output: False

Constraints:

    1 <= n <= 2^31 - 1

Takeaway:

    To detect a cycle, set is wonderful!
"""

class Solution:
    def isHappy_(self, n: int) -> bool:
        # this cannot escape the infinite loop
        # does NOT Work

        # get all digits of n
        # sum of squares
        # update n

        def get_all_digits(number):
            digits = []
            
            while number:
                remainder = number % 10
                digits.append(remainder)
                number //= 10
            
            return digits 

        temp = n

        while n != 1:
            dig = get_all_digits(n)
            n = sum((elem * elem for elem in dig))
                
        return True

    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                # end of loop!
                return True
            elif n in seen:
                # we knew this from before
                return False
            else:
                # add the current number to set
                seen.add(n)
                # use strings to access digits simply
                n = sum(int(i)**2 for i in str(n))

sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))