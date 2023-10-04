"""

TODO:

You are given an array prices where prices[i] is the price of a
 given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one
 stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
 cannot achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed
 because you must buy before you sell.


Example 2:

Input: prices = [7,6,4,3,1]
Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

Takeaway:

We are using a sliding window, with to pointers.

Only moving right pointer is enough to traverse through

check profit for each transaction, and update max

if we find a new low, update left pointer.

"""

class Solution:
    
    # first approach, did a mistake, idk why?
    def maxProfit(self, prices) -> int:
        # We should look for every opportunity where
        # we buy stocks first
        # and sell them on another day
        # the profit is the difference between the prices.
        
        max_profit = 0
        l, r = 0 , 1

        while l < r and r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
            if r == len(prices):
                r = l
                l += 1

        return max_profit

    def maximize_profit(self, prices):
        
        max_profit = 0
        l, r = 0 , 1

        while r < len(prices):
            
            # is this profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max (max_profit, profit)

            # not profitable, but a new low is achieved in R 
            # so set l there
            else: 
                l = r
            # move r
            r += 1

        return max_profit

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit(prices = [7,1,5,3,6,4])) 
    print(sol.maxProfit(prices = [7,6,4,3,1]))

    print("should be true")
    print(sol.maximize_profit(prices = [7,1,5,3,6,4])) 
    print(sol.maximize_profit(prices = [7,6,4,3,1]))