"""
You are given a m x n 2D grid initialized with 
these three possible values.

 -1 - A wall or an obstacle.

 0 - A gate.

 INF - Infinity means an empty room. We use the 
    value 2^31 - 1 = 2147483647 to represent INF as 
    you may assume that the distance to a gate 
    is less than 2147483647.

Fill each empty room with the distance to its 
nearest gate. If it is impossible to reach a 
Gate, that room should remain filled with INF

Example 1:

Input: [[2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647,- 1],
        [0, -1, 2147483647, 2147483647]]

Output: [[3, -1, 0, 1],
         [2, 2, 1, -1],
         [1, -1, 2, -1],
         [0, -1, 3, 4]]

Explanation:

the 2D grid is:

INF  -1  0  INF

INF INF INF  -1

INF  -1 INF  -1

  0  -1 INF INF

the answer is:

  3  -1   0   1

  2   2   1  -1

  1  -1   2  -1

  0  -1   3   4

Example 2:

Input: [[0, -1],
        [2147483647, 2147483647]]

Output: [[0, -1],
         [1, 2]]

Takeaway:

BFS is cool to use. Because if we tried to do DFS
calculations would mix from gates at different coordinates.

With BFS, there comes a deque and set :)


"""
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        # we can try a dfs solution where we run 
        # dfs on every single cell
        # and update min distance to gate
        # can we do better than this complexity ?

        # we can use bfs
        # simultainously start from all gates 
        # and mark islands with distances
        
        # we will stop when all islands are marked
        # so we do not do repeated work 

        # for this, we will use a queue with 
        # all positions of gates
        rows, cols = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def add_room(r, c):
            # if out of bounds OR visited OR wall
            if (r < 0 or r == rows or 
                c < 0 or c == cols or
                (r, c) in visit or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        # add all gates into the q and visited set
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                add_room(r + 1, c)
                add_room(r - 1, c)
                add_room(r, c + 1)
                add_room(r, c - 1)
            dist += 1

if __name__ == "__main__":
    sol = Solution()
    a = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]

    print(a)
    sol.wallsAndGates(a)
    print(a) # [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
