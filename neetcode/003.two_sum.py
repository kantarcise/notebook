"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums , target):
        """It took me some time but I got ir.
        
        Basic idea is to use elements and find the remainder from the target.

        index can be used with a START index to find the (possibly) second element

        these indexes are using o(n) worst case, NOT GOOD
        """
        answer_indexes = []
        remainder = None
        # traverse the array and try to find the other part
        for i, elem in enumerate(nums):
            remainder = target - elem
            if remainder in nums[i+1:]:
                answer_indexes.append(nums.index(elem))
                answer_indexes.append(nums.index(remainder, nums.index(elem)+1))
                return answer_indexes
    
    def twoSumBetter(self, nums, target):
        # keys as numbers and indexes as values
        nums_to_index = {}

        # i is one of the answers
        for i , elem in enumerate(nums):
            complement = target - elem
            # if complement is in out dict
            if complement in nums_to_index:
                # order does not matter
                # return them!
                return [nums_to_index[complement], i]
            # if not, just add the element to our dictionary
            nums_to_index[elem] = i


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))
    print(sol.twoSumBetter([2,7,11,15], 9))
    print(sol.twoSumBetter([3,2,4], 6))
    print(sol.twoSumBetter([3,3], 6))

