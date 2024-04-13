"""
Given an array nums containing n distinct numbers in the 
range [0, n], return the only number in the range that is missing 
from the array.

Example 1:

    Input: nums = [3,0,1]
    
    Output: 2
    
    Explanation: 
        
        n = 3 since there are 3 numbers, so all 
        numbers are in the range [0,3]. 2 is the missing number 
        in the range since it does not appear in nums.

Example 2:

    Input: nums = [0,1]
    
    Output: 2
    
    Explanation: 
        
        n = 2 since there are 2 numbers, so all 
        numbers are in the range [0,2]. 2 is the missing number 
        in the range since it does not appear in nums.

Example 3:

    Input: nums = [9,6,4,2,3,5,7,0,1]
    
    Output: 8
    
    Explanation: 
        
        n = 9 since there are 9 numbers, so all 
        numbers are in the range [0,9]. 8 is the missing number 
        in the range since it does not appear in nums.

Constraints:

    n == nums.length
    
    1 <= n <= 10^4
    
    0 <= nums[i] <= n
    
    All the numbers of nums are unique.
 
Follow up: Could you implement a solution using only O(1) 
extra space complexity and O(n) runtime complexity?

Takeaway:

    number ^ number = 0

    If you XOR a value with itself, all corresponding bits 
    will cancel each other out, resulting in zero.

    number ^ 0 = number

    XORing any value with zero leaves the value unchanged. 

    For this question, you can use the property where 
    the sum of the sequence is missing_number away from the 
    full range sum
"""

class Solution:
    def missingNumber_(self, nums: list[int]) -> int:
        # works

        # Sort the array in ascending order
        nums.sort()
        
        # Initialize a variable to represent the missing element
        missing_elem = -1
        
        # Iterate through the sorted array
        for element in nums:
            # Calculate the difference between the current element and the missing element
            difference = element - missing_elem
            
            # If the difference is not 1, then we found the missing number
            if difference != 1:
                return element - 1
            
            # Update the missing element
            missing_elem += 1
        
        # If the loop completes, the missing number is the next consecutive number
        return nums[-1] + 1
    
    def missingNumber(self, nums: list[int]) -> int:
        # works and really fast

        # the sum of the sequence is only 
        # missing_number away from the full range 
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)
    
    def missingNumber__(self, nums: list[int]) -> int:
        # we can use a set too, works

        # n distinct numbers
        # [0, 1, 2, 3, ]
        hset = set(nums)
        for i in range(len(nums) + 1):
            if i not in hset:
                return i
