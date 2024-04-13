"""
You are given an integer array coins representing coins of 
different denominations and an integer amount representing a 
total amount of money.

Return the number of combinations that make up that amount.

If that amount of money cannot be made up by any 
combination of the coins, return 0.

You may assume that you have an infinite number 
of each kind of coin.

The answer is guaranteed to fit into a 
signed 32-bit integer.

Example 1:

    Input: amount = 5, coins = [1,2,5]

    Output: 4

    Explanation: there are four ways to make up the amount:

        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1

Example 2:

    Input: amount = 3, coins = [2]

    Output: 0

    Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

    Input: amount = 10, coins = [10]
    
    Output: 1
 
Constraints:

    1 <= coins.length <= 300
    
    1 <= coins[i] <= 5000
    
    All the values of coins are unique.
    
    0 <= amount <= 5000

Takeaway:

    We can use a decision tree with memoization

    we gotta think of repeating solutions!

    Or

    We can use 2D DP solution, using the example
"""

class Solution:

    def change_(self, amount: int, coins: list[int]) -> int:
        # works
        # memoization
        
        # based on a decision tree
        
        
        # Input: amount = 5, coins = [1,2,5]
        
        #               0
        #          /    |     \
        #         1     2      5
        #      /  | \   | \     \ 
        #     2   3  6  4  7     10
        
        # because we do not want repeated solutions
        # we set a rule 
        
        # using the index i
        # if we are considering index i
        # we cannot use the elements smaller than i
        
        # which means, 1 can use 1 2 5
        # 2 can use 2 and 5
        # 5 can only use 5
        
        cache = {}
        
        def dfs(i, a):
            # if we found the target amount
            if a == amount:
                return 1
            # if a is bigger than amount
            if a > amount:
                return 0
            
            # if we go out of bounds
            if i == len(coins):
                return 0
            
            # we already computed it
            if (i,a) in cache:
                return cache[(i, a)]
            
            # recursive case
            # choose the coin OR Skip the coin
            
            #               choose                 skip
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            
            return cache[(i, a)]
        
        return dfs(0, 0)
    
    def change(self, amount: int, coins: list[int]) -> int:
        # works, bottom up DP
        
        #              amount
        #           5 4 3 2 1 0 
        #         ---------------
        #       1 |           1 |
        # coin  2 |           1 |
        #       5 |         0 1 |
        #         ---------------
        # 
        
        # base case is 1 because it makes math work out
        # not choosing coins to sum up to 0 , i think
        
        # if we have a 5, summing up to 1 is no bueno - so 0
        
        # if we have 2 and 5, summing 
        # if we used coin 2, we will look at two cells to the right
        # out of bounds, 0
        # if we wanna use 5 coin, we will look down below, already 0
        
        # if we have 1 and 2 and 5
        # if we choose 1 coin, we will look at the right, there is a 1
        # if we looked down, it is 0
        # 1 + 0 so it is 1
        
        # including out of bounds
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        
        # base column
        dp[0] = [1] * (len(coins) + 1)
        
        # we will start from the amount 1
        for a in range(1, amount + 1):
            # starting from the last coin index
            for i in range(len(coins) - 1, -1, -1):
                
                # just skip the coin
                dp[a][i] = dp[a][i + 1]
                # or
                if a - coins[i] >= 0:
                    # make sure we still have coins
                    # add the coin
                    dp[a][i] += dp[a - coins[i]][i]
                    
        return dp[amount][0]
