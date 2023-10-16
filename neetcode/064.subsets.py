"""
Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate 
subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique

Takeaway:

What is backtracking?

The backtracking algorithm enumerates a set of partial candidates 
that, in principle, could be completed in various ways to give all
the possible solutions to the given problem. The completion is done
incrementally, by a sequence of candidate extension steps.

Conceptually, the partial candidates are represented as the nodes 
of a tree structure, the potential search tree. Each partial 
candidate is the parent of the candidates that differ from it 
by a single extension step; the leaves of the tree are the partial 
candidates that cannot be extended any further.

The backtracking algorithm traverses this search tree recursively, from 
the root down, in depth-first order. At each node c, the algorithm checks 
whether c can be completed to a valid solution. If it cannot, 
the whole sub-tree rooted at c is skipped (pruned). Otherwise, the
algorithm (1) checks whether c itself is a valid solution, and if 
so reports it to the user; and (2) recursively enumerates all sub-trees 
of c. The two tests and the children of each node are defined 
by user-given procedures.

Therefore, the actual search tree that is traversed by the 
algorithm is only a part of the potential tree. The total cost 
of the algorithm is the number of nodes of the actual tree 
times the cost of obtaining and processing each node. This fact 
should be considered when choosing the potential search tree 
and implementing the pruning test.

When applying backtracking to a problem, you can make a decision 
tree to represent the sequence of choices made and the paths 
explored to reach a solution.

Backtracking Process: As backtracking proceeds, it explores different 
branches, and when it reaches a dead-end (a choice that doesn't 
lead to a solution), it backtracks to a previous decision point 
and explores a different branch. This process is similar 
to traversing decision trees.

We can make a decision tree to represent the question

We have the choice of adding or not adding
every element for the subset

For every level of the dfs, we will decide on the condition
we are moving on and will call dfs again on one level deeper.

Stop when we reach the leafs for the decision tree

"""

class Solution:
    
    def subsets_recursive(self, seq: 'list'):
        # this solution was from recursion chapter
        # just Gorgeous but a bit complicated
        # base case
        if len(seq) == 0:
            return [[]]
        else:
            # get all subsets without the first element
            subsets_without_first = self.subsets_recursive(seq[1:])
            # get all subsets with the first element
            subsets_with_first = [[seq[0]] + subset 
                        for subset in subsets_without_first]
            # return all subsets
            return subsets_with_first + subsets_without_first
    
    def subsets(self, nums):
        # neetcode

        # we have the choice of adding or not adding
        # every element for the subset

        # here is a decision tree for our question

        #                   .
        #               1         []    
        #             [1]           []
        #           2     []      2    []
        #        [1,2]     [1]   [2]      []  
        #       3   []    3  []  3  []   3   [] 
        #  [1,2,3][1,2][1,3] [1][2,3][2] [3]  []
        # 

        #  8 elements in the end    
        # this is backtracking

        result = []
        subset = []

        # 1, 2, 3  --- i is the index of the current element
        # our dfs function will have access to nums by default
        # also res and subset will be accessed by dfs
        def dfs(i):
            # no more levels to call dfs on.
            if i >= len(nums):
                # if we are out of bounds with the index
                # we are past of the leaf node
                # using subset.cpoy()
                # because the value of subset will be changing 
                # as we move on with dfs
                result.append(subset.copy())
                return
            
            # two decisions

            # decision to include nums[i]
            subset.append(nums[i])
            # call dfs on the next level
            dfs(i + 1)

            # decision to not include nums[i]
            # pop the element just appended
            subset.pop()
            # call the dfs on the next level
            dfs(i + 1)
        
        # start from the root of the decision tree
        dfs(0)
        return result

if __name__ == "__main__":
    sol = Solution()

    print(sol.subsets([1,2,3]))