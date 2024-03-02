"""
Given an array of integers nums, return 
the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: 
  There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:

Input: nums = [1,2,3]
Output: 0
 
Constraints:

  1 <= nums.length <= 100
  1 <= nums[i] <= 100

Takeaway:

  Counter and Combinations

"""

from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        res  = 0
        for k , v in c.items():
            # if there are more than 1 of an element
            if v > 1:
                # Combination formula, C(v, 2), the number of ways 
                # to choose 2 items from a set of v items.
                # Dividing by 2 (// 2) is necessary because the 
                # order of the pair does not matter. 
                res += (v * (v-1)) // 2
                
        return res
