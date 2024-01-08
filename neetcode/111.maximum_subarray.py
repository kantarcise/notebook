"""
Given an integer array nums, find the subarray with the 
largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]

Output: 6

Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Takeaway:

Calculating every single subarray is scary.

You can use a decision tree to solve 
this with a sliding window, kinda.

"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # a decision tree 
        # should we include the current element or not?
        
        # this is like a sliding window solution
        # we remove negative prefixes
        
        result = float("-inf")
        current_sum = 0
        
        for num in nums:
            # include the element OR start a new subarray
            # [-2,1,-3,4,-1,2,1,-5,4]
            # if the number itself is better than 
            # number added to current sum
            # it would be WAY BETTER to start a new subarray just using the number
            current_sum = max(num, current_sum + num)
            
            # result changes at every step
            result = max(result, current_sum)
            
        return result
    
    def maxSubArray_(self, nums: list[int]) -> int:
        # neetcode
        max_sub = nums[0]
        current_sum = 0
        
        for n in nums:
            
            # start over
            if current_sum < 0:
                current_sum = 0
            
            # add the next element
            current_sum += n
            
            # how the result changed in this step
            max_sub = max(max_sub, current_sum)
        return max_sub