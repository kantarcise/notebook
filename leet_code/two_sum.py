# 1. Two Sum
# Easy
# 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.# # 
# 
# You can return the answer in any order.
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Use enumerate to get the element as well as index.
# Focus on the end, so look for the target - value_of_element in list. 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, value in enumerate(nums):
            remainder = target - nums[i]
            nums[i] = None
            if remainder in nums:
                return [i, nums.index(remainder)]
