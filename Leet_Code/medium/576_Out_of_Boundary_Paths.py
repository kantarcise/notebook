"""
There is an m x n grid with a ball. The ball is initially at the 
position [startRow, startColumn]. You are allowed to move the ball to one 
of the four adjacent cells in the grid (possibly out of the grid 
crossing the grid boundary). You can apply at most maxMove moves 
to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number 
of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo 10**9 + 7.

Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:

Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 
Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

Takeaway:

DP question

Cache the solution. 

"""
class Solution: 
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod=10**9+7
        
        cache={}
        
        def dp(move, row, col):
            if move > maxMove:
                return 0
            # out of bounds  
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1

            # if we already made this calculation
            if (move, row, col) in cache:
                return cache[(move, row, col)] % mod

            # onto next move
            cache[(move, row, col)] = (dp(move + 1, row - 1, col) +
                                       dp(move + 1, row, col - 1) +
                                       dp(move + 1, row + 1, col) +
                                       dp(move + 1, row, col + 1)) % mod
            return cache[(move, row, col)]
        
        return dp(0, startRow, startColumn) % mod
