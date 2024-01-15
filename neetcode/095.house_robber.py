"""
You are a professional robber planning to rob houses 
along a street. Each house has a certain amount of 
money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have 
security systems connected and it will automatically 
contact the police if two adjacent houses were broken 
into on the same night.

Given an integer array nums representing the amount of 
money of each house, return the maximum amount of 
money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 
Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

Takeaway:

We can start to think with a decision tree.

For a long nums list, this would be really complex

Recurrence Relationship in DP

A way to break up dynamic programming problems

rob = max( arr[0] + rob[2:n] , rob[1:n])

"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        # we either rob the first house and the max 
        # of remaining houses 
        # or starting from 2nd one, max of all.
        rob1, rob2 = 0, 0 

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # maximum we can rob up until the value n
            temp = max(rob1 + n, rob2)

            # prepare for next step

            # rob1 becomes rob2
            rob1 = rob2
            
            # rob2 becomes the temp
            rob2 = temp
        return rob2
