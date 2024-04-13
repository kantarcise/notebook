"""
Given an integer array nums, find a subarray that has the 
largest product, and return the product.

The test cases are generated so that the answer 
will fit in a 32-bit integer.

Example 1:

    Input: nums = [2,3,-2,4]

    Output: 6

    Explanation: [2,3] has the largest product 6.

Example 2:

    Input: nums = [-2,0,-1]

    Output: 0

    Explanation: The result cannot be 2, because [-2,-1] is 
    not a subarray.
 
Constraints:

    1 <= nums.length <= 2 * 10^4

    -10 <= nums[i] <= 10
    
    The product of any prefix or suffix of nums is guaranteed 
        to fit in a 32-bit integer.

Takeaway:

    Thinking about the solution, might give you the 
    brute force solution

    Thinking about the question might give you the DP solution.
"""

class Solution:

    def maxProduct_(self, nums: list[int]) -> int:
        # brute force
        # NOT WORKING - GG
        """Find the subarray that has the largest product 
        and return the product
        """
        # A subarray is a contiguous part of array.
        # brute force
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            if nums[0] * nums[1] > 0:
                return nums[0] * nums[1]
            elif nums[0] * nums[1] < 0:
                return max(nums)
            else:
                return 0 if (nums[0] < 0 or nums[1] < 0) else max(nums) 
        
        result = 0
        for i in range(len(nums)):
            # for all subarrays containing ith item
            for j in range(i+1, len(nums)):
                # fix this
                # Calculate the product of the subarray nums[i:j+1]
                temp_result = 1
                for k in range(i, j + 1):
                    temp_result *= nums[k]
                    
                result = max(result , temp_result)
        return result
    
    def maxProduct(self, nums: list[int]) -> int:
        # we gotta keep track of both min and max values in mind
        # because consecutive negatives are alternating the result sign
        # 0 is the edge case, it will destroy the streak
        
        result = max(nums) # most basic case is not 0
        
        # for positive and negative values, keep both sides of the product
        current_min, current_max = 1, 1
        
        for n in nums:
            # 0 is destroying our streak
            if n == 0:
                current_min, current_max = 1, 1
                continue
            
            # because current max will change
            # you can use a tuple here to avoid usage of temp
            temp  = current_max * n
            # it has n to it too because n could be opposite signed value
            current_max = max(n * current_max, n * current_min, n)
            # it has n to it too because n could be opposite signed value
            current_min = min(temp, n * current_min, n)
            
            result = max(result, current_max)
        
        return result
    
    def maxProduct__(self, nums: list[int]) -> int:
        # from a homie
        if not nums:
            return 0
        maxv = minv = res = nums[0]
        for n in nums[1:]:   
            # this tuple approach gets rid of temp value         
            maxv, minv = max(n, maxv * n, minv * n), min(n, maxv * n, minv * n)
            res = max(res, maxv)
        return res
