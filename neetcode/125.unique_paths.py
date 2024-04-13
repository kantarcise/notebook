"""
There is a robot on an m x n grid. 

The robot is initially located at the top-left corner (i.e., grid[0][0]). 

The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 

The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique 
paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will 
be less than or equal to 2 * 10^9.

Example 1:

    Input: m = 3, n = 7
    
    Output: 28

Example 2:

    Input: m = 3, n = 2
    
    Output: 3

    Explanation: From the top-left corner, 
        there are a total of 3 ways to reach the bottom-right corner:

        1. Right -> Down -> Down

        2. Down -> Down -> Right

        3. Down -> Right -> Down
 
Constraints:

    1 <= m, n <= 100

Takeaway:

    It is a 2D DP problem.

    Literally a math problem, we add bottom and right
    to get the value on current tile!
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # once we move to bottom or right, 
        # we are limited in places that we can go to 
        
        # we are doiing repeated work.
        
        # the closest to the star, 
        # we need the values of those tiles 
        # we can do bottom up DP
        
        #   -----------
        #   |         |
        #   |   AC    |
        #   |   B    X|
        #   -----------
        
        # Tile A is equal to Sum of B and C
        
        # out of bounds should be 0
        # end poisition can be 1
        
        # than we can do:
        
        #   -----------
        #   |         |
        #   |         |
        #   |111111111|
        #   -----------
        
        # all bottom row is 1, because base case is 1
        
        # if we go one row up:
        
        #   -----------
        #   |         |
        #   |765432311|
        #   |111111111|
        #   -----------
        
        # bottom row
        row = [1] * n
        
        # go through other rows
        for i in range(m - 1):
            # this is above the old row
            new_row = [1] * n
            
            # go through every column except
            # rightmost column
            # because that will be just 1's
            for j in range(n - 2, -1, -1):
                # through right to left
                # new_value = right value + value below
                new_row[j] = new_row[j+1] + row[j]
            
            # update the row
            row = new_row
            
        # in the first row, we want the first variable
        return row[0]
