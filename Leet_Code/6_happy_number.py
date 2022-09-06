# 202. Happy Number
# Easy
# 
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.
# 
# Return true if n is a happy number, and false if not.

# Example 1:
# 
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
# Example 2:
# 
# Input: n = 2
# Output: false

class Solution:
    def isHappy(self, n: int) -> bool:
        """
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
