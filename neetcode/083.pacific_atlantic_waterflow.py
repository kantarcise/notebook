"""
There is an m x n rectangular island that borders both 
the Pacific Ocean and Atlantic Ocean. 

The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean 
touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 

You are given an m x n integer matrix heights where heights[r][c] 
represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water 
can flow to neighboring cells directly north, south, east, 
and west if the neighboring cell's height is less than or equal 
to the current cell's height. 

Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where 
result[i] = [ri, ci] denotes that rain water can flow from 
cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:

    Input: heights = [[1,2,2,3,5],
                      [3,2,3,4,4],
                      [2,4,5,3,1],
                      [6,7,1,4,5],
                      [5,1,1,2,4]]

    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    Explanation: 
    
        The following cells can flow to the Pacific and Atlantic 
            oceans, as shown below:

        [0,4]: [0,4] -> Pacific Ocean 
               [0,4] -> Atlantic Ocean
        [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
               [1,3] -> [1,4] -> Atlantic Ocean
        [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
               [1,4] -> Atlantic Ocean
        [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
               [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
        [3,0]: [3,0] -> Pacific Ocean 
               [3,0] -> [4,0] -> Atlantic Ocean
        [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
               [3,1] -> [4,1] -> Atlantic Ocean
        [4,0]: [4,0] -> Pacific Ocean 
               [4,0] -> Atlantic Ocean

        Note that there are other possible paths for these cells 
        to flow to the Pacific and Atlantic oceans.

Example 2:

    Input: heights = [[1]]

    Output: [[0,0]]

    Explanation: 
    
        The water can flow from the only cell to the 
            Pacific and Atlantic oceans.

Constraints:

    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 10^5
    
Takeaway:

    Oh what a surprise, we will use DFS!

    Compartmentalize the code.
"""

class Solution:
    def pacificAtlantic_(self, heights: list[list[int]]) -> list[list[int]]:
        # could not make this work
        # pacific left - top
        # atlantic - bottom - right
        # return cells where there can be bidirectional flow
        
        rows = cols = len(heights)
        
        # for every cell, check every neighbour
        # return True if dual flow
        
        def dfs(i, j):
            # this method has to return the [i][j] 
            # if conditions hold
            # otherwise returns None
            if (i < 0 or
               j < 0 or
               i >= rows or
               j >= cols):
                return
            return
        
        result = []
        for i in range(rows):
            for j in range(cols):
                result.append(dfs(i, j))
        
        return result
    
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # instead of checking every cell in the grid, which would result in O(m*m)**2
        # seperately, check the reach for pacific, and atlantic
        # for intersection of those sets, we will find the result
        
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visit, previous_height):
            # already visited
            # out of bounds
            # or height is smaller than previous height
            if ((r, c) in visit or 
               r < 0 or c < 0 or r == rows or c == cols or 
               heights[r][c] < previous_height):
                return 
            
            # add the tile into set
            visit.add((r,c))
            
            # call dfs on neighbours
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            
        # go for every single position in the first row
        for c in range(cols):
            # first row, we are checking for pacific
            dfs(0, c, pacific, heights[0][c])
            # bottom row, we are cheking for atlantic
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
            
        # first column and last column
        for r in range(rows):
            # first col, we are checking for pacific
            dfs(r, 0, pacific, heights[r][0])
            # last col, we are checking for atlantic
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
                    
        return result

    def pacificAtlantic__(self, heights: list[list[int]]) -> list[list[int]]:
        # another approach
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        
        # Define directions for moving to neighboring cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Helper function to perform DFS
        def dfs(i, j, visited):
            visited[i][j] = True
            
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                
                # Check if the neighbor is within bounds and the height is greater than or equal
                # Also, check if the neighbor cell has not been visited
                if 0 <= ni < rows and 0 <= nj < cols and heights[ni][nj] >= heights[i][j] and not visited[ni][nj]:
                    dfs(ni, nj, visited)

        # Create matrices to track cells that can reach Pacific and Atlantic Oceans
        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]

        # Check cells in the first and last columns (Atlantic and Pacific Oceans)
        for i in range(rows):
            dfs(i, 0, pacific_reachable)  # Pacific Ocean
            dfs(i, cols - 1, atlantic_reachable)  # Atlantic Ocean

        # Check cells in the first and last rows (Pacific and Atlantic Oceans)
        for j in range(cols):
            dfs(0, j, pacific_reachable)  # Pacific Ocean
            dfs(rows - 1, j, atlantic_reachable)  # Atlantic Ocean

        # Find cells that can reach both Pacific and Atlantic Oceans
        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])

        return result
