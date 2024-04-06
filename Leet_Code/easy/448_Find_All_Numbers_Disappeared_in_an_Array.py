"""
Given an array nums of n integers where nums[i] is in the 
range [1, n], return an array of all the integers in 
the range [1, n] that do not appear in nums.

Example 1:

    Input: nums = [4,3,2,7,8,2,3,1]
    Output: [5,6]

Example 2:

    Input: nums = [1,1]
    Output: [2]
 
Constraints:

    n == nums.length
    1 <= n <= 10^5
    1 <= nums[i] <= n

Takeaway:

    If we are space restricted, we got to work on input itself.

    sets are obvious choice.

"""

class Solution:
    def findDisappearedNumbers__(self, nums: List[int]) -> List[int]:
        expected_nums = set(nums)
        
        result = []
        
        for elem in range(1, len(nums) + 1):
            if elem not in expected_nums:
                result.append(elem)
        
        return result

    def findDisappearedNumbers_(self, nums: List[int]) -> List[int]:
        # really fast solution - but not o(n) memory
        set1 = set(range(1,len(nums)+1))
        set2 = set(nums)

        return list(set1.difference(set2))
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # if we are using constant space, we have to modify input array
        
        # The idea is to use the original array to keep 
        # track of the numbers visited. 
        
        # Since all the numbers are positive intergers, 
        # for every number visited we mark the presence of that 
        # number by negating the number at the index equal 
        # to the current number. 
        
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res
