"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more 
than ⌊n / 2⌋ times. You may assume that the majority 
element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear 
time and in O(1) space?

Takeaway:
    Counter.most_common() :relieved:
    
"""

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        # most common returns n most common elements 
        # in a list of tuples
        return c.most_common(1)[-1][0]
    
    def majorityElement_(self, nums):

        c = 0
        elem = nums[0]

        for i in range(len(nums)):
            if (c == 0):
                elem = nums[i]
            if nums[i] == elem:
                c +=1
            else:
                c -=1
        return elem
    
    def majorityElement__(self, nums: List[int]) -> int:
        # o(n log n)
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement_____(self, nums: List[int]) -> int:
        # my really old solution
        return sorted(nums)[len(nums)//2]
