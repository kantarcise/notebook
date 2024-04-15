"""
Given an integer x, return true if x is a palindrome, and 
false otherwise.

Example 1:

    Input: x = 121
    
    Output: true
    
    Explanation: 
        
        121 reads as 121 from left to right 
            and from right to left.

Example 2:

    Input: x = -121
    
    Output: false
    
    Explanation: 
        
        From left to right, it reads -121. From right 
            to left, it becomes 121-. 
            
        Therefore it is not a palindrome.

Example 3:

    Input: x = 10
    
    Output: false

    Explanation: 
        
        Reads 01 from right to left. 
        
        Therefore it is not a palindrome.

Constraints:

    -2^31 <= x <= 2^31 - 1

Follow up: 

    Could you solve it without converting 
        the integer to a string?

Takeaway:

    If you want to take two pointers route, you need 
        a container.

    deque is cool.

"""

from collections import deque

class Solution:
    def isPalindrome__(self, x: int) -> bool:
        # most brute force way would be just to 
        # convert number to a string and compare it 
        # to it's reverse
        return str(x) == str(x)[::-1]

    def isPalindrome_(self, x: int) -> bool:
        # negatives cannot be palindrome
        if x < 0 : return False
        
        # we can use two pointers approach

        # make a list from the number
        num_deq = deque()
        
        temp = x
        
        # you can also use divmod() here
        while temp:
            remainder = temp % 10
            num_deq.appendleft(remainder)
            temp //= 10

        # 121 - 1 2 1
        l, r = 0, len(num_deq) - 1

        while l < r:
            if num_deq[l] != num_deq[r]:
                return False
            l += 1
            r -= 1

        return True

    def isPalindrome(self, x: int) -> bool:
        # negatives cannot be palindrome
        if x < 0 : return False
        
        # same idea
        temp = x
        reverse = 0
        
        # build the number, instead of a deque / list
        while temp:
            remainder = temp % 10
            reverse = (reverse * 10) + remainder
            temp = temp // 10
        
        return reverse == x

sol = Solution()

print()
print(sol.isPalindrome__(121))
print(sol.isPalindrome__(-121))

print()
print(sol.isPalindrome_(121))
print(sol.isPalindrome_(-121))

print()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))