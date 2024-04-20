"""
You are given a 0-indexed m x n binary matrix land where a 
0 represents a hectare of forested land and a 1 represents 
a hectare of farmland.

To keep the land organized, there are designated rectangular 
areas of hectares that consist entirely of farmland. 

These rectangular areas are called groups. 

No two groups are adjacent, meaning farmland in one group 
is not four-directionally adjacent to another farmland 
in a different group.

land can be represented by a coordinate system where 
the top left corner of land is (0, 0) and the bottom right corner 
of land is (m-1, n-1). 

Find the coordinates of the top left and bottom right corner of 
each group of farmland. 

A group of farmland with a top left corner at (r1, c1) and a 
bottom right corner at (r2, c2) is represented by 
the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above 
for each group of farmland in land. 

If there are no groups of farmland, return an empty array. 

You may return the answer in any order.

Example 1:

    Input: land = [[1,0,0],[0,1,1],[0,1,1]]
    
    Output: [[0,0,0,0],[1,1,2,2]]
    
    Explanation:
    
        The first group has a top left corner at 
            land[0][0] and a bottom right corner at land[0][0].
    
        The second group has a top left corner at 
            land[1][1] and a bottom right corner at land[2][2].

Example 2:

    Input: land = [[1,1],[1,1]]
    
    Output: [[0,0,1,1]]
    
    Explanation:
    
        The first group has a top left corner at 
            land[0][0] and a bottom right corner at land[1][1].

Example 3:

    Input: land = [[0]]
    
    Output: []
    
    Explanation:
    
        There are no groups of farmland.
 
Constraints:

    m == land.length
    
    n == land[i].length
    
    1 <= m, n <= 300
    
    land consists of only 0's and 1's.

    Groups of farmland are rectangular in shape.

Takeaway:

    Farms have 1 in their cells

    They are always forming some rectangles.

    How can we decide if they are part of the same rectangle?

    If there are no neighbours, just return the indexes, twice.

    We can think of it as a graph problem and use DFS on 
    all cells having the value 1.

    Matrix solution is possible too.
"""

class Solution:
    def findFarmland__(self, land: list[list[int]]) -> list[list[int]]:
        # my first try, did not work
        rows, cols = len(land), len(land[0])
        
        result = []
        seen = set()
        temp = [rows, cols, 0, 0]
        
        def dfs(i, j, current):
            
            if (i < 0 or
               i>= rows or
               j < 0 or j >= cols or
               (i, j) in seen):
                # reset temp
                result.append(current)
                return
            
            # we found a not seen cell
            # possibly min and max values are changing
            
            current[0] = min(current[0] , i)
            current[1] = min(current[1], j)
            current[2] = max(current[2], i)
            current[3] = max(current[3], j)
            
            dfs(i + 1, j, current)
            dfs(i - 1, j, current)
            dfs(i, j + 1, current)
            dfs(i, j - 1, current)
        
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1:
                    dfs(r, c, temp)
                
        return result
    
    def findFarmland_(self, land: list[list[int]]) -> list[list[int]]:
        # works, but slow
        
        rows, cols = len(land), len(land[0])
        result = []
        seen = set()

        def dfs(i, j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or
                    land[i][j] == 0 or (i, j) in seen):
                return

            # Initialize current to be the current cell's coordinates
            current = [i, j, i, j]

            # Update current to include the whole group of farmland
            def expand(r, c):
                if (r < 0 or r >= rows or c < 0 or c >= cols or
                        land[r][c] == 0 or (r, c) in seen):
                    return
                seen.add((r, c))
                current[0] = min(current[0], r)
                current[1] = min(current[1], c)
                current[2] = max(current[2], r)
                current[3] = max(current[3], c)
                expand(r + 1, c)
                expand(r - 1, c)
                expand(r, c + 1)
                expand(r, c - 1)

            expand(i, j)
            result.append(current)

        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1 and (r, c) not in seen:
                    dfs(r, c)

        return result
    
    
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        # solution with just loops
        
        m, n = len(land), len(land[0])
        result = []

        for i in range(0, m):
            for j in range(0, n):
                # if not 1 just skip it
                if land[i][j] != 1:
                    continue
                
                # trying to find the ends
                # end row
                end_i = i
                
                # in bounds and still value == 1
                while end_i + 1 < m and land[end_i+1][j] == 1:
                    # stretch end row
                    end_i += 1
                
                # end column
                end_j = j
                
                # in bounds and still value == 1 
                while end_j + 1 < n and land[i][end_j+1] == 1:
                    # stretch end col
                    end_j += 1
                
                for i2 in range(i, end_i+1):
                    for j2 in range(j, end_j+1):
                        # change all those farm lands
                        # so we do not need to check them again
                        land[i2][j2] = 2
                
                # add final coordinates to result
                result.append([i, j, end_i, end_j])
        
        return result
