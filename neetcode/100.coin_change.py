"""
You are given an integer array coins representing coins 
of different denominations and an integer amount representing 
a total amount of money.

Return the fewest number of coins that you need to make 
up that amount. If that amount of money cannot be made 
up by any combination of the coins, return -1.

You may assume that you have an infinite number of each 
kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

Takeaway:

Bottom Up DP solution.

step by step, get to the solution, using memoization

Understanding the question is key, as always.
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # bottom up solution
        # dp[0], dp[1], dp[2], ...
        # based on your coins, calculate the 
        # amount using pre calculated dp values
        
        # we will give a default value here, which we are 
        # expecting the result to be smaller
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # calculate all dps..
        for a in range(1, amount+1):
            # with your coins
            for c in coins:
                if a - c >= 0:
                    # coin is smaller than a
                    
                    # this is the recurrence relation
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
                    # coin = 4
                    # a = 7
                    # dp[7] = 1 + dp[3]
                    
        # return the dp if the value stored is not the default value
        return dp[amount] if dp[amount] != amount + 1 else -1
    
    def coinChange_(self, coins: list[int], amount: int) -> int:
        # incredible
        # i dont even know
        coins = list(filter(lambda coin: coin <= amount, coins))
        step = 0
        seen = 1<<amount

        while seen & 1 != 1:
            cur = seen
            for coin in coins:
                cur |= seen >> coin
            
            if seen == cur:
                return -1

            step += 1
            seen = cur
    
        return step