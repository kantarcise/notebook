"""
You are given an array prices where prices[i] is the 
price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many 
transactions as you like (i.e., buy one and sell one share of 
the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the 
next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions 
simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3

Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0
 
Constraints:

    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000

Takeaway:

2D DP, simply a decision tree.

Which is derived with basic thinking, as always.

Caching is key!

"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # we want to maximize the index i and index i + 1
        # to make a profit
        
        # prices = [1,2,3,0,2]
        
        # we can use a decision tree
        
        #                     0
        #                buy     cd
        #              -1           0
        #      (+2)sell   cd       buy  cd  
        #          +1       -1     -2     0
        #          cd 
        #    (we have to cd)
        #          +1
        #     (0)buy  cd 
        #      +1        +1
        #   sell cd  
        #  +3      +1
        
        # height of the tree is n
        # number of decisions at each point is 2^N
        # o(2^n)
        
        # we can use a cache!
        
        # (index, buy/seel (bool))
        # which will result in o(2n) == o(n)
        
        # State: Buying or Selling?
        # If Buy: increment the index by 1 - i + 1
        # If Sell: increment the index by 2 - i + 2

        dp = {}  # key=(i, buying) val=max_profit

        # if we are a buy state, buying = True
        # if we are a sell state, buying = False
        
        def dfs(i, buying):
            # a recursive function, let's write the base case
            
            # out of bounds
            if i >= len(prices):
                return 0
            
            # if already calculated
            if (i, buying) in dp:
                # max profit already has been stored
                return dp[(i, buying)]

            # are we buying
            if buying:
                # max profit in buy state
                # we have to subtract the price of day i
                buy = dfs(i + 1, not buying) - prices[i]
                
                # always a choice to cooldown
                cooldown = dfs(i + 1, buying)
                
                # cache the result
                # which one resulted in max profit ?
                dp[(i, buying)] = max(buy, cooldown)
            # are we not buying
            else:
                # we sell, we have to increment buy 2
                # we need to increment the profit, we sold!
                sell = dfs(i + 2, not buying) + prices[i]
                
                # always a choice to cooldown
                cooldown = dfs(i + 1, buying)
                
                # cache the result
                # which one resulted in max profit ?
                dp[(i, buying)] = max(sell, cooldown)
            
            # we want to return the max profit
            return dp[(i, buying)]

        # starting from 0 and we start with buying
        return dfs(0, True)