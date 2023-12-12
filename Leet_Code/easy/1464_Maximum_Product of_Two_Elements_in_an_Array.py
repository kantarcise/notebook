"""
Given the array of integers nums, you will choose two different indices i and
j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will 
get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the 
maximum value of (5-1)*(5-1) = 16.

Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

Takeaway:

Tuple unpacking is great!

A question to ask yourself, is the answer alreadyt within the question?

"""
class Solution:
    def maxProduct_(self, nums: List[int]) -> int:
        # this is o(nlogn)
        # can we do better?
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] -1)
    
    def maxProduct(self, nums):
        # the answer is already within the list.
        first = 0
        second = 0
        for num in nums:
            # if current number is bigger or equal to first (biggest)
            if first <= num:
                # set the biggest and bump the current biggest to second
                first, second = num, first
            # if te current number is bigger than second biggest
            elif second < num:
                # set second biggest
                second = num
        return (first-1) * (second-1)
