"""
You are given an m x n binary matrix grid. An island is a 
group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the 
grid are surrounded by water.

The area of an island is the number of cells with a value 1 
in the island.

Return the maximum area of an island in grid. If there is no 
island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6

Explanation: The answer is not 11, because the island must 
be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.


Takeaway:

DFS is wonderful. 

There is a condition on calling dfs

AND

We do not have to call dfs on every tile.

"""

class Solution:
    def maxAreaOfIsland_(self, grid: list[list[int]]) -> int:
        # out of bounds is water
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs_area(i, j):
            if (i < 0 or
                j < 0 or
                i >= rows or
                j >= cols or 
                grid[i][j] == 0):
                return 0
            
            grid[i][j] = 0

            area = 1 
            area += dfs_area(i + 1, j)
            area += dfs_area(i, j + 1)
            area += dfs_area(i -1, j)
            area += dfs_area(i, j - 1)
            
            return area
            
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs_area(i, j))
        
        return max_area
    
    
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # neet
        # uses a visited set for the dfs
        # this way, we will not run dfs on the same island twice or more
        
        # if we bump into a 1 value, we will run dfs
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            # base case first
            if (r < 0 or r == rows or c < 0 or c == cols or 
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            visit.add((r,c))
            
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        
        return area
