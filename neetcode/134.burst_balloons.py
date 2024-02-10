"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is 
painted with a number on it represented by an array nums. You are asked 
to burst all the balloons.

If you burst the ith balloon, you will get 
nums[i - 1] * nums[i] * nums[i + 1] coins. 

If i - 1 or i + 1 goes out of bounds of the array, then 
treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by 
bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167

Explanation:

    nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

    n == nums.length
    1 <= n <= 300
    0 <= nums[i] <= 100

Takeaway:

Still just using dfs - cached.

Instead of thinking which balloon to pop first, think which 
one to pop last.

Use the example to derive the relation of recursion

"""
class Solution:
    
    def maxCoins(self, nums: list[int]) -> int:
        # neet

        # a legit hard question
        # couple of tricks 

        # we can use a decision tree  and backtracking

        # Input: nums = [3,1,5,8] 
        #           _
        #       3 1  5  8
        #     1 5 8 

        # time complexity would be o(n^n)
        # oh no

        # when we pop an baloon,
        # we get a subproblem

        # [3, 1, 5, 8] -> [3, 1, 8]

        # as we pop elements we get every single subsequence
        # how many subsequences are there?
        # for each element we can either include it or not include it
        # this is still o(2^n)

        # instead of thinking popping baloons

        # think like what if we pop a baloon LAST.

        # [3, 1, 5, 8]

        # when a 5 is going to be popped last:

        # [1], [[3, 1] , 5]

        # we are not going to delete 5 or the implicit 1 at the left
        # this allows us to get a subproblem we can cache

        # so we will have a 2D cache:
        # dp[L][R] - left and right boundaries of arrays

        # Our decision tree is changed to:
        # what if we popped a value LAST

        #   0   1  2  3  4    5
        #   1, [3, 1, 5, 8] , 1
        #       L        R

        # If we popped 3 last
        # The point calculation + left_subarray + right_subarray
        # there is no left subvarray when we pop 3
        # nums[L-1] * 3 * nums[R+1] + DP[L+1][R]

        # if we popped a middle value
        # if we popped 1 last:
        # The point calculation + left_subarray + right_subarray
        # nums[L-1] * 1 * nums[R+1] + DP[i+1][R] + DP[L][i-1]

        # if we popped a end value
        # if we popped 8 last
        # The point calculation + left_subarray + right_subarray
        # nums[L-1] * 8 * nums[R+1]

        # update the input array
        nums = [1] + nums + [1]

        dp = {}

        # l and r are indices of input array
        def dfs(l ,r):
            # l == r is okay, we have one baloon left to pop
            if l > r :
                # we ran out of baloons
                return 0
            
            # already computed
            if (l, r) in dp:
                return dp[(l, r)]
            
            # initially zero
            dp[(l, r)] = 0

            # go through every index
            for i in range(l, r + 1):
                # just the point
                coins = nums[l -1] * nums[i] * nums[r + 1]
                # left and right subarray addtitions
                coins += dfs(l, i -1) + dfs(i + 1, r)
                
                # update with the current value and calculated coins
                # we are looking for the max 
                dp[(l, r)] = max(dp[(l, r)], coins)
            
            # return the value
            return dp[(l, r)]

        # we do not want to include the added 1's
        return dfs(1, len(nums) - 2)
    
    
    def maxCoins_(self, nums: list[int]) -> int:
        # from a homie
        # bottom up solution
        
        # according to the recursive solution, 
        # we need to get dp[1][len(nums) - 2], it is 
        # in the right-top corner. in the coordinate system
        # l is less and less, r is bigger and bigger
        nums = [1] + nums + [1]
        
        dp = [[0] * len(nums) for _ in range(len(nums))]
        
        for l in range(len(nums) - 2, 0, -1):
            for r in range(l, len(nums) - 1):
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    # dp[l][r] = max(dp[l][r], coins)
                    if dp[l][r] < coins:
                        dp[l][r] = coins
        return dp[1][len(nums) - 2]