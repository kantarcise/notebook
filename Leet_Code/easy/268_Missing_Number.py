"""
Given an array nums containing n distinct numbers in the 
range [0, n], return the only number in the range that 
is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers 
    are in the range [0,3]. 2 is the missing number in 
    the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers 
    are in the range [0,2]. 2 is the missing number in 
    the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all 
  numbers are in the range [0,9]. 8 is the missing number 
  in the range since it does not appear in nums.
 
Constraints:

  n == nums.length
  1 <= n <= 104
  0 <= nums[i] <= n
  All the numbers of nums are unique.
 
Follow up: Could you implement a solution using only 
  O(1) extra space complexity and O(n) runtime complexity?

Takeaway:

  When told about a piece in range, always remember (n)(n + 1)/2

  Brute force would be just to use a set and traverse input.

  Bitwise operators - XOR magic
"""

class Solution:
    def missingNumber___(self, nums: List[int]) -> int:
        # incredibly slow
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
            
    def missingNumber__(self, nums: List[int]) -> int:
        # way faster and smarter
        n = len(nums)
        # just return the expected total subtracted by current sum
        return (n * (n + 1)) // 2 - sum(nums)
    
    def missingNumber_(self, nums : list[int]) -> int:
        seen = set(nums)

        for i in range(len(nums) + 1):
            if i not in seen:
                return i
    
    def missingNumber(self, nums: list[int]) -> int:
        # what do we know ?
        # a ^ a = 0
        # a ^ 0 = a

        # in a range of numbers:
        # only a single number will not have 
        # and index and a value together

        # example
        # [1, 3, 2]

        # starting from 3 than traversing the list
        # 3 ^ 0 ^ 1 ^ 3 ^ 1 ^ 2 ^ 2

        # only non pair is the answer -> 0! 

        # take the initial value as the length of nums
        result = len(nums)
        
        # xor all numbers and indexes in the list

        for idx, num in enumerate(nums):
            result ^= idx ^ num
        
        return result
