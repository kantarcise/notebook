"""
Given an array nums of integers, return how many of 
them contain an even number of digits.

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2

Explanation: 

  12 contains 2 digits (even number of digits). 
  345 contains 3 digits (odd number of digits). 
  2 contains 1 digit (odd number of digits). 
  6 contains 1 digit (odd number of digits). 
  7896 contains 4 digits (even number of digits). 

Therefore only 12 and 7896 contain an even number of digits.

Example 2:

Input: nums = [555,901,482,1771]
Output: 1 

Explanation: 
  Only 1771 contains an even number of digits.
 
Constraints:

  1 <= nums.length <= 500
  1 <= nums[i] <= 105

Takeaway:

Yeah string works but STOP.

Just divide by 10 MAN.
"""

class Solution:
    def findNumbers_(self, nums: List[int]) -> int:
        # 4 - 1 digit
        # 34 - 2 digits - 123456789
        # 100 - 3 digits - 10, 11, 12 , ... ,99
        
        result = 0
        # I can use a string method
        for elem in nums:
            if len([c for c in str(elem)]) % 2 == 0:
                result += 1
        return result
    
    def findNumbers(self, nums: List[int]) -> int:
        # with division by 10
        result = 0
        
        def digits(number):
            # find number of digits in positive number
            if number == 0: return 1
            res = 0
            while number:
                number //= 10
                res += 1
            return res
        
        for elem in nums:
            if digits(elem) % 2 == 0:
                result += 1
                
        return result
