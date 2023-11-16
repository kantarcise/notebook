"""
Given an integer n, return an array ans of length n + 1 such 
that for each i (0 <= i <= n), ans[i] is the number of 1's in 
the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 
Constraints:

0 <= n <= 105
 
Follow up:

It is very easy to come up with a solution with a runtime of 
O(n log n). Can you do it in linear time O(n) and 
possibly in a single pass?

Takeaway:

YOu can use the built in bin function ans str count

The problem literally begs for DP

So, dont forget, dp is memoization. 

Find the pattern and move.
"""

class Solution:

    def countBits(self, n: int) -> list[int]:
        """
        Use the built in bin function ans str count
        
        Args:
            n(int): the number for constructing the list

        Returns:
            result(list[int]): all the numbers with count of 1s
        
        """
        result = []
        for index in range(n+1):
            result.append((bin(index)).count("1"))
        return result
    

    def countBits(self, n: int) -> list[int]:
        # I KNEW IT
        # THIS IS A SNEAKY Dynamic Programming PRoblem
        
        # what is the most significant bit we have reached so far?

        # 0 -  0000  - 0
        # 1 -  0001  - 1 + dp[n-1]
        # 2 -  0010  - 1 + dp[n-2]
        # 3 -  0011  - 1 + dp[n-2]
        # 4 -  0100  - 1 + dp[n-4]
        # 5 -  0101  - 1 + dp[n-4]
        # 6 -  0110  - 2
        # 7 -  0111  - 3
        # 8 -  1000  - 1 + dp[n-8]

        dp = [0] * (n + 1)
        offset = 1 # will be just 1, 2, 4, 8, 16

        for i in range(1, n + 1):
            # offset possibly changes with every movement
            if offset * 2 == i:
                offset = i
            # the calculation
            dp[i] = 1 + dp [i - offset]

        return dp
    
    def countBits_llm(self, n: int) -> list[int]:
        # Initialize an array 'ans' to store the count of set bits for each number
        ans = [0] * (n + 1)

        # Iterate from 1 to n (inclusive)
        for i in range(1, n + 1):
            # The count of set bits for a number 'i' is the same as the count
            # of set bits for 'i >> 1' (right shift by 1) plus the least
            # significant bit of 'i' (i & 1).
            ans[i] = ans[i >> 1] + (i & 1)

        # Return the final array containing the count of set bits for each number
        return ans