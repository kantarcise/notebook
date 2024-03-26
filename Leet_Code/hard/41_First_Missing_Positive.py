"""
Given an unsorted integer array nums. Return the smallest 
positive integer that is not present in nums.

You must implement an algorithm that runs 
in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:

  1 <= nums.length <= 10^5
  -2^31 <= nums[i] <= 2^31 - 1

Takeaway:

  sets would be cool, but if you are constrained,
  you gotta think manipulation.

"""

class Solution:
    def firstMissingPositive_(self, nums: List[int]) -> int:
        # works but not CONstant space!
        # make a set
        s = set(nums)
        for i in range(1, len(nums)+1):
            if i not in s:
                return i
        return i+1
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        # how can we make it constant space?
        # we can manipulate the list given to us
        
        # swap elements in the list
        def swap(container, i, j):
            container[i], container[j] = container[j], container[i]
        
        n = len(nums)
        
        # Place each positive integer i at index i-1 if possible
        # we want to make 
        # [3,4,-1,1] -> [1, -1, 3, 4]
        # because we know the answer is between [1, n+1]
        for i in range(n):
            # while the element is within range
            # and
            # element is not equal to, element at the index it's supposed to
            # i = 0 , 3 is within range, 3 != -1
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        
        # now that we have the list as we want it,
        # lets find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers from 1 to n are present, return n + 1
        return n + 1
