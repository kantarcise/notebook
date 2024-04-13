"""
Given an integer array nums that may contain duplicates, return 
all possible subsets (the power set).

The solution set must not contain duplicate subsets. 

Return the solution in any order.

Example 1:

    Input: nums = [1,2,2]
    
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

    Input: nums = [0]
    
    Output: [[],[0]]

Constraints:

    1 <= nums.length <= 10
    
    -10 <= nums[i] <= 10

Takeaway:

    Use backtracking, because we can see the solution is 
    about a decision tree

    Sort the list so that you can compare consecutive elements

    for every decision, either select or do not select element 
    to be in the subset

    before going to not including part, move your pointer to
    escape duplicates

    and even before that, pop the last element you 
    added to current subset

"""

class Solution:
    def subsetsWithDup(self, nums: "list[int]") -> "list[list[int]]":
        
        # we can use backtracking

        # a decision tree
         
        #                      []
        #                 1          []
        #              [1]             []
        #            [2]  []        [2]  []
        #        [1,2]      [1]   [2]      []
        #      [2] []     [2]  [][2] []  [2] []
        # [1,2,2] 
        #          
        
        # while adding elements in our decision tree, if there are 
        # duplicate elements, skip that index and go next.
        # example - [1,2,2,3]
        # second 2 will be skipped, because it will result duplicate subsets
        # if we continue backtracking on it  

        res = []
        # to simply compare elements back to back
        nums.sort()
        
        def backtrack(i , subset):
            if i == len(nums):
                # base case, we reached the end
                # subset is complete for this iteration
                res.append(subset.copy())
                return

            # all subsets that do include nums[i]
            subset.append(nums[i])
            # this will result with a subset added to result
            backtrack(i + 1, subset)
            # so before going to the choice of not including subsets.
            # pop the last element
            subset.pop()

            # all subsets that do not include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            # if we do not include any elements, we will have []
            # so we still need to call backtracking one more time
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup(nums =  [1,2,2]))
