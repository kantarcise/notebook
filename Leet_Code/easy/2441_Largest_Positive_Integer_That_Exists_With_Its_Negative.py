"""
Given an integer array nums that does not 
contain any zeros, find the largest positive 
integer k such that -k also exists in the array.

Return the positive integer k. 

If there is no such integer, return -1.

Example 1:

    Input: nums = [-1,2,-3,3]

    Output: 3

    Explanation: 

      3 is the only valid k we can find in the array.

Example 2:

    Input: nums = [-1,10,6,7,-7,1]

    Output: 7

    Explanation: 
        
        Both 1 and 7 have their corresponding 
        negative values in the array. 
        7 has a larger value.

Example 3:

    Input: nums = [-10,8,6,7,-2,-3]

    Output: -1

    Explanation: 
    
        There is no a single valid k, we return -1.
 
Constraints:

    1 <= nums.length <= 1000
    -1000 <= nums[i] <= 1000
    nums[i] != 0

Takeaway:

    Containment check, set. A classic.

    Tenary operator.

"""
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # make a set
        # make a result list
        # check condition
        # return max
        # time o(n) - space o(n)
        # is time o(n) - space o(1) possible?
        
        s, result = set(), []
        for elem in nums:
            if -elem in s:
                result.append(abs(elem))
            s.add(elem)
        return max(result) if result else -1
    
    def findMaxK_(self, nums: List[int]) -> int:
        # this is O(1) space
        # but the time complexity is O(nlogn)
        max_k = -1
        nums.sort()
        left, right = 0, len(nums) - 1
        
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == 0:
                max_k = max(max_k, abs(nums[left]))
                left += 1
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                right -= 1
        
        return max_k
