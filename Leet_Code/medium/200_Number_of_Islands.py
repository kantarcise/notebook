"""
Given an m x n 2D binary grid grid which represents a map 
of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. 

You may assume all four edges of the grid are all 
surrounded by water.

Example 1:

    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    
    Output: 1

Example 2:

    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3
    

Constraints:

    m == grid.length
    
    n == grid[i].length
    
    1 <= m, n <= 300
    
    grid[i][j] is '0' or '1'.

Takeaway:

    To solve this question, think like a kindergardener.

    How can you find a single island?

    You look.

    For each 1, you need to check neighbours, this is clearly bfs or dfs.

    Setting the cell to 0 in order to not visit it again is pretty cool.
"""

class Solution:
    
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0

        def dfs(i, j):
            if (i < 0 or 
                j < 0 or 
                i >= m or 
                j >= n or 
                grid[i][j] == '0'):
                    return
			# make the current tile 0
			# so you will not count this tile again
            grid[i][j] = '0'

			# go to every direction possible
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i, j)
        
        return result
