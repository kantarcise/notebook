"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent 
to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell 
has a fresh orange. If this is impossible, return -1.

Example 1:

    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    
    Output: 4

Example 2:

    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    
    Output: -1
    
    Explanation: 
    
        The orange in the bottom left corner (row 2, column 0) 
            is never rotten, because rotting only happens 4-directionally.

Example 3:

    Input: grid = [[0,2]]
    
    Output: 0
    
    Explanation: 
    
        Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.

Takeaway:

    DFS wont work because, oranges rot at the same time
    if there are more than 1 rotten oranges
    we cannot count time rightfully

    we should do a multi source BFS
    BFS is implemented with, usually using a queue
    if after BFS is done, 
    there are still fresh oranges
    we cannot rot the table, Return -1
"""

from collections import deque

class Solution:
    def orangesRotting__(self, grid: list[list[int]]) -> int:
        # just try
        # kinda like a fool
        # a fool is the precursor to savior
        
        counter = 0
        rows , cols = len(grid), len(grid[0])
        
        # if we bump into a rotten orange,
        # we will rot all 4 other directions
        
        # if all rotten we stop
        
        def dfs(r, c, rot):
            if (r < 0 or c < 0 or
                r == rows or c == cols or             
                grid[r][c] in [0, 1]):
                return
            
            # rotten orange
            counter += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
                
        dfs(0, 0)
        return counter
                
    def orangesRotting_(self, grid: list[list[int]]) -> int:
        # this works

        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
        
        fresh, rotten = set(), deque()

        # iterate through the grid to get all 
        # the fresh and rotten oranges
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if we see a fresh orange, put its position in fresh
                if grid[row][col] == 1:
                    fresh.add((row, col))

                # if we see a rotten orange, put its position in rotten
                elif grid[row][col] == 2:
                    rotten.append((row, col))

        minutes = 0
        # If there are rotten oranges in the queue and 
        # there are still fresh oranges in the grid 
        # keep looping
        while fresh and rotten:

            minutes += 1

            # iterate through rotten, popping off the (row, col) that's currently in rotten
            # we don't touch the newly added (row, col) that are added during the loop until the next loop
            for rot in range(len(rotten)):
                row, col = rotten.popleft()

                for direction in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if direction in fresh:
                        # if the (row, col) is in fresh, remove it then add it to rotten
                        fresh.remove(direction)
                        # we will perform 4-directional checks on each (row, col)
                        rotten.append(direction)

        # if fresh is not empty, then there is an orange we were not able to reach 4-directionally    
        return -1 if fresh else minutes

        
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # dfs wont work because, oranges rot at the same time
        # if there are more than 1 rotten oranges
        # we cannot count time rightfully
        
        # we should do a multi source bfs
        # bfs is implemented with, usually using a queue
        # if after bfs is done, 
        # there are still fresh oranges
        # we cannot rot the table
        
        q = deque()
        time, fresh = 0, 0
        
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
                    
        # make directions list
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while q and fresh > 0:
            
            for i in range(len(q)):
                # this is a queue so not pop, popleft
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # if in bounds and fresh, make rotten
                    if (row < 0 or row == len(grid) or
                       col < 0 or col == len(grid[0])
                       or grid[row][col] != 1):
                        continue
                    # else rot it
                    grid[row][col] = 2
                    # add the new rotten orange to queue
                    q.append([row, col])
                    fresh -= 1
            time += 1
            
        return time if fresh == 0 else -1
