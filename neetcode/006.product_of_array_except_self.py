"""
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums except nums[i].

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
    
    The product of any prefix or suffix of nums is 
        guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)

Takeaway:

    If you multiply every element to the left and to the right, 
    you will get the product of all elements.

"""

import random

# for an extra test
from time import perf_counter_ns

class Solution:
    def productExceptSelf_(self, nums: list[int]) -> list[int]:
        # can we brute force it?
        # yeah, but it is not o(n), here it is anyway
        n = len(nums)
        result = [1] * n
        for i in range(n):
            product = 1 
            for j in range(n):
                if j != i:
                    product *= nums[j]
            result[i] = product
        
        return result


    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # here is how you solve it in o(n)

        # how can we solve it in o(n) ? 
        # we basically cannot have nested loops,
        # we can iterate over the list only. No sorting.
        
        # compartmentalize the problem!

        n = len(nums)
        result = [1] * n

        # compute products to the left of each element
        # and store it in result
        left_product = 1
        for i in range(n):
            # multiply the result element with current 
            # left_product
            result[i] *= left_product
            # adjust the left product with given list element
            left_product *= nums[i]

        # compute products to the left of each element
        # and store it in result
        right_product = 1

        # in backwards:
        for i in range(n-1, -1, -1):
            # multiply the result element with current 
            # left_product
            result[i] *= right_product
            # adjust the left product with given list element
            right_product *= nums[i]

        return result


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.productExceptSelf_(nums = [1,2,3,4]))
    print(sol.productExceptSelf_(nums = [-1,1,0,-3,3]))
    
    a = perf_counter_ns()
    print(sol.productExceptSelf_(random.sample(range(1,234623576), 30)))
    b = perf_counter_ns()
    print(F"Brute force took {(b - a)} nanoseconds")
    
    print(sol.productExceptSelf(nums = [1,2,3,4]))
    print(sol.productExceptSelf(nums = [-1,1,0,-3,3]))
    
    # this will work!
    c = perf_counter_ns()
    print(sol.productExceptSelf(random.sample(range(1,234623576), 30)))
    d = perf_counter_ns()
    print(F"Linear Time solution took {(d - c)} nanoseconds")
