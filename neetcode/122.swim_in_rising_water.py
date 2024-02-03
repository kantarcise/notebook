"""
You are given an n x n integer matrix grid where 
each value grid[i][j] represents the elevation 
at that point (i, j).

The rain starts to fall. 

At time t, the depth of the  water everywhere is t.
You can swim from a square to another 4-directionally 
adjacent square if and only if the elevation of both 
squares individually are at most t. 

You can swim infinite distances in zero time. 
Of course, you must stay within the boundaries of 
the grid during your swim.

Return the least time until you can reach 
the bottom right square (n - 1, n - 1) 
if you start at the top left square (0, 0).

Example 1:

Input: grid = [[0,2],[1,3]]

Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.

Takeaway:

Djikstra is basically a BFS but 
instead of a normal queue
we use a priority queue, which is a heap in Python

"""

from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # neet
        
        # this question is basically asking what path can 
        # we take so that the height is minimized, 
        # which minimizes t
        
        # we could look at every path and return the one 
        # with min(max_height) but that would be exponential
        
        # so we use Djikstra!
        
        # Djikstra is basically a BFS but 
        # instead of a normal queue
        # we use a priority queue, which is a heap in Python
        
        
        #                                           min_heap
        
        # 0---1---3                                (0, r, c)
        # |   |   |    - right,bottom         (1,r,c) (2,r,c)
        # 2---4---1    - from 1 right bottom  (3,r,c) (4,r,c)         
        # |   |   |    - pop min, go back to 2 -      (2,r,c)
        # 1---2---1    - 2 is still min, go right,    (2,r,c)
        #              - go right                     (2,r,c) 
        #              - we are at the end!       
        
        # we never popped (3,r,c) or (4,r,c)
        # because we are using a priority queue!
            
        # a modified Djikstra because each time we add a value to the heap
        # we want to add it with the current height and 
        # the height that came before it
        
        # max(cur_heig, prev_heig)
        
        N = len(grid)
        
        visit = set()
        
        # [time/max-height, r, c]
        min_heap = [[grid[0][0], 0 , 0]]
                    
        # only valid directions            
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    
        visit.add((0, 0))
        # while our min heap is not empty
        while min_heap:
            t, r, c = heappop(min_heap)
                    
            # when do we stop?
            # if we reached to the destination
            if r == N - 1 and c == N - 1:
                return t
                    
            for dr, dc in directions:
                nei_row, nei_col = r + dr, c + dc
                # check out of bounds for these neighbours
                # and/or already visited
                if ((nei_row < 0 or nei_col < 0 or 
                   nei_row == N or nei_col == N) or
                    (nei_row, nei_col)  in visit):
                    continue
                visit.add((nei_row, nei_col))
                heappush(min_heap, 
                         [max(t, grid[nei_row][nei_col]),
                          nei_row,
                          nei_col])
                    
            