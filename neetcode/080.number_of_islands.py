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

from collections import deque

class Solution:
    def numIslands(self, grid: "list[list[str]]") -> int:
        # it is just bfs man. We got this.
        if not grid:
            return 0
        
        rows , cols = len(grid), len(grid[0])

        visited = set()
        islands = 0

        def bfs(r ,c):
            q = deque()
            visited.add((r,c))
            # add the coordinates to the queue
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for deltar, deltac in directions:
                    r , c = row + deltar , col + deltac

                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        # add the coordinate to queue
                        q.append((r, c)) 
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # we found a new Island!
                    # lets see how big it is?
                    bfs(r,c)
                    islands += 1

        return islands
    
    def numIslands_(self, grid: list[list[str]]) -> int:
        # dfs solution

        row = len(grid)
        column = len(grid[0])
        result = 0

        def dfs(i, j):

            # return if not proper island
            if (i < 0 or 
                j < 0 or 
                i >= row or 
                j >= column or 
                grid[i][j] == '0'):
                    return

            #  Otherwise, it marks the current cell 
            # as visited by setting it to '0' and recursively 
            # calls dfs on its neighbors 
            # (up, down, left, and right).
            grid[i][j] = '0'

            # 4 direction dfs. cool
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i, j)
        
        return result
