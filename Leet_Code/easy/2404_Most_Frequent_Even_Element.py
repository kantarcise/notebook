"""
Given an integer array nums, return the 
most frequent even element.

If there is a tie, return the smallest one. 
If there is no such element, return -1.

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
  The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
  We return the smallest one, which is 2.

Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4

Explanation: 4 is the even element appears the most.

Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1

Explanation: There is no even element.
 
Constraints:

  1 <= nums.length <= 2000
  0 <= nums[i] <= 105

Takeaway:

freq map.

double condition loop. Elegant.

"""

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # we need to hold frequency - hashmap
        # return most freq, even
        # if tie - return smaller
        
        hmap = {elem: 0 for elem in nums if elem % 2 == 0}
        
        for elem in nums:
            if elem % 2 == 0:
                hmap[elem] += 1
                
        most_frequent_even = float('-inf')
        max_frequency = 0

        for num, freq in hmap.items():
            
            # if more frequent 
            # OR
            # same frequent and smaller number
            if freq > max_frequency or (freq == max_frequency and num < most_frequent_even):
                most_frequent_even = num
                max_frequency = freq

        return most_frequent_even if most_frequent_even != float("-inf") else -1
