# 9. Palindrome Number
# Easy
# 
# Given an integer x, return true if x is palindrome integer.
# 
# An integer is a palindrome when it reads the same backward as forward.
# 
#    For example, 121 is a palindrome while 123 is not.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Not the fastest.
# Change the int to a str and check if it's equal with reversed version.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==(str(x))[::-1]
            
