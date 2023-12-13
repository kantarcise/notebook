"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by 
the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it 
will stay), or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 
Example 1:

Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Example 2:

Input: n = 2
Output: false
 
Constraints:

1 <= n <= 231 - 1

Takeaway:

Using a set for detecting visit is a CLASSIC

a happy number will loop endlessly on 1

a non happy number will loop endlessly on a
cycle which deos not includes 1

Working on digits is possible by either str -> int shenanigans

OR

using Modulo % and Integer division //

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        # a happy number will loop endlessly on 1
        # a non happy number will loop endlessly on a cycle which deos not includes 1
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sum_of_sq(n)
            
            if n == 1:
                return True
        # if we never met a 1 in our set
        return False
            
    def sum_of_sq(self, number):
        # using modulo and integer division to work on digits
        output = 0
        while number:
            digit = number % 10
            digit = digit ** 2
            output += digit
            number = number // 10
        return output
    
    def isHappy_(self, n: int) -> bool:
        # with a homie
        """
        This function evaluates if the number is a Happy Number.
        The function initialises a set, then continues with a while statement,
        breaking where n==1, returning True, or where the number is within the 
        seen set, indicating it has already been seen, returning False. Finally,
        the loop continues using the logic to create a happy number for each value
        of n.
        
        :param n: the number to be evaluated. (int)
        :return outcome: a boolean indicating a happy number. (bool)
        """
        seen = set()
        while True:
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)
                n = sum(int(i)**2 for i in str(n))