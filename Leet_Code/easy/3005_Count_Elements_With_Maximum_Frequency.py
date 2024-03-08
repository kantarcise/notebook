"""
You are given an array nums consisting 
of positive integers.

Return the total frequencies of elements in nums such 
that those elements all have the maximum frequency.

The frequency of an element is the number of 
occurrences of that element in the array.

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 
2 which is the maximum frequency in the array.

So the number of elements in the array with 
maximum frequency is 4.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 5

Explanation: All elements of the array have a frequency 
of 1 which is the maximum.

So the number of elements in the array with 
maximum frequency is 5.

Constraints:

  1 <= nums.length <= 100
  1 <= nums[i] <= 100

Takeaway:

  Both Counter and {} will work

"""
from collections import Counter

class Solution:
    def maxFrequencyElements_(self, nums: list[int]) -> int:
        # with counter
        c = Counter(nums)
        most_common_count = c.most_common(1)[0][1]
        result = 0
        for k, v in c.items():
            if v >= most_common_count:
                result += v
        return result
    
    def maxFrequencyElements(self, nums: list[int]) -> int:
        # with just dictionaries
        freq_map = {}
        for number in nums:
            freq_map[number] = freq_map.get(number, 0) + 1

        max_count = freq_map[max(freq_map, key  = lambda x : freq_map[x])]

        # or you can:
      
        # max_key = max(freq_dict, key=freq_dict.get)
        # max_count_from_key = freq_map[max_key]
        
        result = 0

        for k, v in freq_map.items():
            if v >= max_count:
                result += v
        return result
