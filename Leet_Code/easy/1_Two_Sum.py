"""
Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly 
one solution, and you may not use the same 
element twice.

You can return the answer in any order.

Example 1:

    Input: nums = [2,7,11,15], target = 9
    
    Output: [0,1]
    
    Explanation: 
    
        Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

    Input: nums = [3,2,4], target = 6
    
    Output: [1,2]

Example 3:

    Input: nums = [3,3], target = 6
    
    Output: [0,1]

Constraints:

    2 <= nums.length <= 10^4
    
    -10^9 <= nums[i] <= 10^9
    
    -10^9 <= target <= 10^9
    
    Only one valid answer exists.

Follow-up: 
    
    Can you come up with an algorithm that is 
        less than O(n^2) time complexity?

Takeaway:

    dictionaries are wonderful.

    you can fill them while traversing.

"""

class Solution:
    def twoSum__(self, nums: list[int], target: int) -> list[int]:
        # we are looking for indices
        # use every element once

        # this solution works, but a bit messy

        indices_map = {elem: index for index, elem in enumerate(nums)}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in indices_map:
                if i != indices_map[remainder]:
                    return [i, indices_map[remainder]]

    def twoSum_(self, nums: list[int], target: int) -> list[int]:
        # this works too
        # we do not have to populate 
        # the dict right away
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                # found the solution
                return [num_map[complement], i]

            # otherwise, just add the element to map
            num_map[num] = i
        
        return None
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # even more advanced version.
        map = {}
        # index and element traversal
        for i, n in enumerate(nums):
            if n in map:
                return [map[n], i]
            else:
                map[target - n] = i

sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9)) # [0, 1]
print(sol.twoSum(nums = [3,2,4], target = 6)) # [1, 2]