"""
You are given row x col grid representing a map where 
grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 

The grid is completely surrounded by water, and there is exactly 
one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected 
to the water around the island. 

One cell is a square with side length 1. The grid is 
rectangular, width and height don't exceed 100. 

Determine the perimeter of the island.

Example 1:

    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    
    Output: 16
    
    Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

    Input: grid = [[1]]
    
    Output: 4

Example 3:

    Input: grid = [[1,0]]
    
    Output: 4
 
Constraints:

    row == grid.length
    
    col == grid[i].length
    
    1 <= row, col <= 100
    
    grid[i][j] is 0 or 1.
    
    There is exactly one island in grid.

Takeaway:

    dfs with a simple data structre alongside.

"""

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        # we can use dfs
        
        rows, cols = len(grid), len(grid[0])
        total = 0

        def dfs(i, j, total):
            if (i < 0 or 
                i >= rows or 
                j < 0 or 
                j >= cols or 
                grid[i][j] == 0):
                return total + 1
            
            if grid[i][j] == -1:
                return total
            
            # Mark as visited
            grid[i][j] = -1
            
            # run through all directions
            total = dfs(i+1, j, total)
            total = dfs(i-1, j, total)
            total = dfs(i, j+1, total)
            total = dfs(i, j-1, total)
            
            return total

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j, total)
                
sol = Solution()
print(sol.islandPerimeter(grid = [[0,1,0,0],
                                  [1,1,1,0],
                                  [0,1,0,0],
                                  [1,1,0,0]])) # 16
