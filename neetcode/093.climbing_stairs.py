"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many 
distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:

1 <= n <= 45

Takeaway:

you do not have to compute what you already know
        
using dfs, you already solved some parts of the tree
the left side will give you what you need!
use it on the right side

              0
           /     \
         1         2
        / \       / \
       2   3     3   4
      / \ / \   / \
     3  4 4  5  4   5
    / \
   4   5

               0
           /       _\_______
         1        |    2    | 
    ____/_\       |   / \   | 
   |    2 |  3    |  3   4  |
   |   / \| / \   | / \     |
   |  3  4| 4  5  | 4   5   |
   | / \  |       |_________|
   |4   5 |
   |______|
        
you can see thar these are identical.
also for left subtree where root is 3
also for left subtree where root is 4

This is called memoization
or Caching.

solve the base case
this is bottom up solution for dp

we can make memoization with an array
we dont even need that.

0 1 2 3 4 5  - height
8 5 3 2 1 1  - steps (how many different ways you can get to top)

start from the end
stop when one gets to the starting point.

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # llm approach
        # n steps to the top
        # at each step we are choosing whethjer to take 1 or 2 steps
        """
        Identifying a dynamic programming problem often involves 
        recognizing two key properties: optimal substructure and 
        overlapping subproblems.

        Optimal Substructure:

        A problem exhibits optimal substructure if an optimal 
        solution to the problem can be constructed from optimal 
        solutions to its subproblems.
        In the context of climbing stairs, the number of distinct
        ways to reach a step is related to the number of 
        distinct ways to reach the previous steps.
        
        Overlapping Subproblems:

        Overlapping subproblems occur when a problem can be 
        broken down into smaller subproblems, and the same 
        subproblems are solved multiple times.
        For example, the number of ways to reach step i may 
        be needed in the solutions to both step i+1 and 
        step i+2, resulting in redundant computations."""
        
        if n <= 2: return n

        # Initialize an array to store the number of ways 
        # to reach each step
        dp = [0] * (n + 1)
        
        # Base cases
        dp[1] = 1
        dp[2] = 2
        
        # Build up to the solution using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # The result is the number of ways to reach the top step
        return dp[n]
    

    def climb_stairs(self, n : int):
        # you do not have to compute what you already know
        
        # using dfs, you already solved some parts of the tree
        # the left side will give you what you need!
        # use it on the right side

        #               0
        #            /     \
        #          1         2
        #         / \       / \
        #        2   3     3   4
        #       / \ / \   / \
        #      3  4 4  5  4   5
        #     / \
        #    4   5

        #                0
        #            /       _\_______
        #          1        |    2    | 
        #     ____/_\       |   / \   | 
        #    |    2 |  3    |  3   4  |
        #    |   / \| / \   | / \     |
        #    |  3  4| 4  5  | 4   5   |
        #    | / \  |       |_________|
        #    |4   5 |
        #    |______|
        
        # you can see thar these are identical.
        # also for left subtree where root is 3
        # also for left subtree where root is 4

        # This is called memoization
        # or Caching.

        # solve the base case
        # this is bottom up solution for dp

        # we can make memoization with an array
        # we dont even need that.

        # 0 1 2 3 4 5  - height
        # 8 5 3 2 1 1  - steps (how many different ways you can get to top)

        # start from the end
        # stop when one gets to the starting point.
        one, two = 1, 1

        for i in range(n -1):
            temp = one
            one = one + two
            two = temp

        return one

# Example usage
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(5))  # Output: 8
