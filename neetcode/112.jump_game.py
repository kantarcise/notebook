"""
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward 
jump from index i. In other words, if you are at nums[i], you 
can jump to any nums[i + j] where:

0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The 
test cases are generated such that you can reach nums[n - 1].


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2

Explanation: The minimum number of jumps to reach the 
last index is 2. Jump 1 step from index 0 to 1, then 
3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 
Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

Takeaway:

We can solve this question with a decision Tree and 
using a DP array. But that solution is O(n^2)

Greedy approach is better. It is O(n)

We move the goal post until the start of the array =)

"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """Think of the last element as a goal"""
        # If you can get to the the element before the 
        # last element, goalpost just moves to the left
        
        
        # 2, 3, 1, 1, 4
        # Original goal is 4
        # But we can get to 4 with 1 
        # New goal is 1
        
        goal = len(nums) - 1
        
        for i in range(len(nums) -1, -1 , -1):
            if nums[i] + i >= goal:
                # we can reach the goal!
                goal = i
                
        # that is literally it
        # we either moved the goal to the 0
        # or we failed somewhere along the lines
        return True if goal == 0 else False 
        
    def canJump_(self, nums: list[int]) -> bool:
        """First attempt, gg"""
        # [2, 3, 1, 1, 4]
        # decision tree
        # we can either go to 3 or 1
        # every step we will have different number of options.
        # we can choose the bigger element always.
        # but if we have equal ones, we will select the one that is further.
        
        # using dp lets start from end of the list
        
        n = len(nums)

        dp = [0] * n
        # the goal to reach is n-1
        steps = 0
        for i in range(n - 1 , -1, -1):
            dp[i] == max(dp[i - 1], dp[i-2] + 2)
            
        return dp[-1]
    
    def canJump___(self, nums: list[int]) -> bool:
        """Greedy, using single variable
        A bit confusing."""
        n = len(nums)

        # Instead of using a separate array 
        # for dp, we can use a single variable
        # to keep track of the maximum index that can be reached.
        max_reach = 0

        # Start iterating from the beginning
        for i in range(n):
            # If current index is greater than the 
            # maximum index that can be reached,
            # then we cannot proceed further, and 
            # it's not possible to reach the end.
            if i > max_reach:
                return False

            # Update the maximum index that can be reached at this position.
            max_reach = max(max_reach, i + nums[i])

            # If the maximum index that can be reached is greater than or equal to
            # the last index, then we can reach the end.
            if max_reach >= n - 1:
                return True

        # If we have iterated through the array 
        # and haven't reached the end,
        # then it's not possible to reach the last index.
        return False
    
    def canJump__(self, nums: list[int]) -> bool:
        """This is actually correct, but Errors with TimeLimitExceeded"""
        n = len(nums)

        # Use a dp array to store whether each index is reachable
        # You can get to this idea by using a DecisionTree
        # We select elements and we investigate whether we can get to the end?
        dp = [False] * n
        dp[0] = True  # The first index is always reachable

        # Iterate through the array
        for i in range(1, n):
            # Check if the current index is reachable by 
            # checking previous reachable indices
            # up until the value of i
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break

        # The last index is reachable if dp[n-1] is True
        return dp[n - 1]