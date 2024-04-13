"""
Given a collection of candidate numbers (candidates) and a target 
number (target), find all unique combinations in candidates where 
the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

    Input: candidates = [10,1,2,7,6,1,5], target = 8
    
    Output:

        [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
        ]

Example 2:

    Input: candidates = [2,5,2,1,2], target = 5
    
    Output:

        [
        [1,2,2],
        [5]
        ]

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

Takeaway:

    for every element, we can include it or not include it
    time complexity will be 2^n

    if we just brute force it
    there will be duplicate solutions

    to get rid of duplicate solutions
    subtract the element from the target and 
    make sure the left subtree is including the unique
    element and right subtree is not

    this was we will make sure that the results will be unique
    [10, 1, 2, 7, 6, 1]
    sort it
    [1, 1, 2, 6, 7, 10]

    for each subtree either add or not add the element 
    move the pointer accordingly

"""

class Solution:
    
    def combinationSum2__(self, candidates: "list[int]", target: int) -> "list[list[int]]":
        # my first try
        # DOES NOT work

        # we can use a decision tree
        
        # basically for every level on our tree, we are trying 
        # to find candidates that sum up too target
        
        # we can remove all elements higher than target to 
        # eliminate unneccessary computation
        
        # [1,2,2,2,5] - 5
        
        #                           []
        #                  1                   []
        #         1,2            1        2             []
        #     1,2,2   1,2     1,5  1    2,2  2      5       []
        #   
        
        res = []
        subset = []
        
        def backtrack(i , subset):
            if sum(subset) == target:
                res.append(subset.copy())
            elif sum(subset) > target:
                return
            else:
                subset.append(candidates[i])
                backtrack(i+1, subset)
                subset.pop()
                
                while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1
                
                backtrack(i+1, subset)
                
        backtrack(0, [])
        return res

    def combinationSum2(self, candidates: "list[int]", target: int) -> "list[list[int]]":
        # for every element, we can include it or not include it
        # time complexity will be 2^n
        
        # if we just brute force it
        # there will be duplicate solutions

        # to get rid of duplicate solutions
        # subtract the element from the target and 
        # make sure the left subtree is including the unique
        # element and right subtree is not

        # this was we will make sure that the results will be unique

        # [10, 1, 2, 7, 6, 1]

        # sort it
        # [1, 1, 2, 6, 7, 10]
        # 
        # for each subtree either add or not add the element 
        # move the pointer accordingly

        candidates.sort()
        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                # we found a solution
                res.append(cur.copy())
            if target <= 0:
                # we went over
                return

            prev = float("-inf")
            for i in range(pos, len(candidates)):
                # if we already have a solution using an element
                if candidates[i] == prev:
                    # skip this iteration of the loop
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()

                prev = candidates[i]
        
        backtrack([], 0 ,target)

        return res


    def combinationSum2_(self, candidates: "list[int]", target: int) -> "list[list[int]]":
        # this works, and it is faster
        
        def backtrack(start, path, target):
            if target == 0:
                # found the solution
                res.append(path)
                return
            
            for i in range(start, len(candidates)):
            
                if i > start and candidates[i] == candidates[i - 1]:
                    # skip this iteration of the loop
                    # same elements
                    continue
                if candidates[i] > target:
                    # we are over target
                    break
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])

        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res
