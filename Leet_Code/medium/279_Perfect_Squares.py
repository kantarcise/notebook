"""
Given an integer n, return the least number of perfect 
square numbers that sum to n.

A perfect square is an integer that is the square of an 
integer; in other words, it is the product of some integer 
with itself. 

For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.

Example 2:

    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9.

Constraints:

    1 <= n <= 10^4

Takeaway:

    You KNOW this is a DP problem.

"""
class Solution:    
    def numSquares_(self, n: int) -> int:
        # this works
        
        # dp problem for SURE
        
        dp = [10e4] * (n + 1)
        
        # because 0 would be 0
        dp[0] = 0
        
        # Iterate through numbers from 1 to n
        for i in range(1, n + 1):
            # Try all possible perfect square numbers 
            # less than or equal to i
            j = 1
            while j * j <= i:
                # Update dp[i] if using j*j can achieve 
                # a smaller number of perfect squares
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        
        # dp[n] now stores the least number of 
        # perfect square numbers that sum up to n
        return dp[n]
        
        
    def numSquares(self, n: int) -> int:
        # this works, and it's faster
        
        # all the perfect squares we can use within n
        perfect = []

        i = 1
        while i * i <= n:
            perfect.append(i*i)
            i += 1
        
        # print(perfect)
        dp = [10e4] * (n+1)

        # because 0 would be 0
        dp[0] = 0

        for i in range(1, n+1):
            for j in perfect:
            # for all possible perfects
                if j > i:
                    # cannot use this coin
                    # stop calculating
                    # for that number
                    break
                else:
                    # we want the min between
                    # either current or using jth coin
                    # plus 1 
                    dp[i] = min(dp[i], 1 + dp[i-j])

        # print(perfect, dp)
        # print(dp)
        return dp[n]
