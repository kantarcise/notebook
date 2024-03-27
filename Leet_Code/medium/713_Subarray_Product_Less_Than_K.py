"""
Given an array of integers nums and an integer k, return 
the number of contiguous subarrays where the product of 
all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
  [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
  Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

Constraints:

  1 <= nums.length <= 3 * 10^4
  1 <= nums[i] <= 1000
  0 <= k <= 10^6

Takeaway:

  You can go brute force and calculate all the subarrays.

  Or you can use a sliding window!

"""
class Solution:
    def numSubarrayProductLessThanK_(self, nums: List[int], k: int) -> int:
        # brute force, calculate all subarrays
        # memory limit exceeded
        subarrays = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                subarrays.append(nums[i:j])
        
        def multiply(my_list):
            product = 1
            for elem in my_list:
                product *= elem
            return product
        
        result = 0
        for l in subarrays:
            if multiply(l) < k:
                result +=1
                
        return result
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # how can we avoid exceeding memory error?
        # do we have to calculate all subarrays? 
        
        # edge case
        if k <= 1:
            return 0
        
        # let's use a sliding window!
        result = 0
        product = 1  
        left = 0   # Left pointer of the window
        
        for right, num in enumerate(nums):
            # expand the window
            product *= num
            # if we went over on the product
            while product >= k:
                # undo the effect from leftmost element
                product /= nums[left]
                # increase left, shrink window
                left += 1
            
            #  the length of the current window, 
            # which is right - left + 1, represents the number 
            # of valid subarrays ending at the current right index.
            result += right - left + 1 
        
        return result
