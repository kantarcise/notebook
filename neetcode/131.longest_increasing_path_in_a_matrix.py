"""
Given an m x n integers matrix, return the length 
of the longest increasing path in matrix.

From each cell, you can either move in four directions: 
left, right, up, or down. 

You may not move diagonally or move outside 
the boundary (i.e., wrap-around is not allowed).

Example 1:

    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    
    Output: 4

    Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    
    Output: 4

    Explanation: 
    
        The longest increasing path is [3, 4, 5, 6]. 
        Moving diagonally is not allowed.

Example 3:

    Input: matrix = [[1]]
    
    Output: 1
 
Constraints:

    m == matrix.length
    
    n == matrix[i].length
    
    1 <= m, n <= 200
    
    0 <= matrix[i][j] <= 2^31 - 1

Takeaway:

    Memoization. Brute Force DFS.

    Understand what if dfs returning, or why is it there?

    Call dfs from all cells - check all directions
"""

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        
        # we cannot reuse values, because we are 
        # on an increasing path
        
        # brute force
        # try every single position, 
        # lip matrix for original matrix.
        
        
        # original
        # 9 9 4
        # 6 6 8 
        # 2 1 1
        
        
        # LIP
        #  -----------
        # | 1 | 1 | 2 |
        # | 2 | 2 | 1 |
        # | 3 | 4 | 2 |
        #  -----------
        
        # from first 9 we cannot go anywhere
        
        # from second 9 we cannot go anywhere        
        
        # from 4 we can go left, we already run dfs on 9
        # from 4 we can go down, we will run dfs on 8
        # from 8 we cannot go anywhere.
        
        # from 6 we can only go up
        
        # from middle 6 we can go up or right
        # result is 2 
        
        # from left 8, we already computed when we ran 4
        
        # from 2, we can go up
        
        # from bottom middle 1, we can go left and add cached
        
        # if we have a perfect path, 
        # we will run dfs once for o(n*m)
        # than we are good for all other cells
        
        # if all cells are equal, 
        # all dfs() will be o(1) 
        # called for o(n*m) times
        
        # so the time complexity is o(N*m)
        
        rows, cols = len(matrix), len(matrix[0])
        
        dp = {} # (r, c) for LIP
        
        # find the longest path in a given cell r, c
        def dfs(r, c, prev_val):
            # out of bounds and not increasing
            # base cases
            if (r < 0 or r == rows or
               c < 0 or c == cols or
                matrix[r][c] <= prev_val):
                return 0
            
            # already computed base case
            if (r, c) in dp:
                return dp[(r, c)]
            
            # at least 1 in path
            res = 1
            
            # go all 4 directions
            
            # compare between 
            # current value of res
            # and
            # 1 + the next cell we are looking for
            res = max(res, 1 + dfs(r + 1, c , matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c , matrix[r][c]))            
            res = max(res, 1 + dfs(r, c + 1 , matrix[r][c]))            
            res = max(res, 1 + dfs(r, c - 1 , matrix[r][c])) 
            
            # return the result in cache
            dp[(r, c)] = res
            
            return res
        
        for r in range(rows):
            for c in range(cols):
                # because -1 will always be smaller
                dfs(r, c, -1)
                
        return max(dp.values())
