"""
You are a professional robber planning to rob houses along 
a street. Each house has a certain amount of money 
stashed, the only constraint stopping you from robbing 
each of them is that adjacent houses have security systems 
connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount 
of money of each house, return the maximum amount 
of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4

Explanation: 

  Rob house 1 (money = 1) and then rob house 3 (money = 3).
  Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12

Explanation: 

  Rob house 1 (money = 2), rob house 
    3 (money = 9) and rob house 5 (money = 1).

  Total amount you can rob = 2 + 9 + 1 = 12.
 
Constraints:

  1 <= nums.length <= 100
  0 <= nums[i] <= 400

Takeaway:

DP problem

Normally we get to memoization table
solution (with recursion)

After that we optimize for bottom up 

Tabulation = Bottom Up Approach

Starting with the smallest subproblems and 
solving them iteratively until the main 
problem is solved.


"""

class Solution:
    def rob__(self, nums: List[int]) -> int:
        # does NOT Work
        # we either rob odd houses 
        # or even ones.
        
        # that is not True, because we might
        # rob first and last houses in
        # [2,1,1,2]
        
        # obviously wrong
        return max(sum([elem for elem in nums[0::2]]), 
                   sum([elem for elem in nums[1::2]]))

    def rob_(self, nums: List[int]) -> int:
        
        # with a memoization table
        # only single house
        if len(nums) == 1:
            return nums[0]
        # 2 houses
        if len(nums) == 2:
            return max(nums)
        # make a list for dp
        dp = [0] * len(nums)
        # start is the first house
        dp[0] = nums[0]
        # second elem is the bigger of two
        dp[1] = max(nums[0], nums[1])

        # fill the dp table
        for i in range (2, len(nums)):
            # basically, DP before VS element and DP 2 index before 
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        # return the last element
        return dp[-1]
      
    def rob(self, nums: List[int]) -> int:
        # at each house we decide whether or not we 
        # rob the house or not
        # iteration solution
        
        # tabulation
        
        # Bottom-Up Approach: DP iteration follows a bottom-up 
        # approach, starting with the smallest subproblems and 
        # solving them iteratively until the 
        # main problem is solved.
        
        # think about the solution like
        # [rob1, rob2, n, n+1, n+2, ..]
        rob1, rob2 = 0, 0
        for n in nums:
            
            # if we are including n, we cannot start with rob2
            # we gotta start with rob1
            # select the highest among
            temp = max(rob1 + n, rob2)                  
            
            # move the window
            rob1 = rob2
            
            # rob2 would become the n
            # but we calculated n as the new max using "temp"
            rob2 = temp
            
        # when we get to the end in the loop,
        # rob2 will be the highest value,
        # meaning it would be our answer
        return rob2
