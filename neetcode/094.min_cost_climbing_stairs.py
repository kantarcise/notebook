"""
You are given an integer array cost where cost[i] is 
the cost of ith step on a staircase. Once you pay the 
cost, you can either climb one or two steps.

You can either start from the step with index 0, or the 
step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999

Takeaway:

the idea is from leaf to root
we can use the list that is given to us
and two variables

the calculation is a decision tree.
[10, 15, 20] 
        
          0
        /   \
      1       2 
     / \     /
    2   3   3
   /
  3 

edges are costs of moving:

           0
       10/   \10
       1       2 
    15/\15    20/
     2   3   3
  20/
   3 
        
a lot of repeated work
while we are completing the left subtree, we learn a lot about
to go from 2  to 3 and 1 to 2
SO lets use that info!

my approach
we make decisions at each step
starting from the end, a lot of recomputation
        
starting from the last two steps, go backwards
always compare 
        
"""
class Solution:

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # my approach
        # we make decisions at each step
        # starting from the end, a lot of recomputation
        # we can use dp
        # Input: cost = [1,100,1,1,1,100,1,1,100,1]
        #                                        |
        # Output: 6
        
        # starting from the last two steps, go backwards
        # always compare 
        
        n = len(cost)
        steps = [0] * n

        # Initialize steps array with the costs
        steps[n - 1] = cost[n - 1]
        steps[n - 2] = cost[n - 2]

        # Start from the third-to-last step and go backwards
        for i in range(n - 3, -1, -1):
            # Calculate the minimum cost to reach the current step
            steps[i] = cost[i] + min(steps[i + 1], steps[i + 2])

        # The result is the minimum cost to reach either the first or second step
        return min(steps[0], steps[1])


    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # the idea is from leaf to root
        # we can use the list that is given to us
        # and two variables

        # the calculation is a decision tree.
        # [10, 15, 20] 
        
        #           0
        #         /   \
        #       1       2 
        #      / \     /
        #     2   3   3
        #    /
        #   3 

        # edges are costs of moving:

        #           0
        #       10/   \10
        #       1       2 
        #    15/\15    20/
        #     2   3   3
        #  20/
        #   3 
        
        # a lot of repeated work
        # while we are completing the left subtree, we learn a lot about
        # to go from 2  to 3 and 1 to 2
        # SO lets use that info!

        # add a zero - the top floor
        # [10, 15, 20] 0
        cost.append(0)


        # from 15 , we can take a 1 jump
        # or a double jump
        for i in range(len(cost) - 3, -1 , -1):
            cost[i] = min(cost[i]+cost[i+1], cost[i]+ cost[i+2])

        # cost array at least have 2 items
        return min(cost[0], cost[1])