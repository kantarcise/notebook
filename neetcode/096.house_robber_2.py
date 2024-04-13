"""
You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed. All houses at 
this place are arranged in a circle. 

That means the first house is the neighbor of the last one. 

Meanwhile, adjacent houses have a security system connected, and it 
will automatically contact the police if two adjacent houses 
were broken into on the same night.

Given an integer array nums representing the amount of money of 
each house, return the maximum amount of money you can rob 
tonight without alerting the police.

Example 1:

    Input: nums = [2,3,2]
    
    Output: 3
    
    Explanation: 
    
        You cannot rob house 1 (money = 2) and then 
        rob house 3 (money = 2), because they are adjacent houses.

Example 2:

    Input: nums = [1,2,3,1]
    
    Output: 4
    
    Explanation: 
        
        Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.

Example 3:

    Input: nums = [1,2,3]
    Output: 3

Constraints:

    1 <= nums.length <= 100
    
    0 <= nums[i] <= 1000

Takeaway:

    We either rob the first house or dont.

    basicaly the 3sum and 2sum relationship.

    Instead of whole rewrites, we write a helper function.
"""

class Solution:
    def rob_(self, nums: list[int]) -> int:
        # kinda like a circular linked list
        # basically an edge case where we cannot rob 
        # both initial and ending houses        
        # 0, 1, 2, 3, 4
        # either rob 0 or dont
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        # either rob the first house or dont:
        nums1, nums2 = nums[:-1], nums[1:] 
        dp1, dp2 = ([0] * len(nums1)), ([0] * len(nums2))
        
        # for nums1
        dp1[0] = nums1[0]
        dp1[1] = max(nums1)
        
        for i in range(2, len(nums1)):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums1[i])
            
        # for dp2
        dp2[0] = nums2[0]
        dp2[1] = max(nums2)
        
        for i in range(2, len(nums2)):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums2[i])
            
        return max(dp1[-1], dp2[-1])
    
    def rob(self, nums: list[int]) -> int:
        # clean up the code
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        # write a helper function
        # instead of writing it 2 times
        def rob_linear(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            return dp[-1]
        
        # Either rob the first house or don't
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
