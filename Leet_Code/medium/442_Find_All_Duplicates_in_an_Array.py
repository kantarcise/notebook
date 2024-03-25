"""
Given an integer array nums of length n where all 
the integers of nums are in the range [1, n] and each 
integer appears once or twice, return an array of 
all the integers that appears twice.

You must write an algorithm that runs in O(n) 
time and uses only constant extra space.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []
 
Constraints:

  n == nums.length
  1 <= n <= 10^5
  1 <= nums[i] <= n
  Each element in nums appears once or twice.

Takeaway:

  Sets, dicts, Counter.

  If mambo jambo, think about pointers and indexes!

"""

class Solution:
    def findDuplicates_(self, nums: List[int]) -> List[int]:
        # just use a set ?
        # not constant space !
        my_set = set()
        result = []
        for elem in nums:
            if elem in my_set:
                result.append(elem)
            my_set.add(elem)
        return result
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # cannot sort it.
        # this works
        # how about using indexes ?
        result = []
        for num in nums:
            # this index i will be only same if nums is a duplicate
            i = abs(num) - 1
            if nums[i] < 0:
                # if we encountered this index before
                result.append(abs(num))
            else:
                # first time seeing this number
                nums[i] = -nums[i]
        return result
