"""
Given an array of distinct integers candidates and a target integer 
target, return a list of all unique combinations of candidates where the 
chosen numbers sum to target. 

You may return the combinations in any order.

The same number may be chosen from candidates an unlimited 
number of times. 

Two combinations are unique if the frequency of at least one of 
the chosen numbers is different.

The test cases are generated such that the number of unique 
combinations that sum up to target is less than 150 
combinations for the given input.

Example 1:

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

    Explaination:
        
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

    The simple approach would be make a hudge decision tree.

    The problem with that approach is that we will not be able 
    to identify duplicates

    to solve the decision tree
    we approach it in a unique manner
    at every level, when we decide that we are not adding
    a value to a possible solution, we wont
    be adding that value anymore

    to track which elements we can choose
    we will have a pointer and after each decision we 
    will move the pointer

    In backtracking, we have a decision to be made in the 
    end of dfs function 

"""

class Solution:

    def combinationSum_(self, candidates: "list[int]", target: "int") -> "list[list[int]]":
        # does not work
        
        # we can use a decision tree
        # with 4 decision each time.
        # the problem is, we will have duplicates with that
        # like [2, 2, 3] and [2, 3, 2] 

        # how about a simple hashmap
        # did not work
        result = []

        solution_dict = {elem: [] for elem in candidates}

        for key in solution_dict:
            while  key < target:
                solution_dict[key].append(key)
                if sum(solution_dict[key]) == target:
                    result.append(solution_dict[key])

        return result

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

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum())
