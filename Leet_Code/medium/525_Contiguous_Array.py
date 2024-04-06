"""
Given a binary array nums, return the maximum length of a 
contiguous subarray with an equal number of 0 and 1.

Example 1:

    Input: nums = [0,1]
    Output: 2
    
    Explanation: 
        [0, 1] is the longest contiguous subarray with an 
          equal number of 0 and 1.

Example 2:

    Input: nums = [0,1,0]
    Output: 2
    
    Explanation: 
    
        [0, 1] (or [1, 0]) is a longest contiguous subarray 
        with equal number of 0 and 1.
 
Constraints:

    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.

Takeaway:
  
    Using pointers for each index, designed for them.

"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # we are looking for contiguous subarray
        
        # we just need to return the lenght of it
        
        # [1,1,1,1]
        
        # [1,0,1,1,1,1,0,0,0,0]
        # we need to be able to see the future 
        # to add these 1's 
        
        # the solution does not start 
        # from beginning, not necessarily 
        
        zeros, ones = 0, 0
        res = 0
        
        # count the difference to the ending subarray
        difference_index = {} # count[1] - count[0] -> index
        
        for i, elem in enumerate(nums):
            
            if elem == 0:
                zeros += 1
            else:
                ones += 1
            
            # if we never encountered this difference
            if ones - zeros not in difference_index:
                difference_index[ones - zeros] = i
                
            if ones == zeros:
                res = ones + zeros
                
            # we already added the difference so we can use
            # else instead of elif
            # elif one - zero in difference_index:
            else:
                index = difference_index[ones - zeros]
                res = max(res, i - index)
                
        return res
