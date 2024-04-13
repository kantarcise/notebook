"""
Given an integer array nums, return true if you can partition the 
array into two subsets such that the sum of the elements 
in both subsets is equal or false otherwise.

Example 1:

    Input: nums = [1,5,11,5]

    Output: true

    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

    Input: nums = [1,2,3,5]
    
    Output: false

    Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:

    1 <= nums.length <= 200
    
    1 <= nums[i] <= 100

Takeaway:

    THe tabulation solution, starting from the end

    We either add the element or we dont.

    We can use a set() for DP, but we need to keep the set fresh.
"""

class Solution:

    def canPartition_(self, nums: list[int]) -> bool:
        # works, slow
        # we are basically trying to find half of 
        # the sum with some elements
        if sum(nums) % 2:
            # if sum is odd, no way
            return False
        
        # start from backwards and 
        # add each element or do not add it
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            # make a new set for each element,
            # because we are either adding the elements or not
            # starting from old set
            nextDP = set()
            for t in dp:
                # add the element
                nextDP.add(t + nums[i])
                # do not add the element
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False


    def canPartition_(self, nums: list[int]) -> bool:
        # optimized
        # we are basically trying to find half of 
        # the sum with some elements
        if sum(nums) % 2:
            # if sum is odd, no way
            return False
        
        # start from backwards and 
        # add each element or do not add it
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            # make a new set for each element,
            # because we are either adding the elements or not
            # starting from old set
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                # add the element
                nextDP.add(t + nums[i])
                # do not add the element
                nextDP.add(t)
            dp = nextDP
        return False
