"""
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without 
making a copy of the array.

Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:

    Input: nums = [0]
    Output: [0]
 
Constraints:

    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1

Takeaway:

    Manual way is meh. Understand two pointers.

"""
class Solution:
    def moveZeroes_(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[j] == 0:
                # move to end
                del nums[j]
                nums.append(0)
            else:
                j += 1
                continue
                
    def moveZeroes(self, nums: List[int]) -> None:
        # nums = [0,1,0,3,12]
        # resulting
        # nums = [1,3,12,0,0]
        
        # a clear version for 2 pointers
        
        left = 0
        for right in range(len(nums)):
            # basically, move every non zero to left
            if nums[right] != 0: 
                # a non zero at index right
                # switch elements from right and left 
                nums[right], nums[left] = nums[left], nums[right]
                # increment left
                left += 1

        return nums
