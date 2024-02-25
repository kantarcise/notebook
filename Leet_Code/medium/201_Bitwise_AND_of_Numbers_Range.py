"""
Given two integers left and right that represent the 
range [left, right], return the bitwise AND of all numbers 
in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4

Example 2:

Input: left = 0, right = 0
Output: 0

Example 3:

Input: left = 1, right = 2147483647
Output: 0

Constraints:

0 <= left <= right <= 231 - 1

Takeaway:

 The idea is using the identity element for AND operation
 You got to know about shifting.

"""

from copy import deepcopy

class Solution:
    def rangeBitwiseAnd_(self, left: int, right: int) -> int:
        # does not work - first try
        
        # 5 -7 
        # result 4 - how ?
        
        # 101 - 110 -  111
        
        # 100
        
        # basically - biggest power of two in the range is the result
        
        small_numbers = {0 , 1, 2}
        if left in small_numbers and right in small_numbers:
            return left & right
        
        i = 2
        potential = []
        while i <= (2*31 - 1):
            if i > right:
                break
            if left <= i and i <= right:
                potential.append(i)
            i *= 2
            # print(i)
            
        if potential:
            return max(potential)

        return 2 ** (len(bin(left)[2:]) - 1)
    
    def rangeBitwiseAnd__(self, left: int, right: int) -> int:
        # brute force -TLE
        
        res = left
        for elem in range(left + 1, right + 1):
            res &= elem
            
        return res
    
    def rangeBitwiseAnd____(self, left: int, right: int) -> int:
        # does NOT work
        
        # edge cases
        
        small_numbers = {0 , 1, 2}
        if left in small_numbers and right in small_numbers:
            return left & right
        
        # 0 1
        # 2 3 
        # 4 5 6 7 
        # 8 9 10 11 12 13 14 15
        # 16 ...
        
        # 5 - 7
        # 4
        
        # powers of 2 is the dominant
        
        # find the biggest power of 2
        
        small_power = 2 
        while small_power < left:
            small_power *= 2
        
            if small_power > left:
                small_power = small_power // 2
                break
        
        big_power = deepcopy(small_power)
        while big_power < right:
            big_power *=2
            
        print(small_power)
        print(big_power)
            
        return small_power & big_power

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # most significant bits are least likely to change
        
        # the range will tell you how many 0's
        # are going to occur in a bit
        
        #   100
        #   101
        #   110
        #   111
        #  1000 
        # &____
        
        # while left and right is not equal
        # there must be a 0 in that bit
        # shift right and left to the left by 1
        # compare again
        
        # 1001
        # 1010
        
        shift_count = 0
        while left != right:
            # basically, shift both numbers and 
            # increment shift count
            left = left >> 1
            right = right >> 1
            shift_count  += 1
        
        # when left and right is equal, you can use 
        # left or right
        # just make sure to return all chopped pieces
        return left << shift_count
