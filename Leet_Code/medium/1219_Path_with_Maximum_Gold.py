"""
In a gold mine grid of size m x n, each cell 
in this mine has an integer representing 
the amount of gold in that 
cell, 0 if it is empty.

Return the maximum amount of gold you 
can collect under the conditions:

    Every time you are located in a 
    cell you will collect all the gold in that cell.
    
    From your position, you can walk one 
    step to the left, right, up, or down.
    
    You can't visit the same cell more than once.
    
    Never visit a cell with 0 gold.
    
    You can start and stop collecting gold from 
    any position in the grid that has some gold.
 
Example 1:

    Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
    
    Output: 24
    
    Explanation:
        [[0,6,0],
         [5,8,7],
         [0,9,0]]
    
        Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

    Input: grid = [[1,0,7],[2,0,6],
                    [3,4,5],[0,3,0],[9,0,20]]
    
    Output: 28
    
    Explanation:
    
        [[1,0,7],
         [2,0,6],
         [3,4,5],
         [0,3,0],
         [9,0,20]]
    
        Path to get the maximum gold, 
            1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:

    m == grid.length
    
    n == grid[i].length
    
    1 <= m, n <= 15
    
    0 <= grid[i][j] <= 100

    There are at most 25 cells containing gold.

Takeaway:

    using dfs, and backtracking

    there could be more than 1 
    search on different parts of the mine! 

"""

class Solution:
    def getMaximumGold_(self, 
                        grid: list[list[int]]) -> int:
        # DOES NOT WORK
        
        # we can use dfs on each non 0 cell
        # we can find all paths
        # sort them and return the max
        
        r, c = len(grid), len(grid[0])
        
        result = []
        
        def dfs(i, j, path):
            if (i < 0 or 
                j < 0 or 
                i >= r or 
                j >= c or 
                grid[i][j] == '0'):
                    return path
			# make the current tile 0
			# so you will not count this tile again
            result.append(grid[i][j])
            grid[i][j] = '0'

			# go to every direction possible
            dfs(i - 1, j, result.copy())
            dfs(i + 1, j, result.copy())
            dfs(i, j - 1, result.copy())
            dfs(i, j + 1, result.copy())
            
        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    dfs(i, j, [])
                    
        for elem in result:
            elem.sort()
        
        result.sort()
        return result[-1]
    
    def getMaximumGold(self, 
                       grid: list[list[int]]) -> int:
        # get row and col
        r, c = len(grid), len(grid[0])
        
        def dfs(i, j, path):
            if (i < 0 or j < 0 or 
                i >= r or j >= c or 
                grid[i][j] == 0):
                # if out of bounds
                # or value is 0
                return path
            
            temp = grid[i][j]
            grid[i][j] = 0
            path += temp
            
            # find the max value that will 
            # increase our path the most
            max_path = max(dfs(i - 1, j, path), 
                           dfs(i + 1, j, path), 
                           dfs(i, j - 1, path), 
                           dfs(i, j + 1, path))
            
            # set grid value back to temp
            grid[i][j] = temp
            
            # return max possible path
            return max_path
        
        # we will try a lot of dfs's
        # and will return the max 
        # path among them
        max_gold = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, 
                                   dfs(i, j, 0))
                    
        return max_gold
    
sol = Solution()
print(sol.getMaximumGold(grid = [[0,6,0],
                                 [5,8,7],[0,9,0]])) 
