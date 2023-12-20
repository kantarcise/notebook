"""
Given an integer array nums and an integer k, return true 
if there are two distinct indices i and j in the array such 
that nums[i] == nums[j] and abs(i - j) <= k. 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

Takeaway:

You can do amazing things with hashmaps

enumerate is magical as always.
"""

class Solution:
    def containsNearbyDuplicate_(self, nums: List[int], k: int) -> bool:
        # need work on hashmaps
        # and sliding windows
        # two conditions
        if k > len(nums):
            if len(nums) != set(nums):
                return True
        
        for i in range(len(nums) - k + 1):
            if len(nums[i: i + k + 1]) != len(set(nums[i:i+ k + 1])):
                return True
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # from a homie
        # map numbers to indexes
        d = {}

        for i, n in enumerate(nums):
            # if the new value is in the map and 
            # the index difference is smaller than k
            if n in d and abs(i - d[n]) <= k:
                return True
            else:
                d[n] = i
        return False
