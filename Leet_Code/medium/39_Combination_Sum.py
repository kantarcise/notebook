"""
Given an array of distinct integers candidates and a target 
integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. 

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 

Two combinations are unique if the frequency of at least 
one of the chosen numbers is different.

The test cases are generated such that the number of 
unique combinations that sum up to target is less than 
150 combinations for the given input.

Example 1:

    Input: candidates = [2,3,6,7], target = 7
    
    Output: [[2,2,3],[7]]
    
    Explanation:
    
        2 and 3 are candidates, and 2 + 2 + 3 = 7. 
            Note that 2 can be used multiple times.

        7 is a candidate, and 7 = 7.

        These are the only two combinations.

Example 2:

    Input: candidates = [2,3,5], target = 8
    
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

    Input: candidates = [2], target = 1
    
    Output: []

Constraints:

    1 <= candidates.length <= 30
    
    2 <= candidates[i] <= 40
    
    All elements of candidates are distinct.
    
    1 <= target <= 40

Takeaway:

    Decision tree, traversed with DFS.
"""

class Solution:
    def combinationSum(self, candidates: "list[int]", target: "int") -> "list[list[int]]":
        
        # to solve the decision tree
        # we approach it in a unique manner
        # at every level, when we decide that we are not adding
        # a value to a possible solution, we wont
        # be adding that value anymore

        # to track which elements we can choose
        # we will have a pointer and after each decision we 
        # will move the pointer

        res = []

        # which are the elements we are allowed to choose - i 
        def dfs(i , current_combination, total):
            # base case where we succeed
            if total == target:
                # make a copy because we will be modifying it
                res.append(current_combination.copy())
                return
            # out of bounds OR we are over target:
            if i >= len(candidates) or total > target:
                return

            # first decision
            # choose to add the candidates[i]
            current_combination.append(candidates[i])
            # move on deeper - do not change i, choose to reuse it
            dfs(i, current_combination, total + candidates[i])
            
            # second decision
            # pop the value before going to other decision
            # total will not change, because we did not add the value
            current_combination.pop()
            dfs(i + 1, current_combination, total)

        dfs(0, [], 0)
        return res
