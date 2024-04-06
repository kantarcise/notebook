"""
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of 
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and 
without using the division operation.

Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
 
Constraints:

    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed 
      to fit in a 32-bit integer.

Takeaway:

    2 traversal in opposite to get to answer.

"""
class Solution:
    def productExceptSelf_(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1] * n
        
        # for the example 
        # [1,2,3,4]
        
        
        # Compute products to the left of each 
        # element and store in the result array
        
        # result:
        # [1,1,1,1] -> [1,1,2,6]
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]

        # Compute products to the right of each 
        # element and update the result array
        right_product = 1
        for i in range(n-1, -1 , -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        # result:
        # [1,1,2,6] -> [24,12,8,6]
        
        return result
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # from a homie
        # prefix - postfix   
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
