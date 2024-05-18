"""
You are given an m x n binary matrix grid.

A move consists of choosing any row or column 
and toggling each value in that row or 
column (i.e., changing all 0's to 1's, and 
all 1's to 0's).

Every row of the matrix is interpreted as 
a binary number, and the score of the matrix is 
the sum of these numbers.

Return the highest possible score after 
making any number of 
moves (including zero moves).

Example 1:

    Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    
    Output: 39
    
    Explanation: 
    
        0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:

    Input: grid = [[0]]
    
    Output: 1

Constraints:

    m == grid.length
    
    n == grid[i].length
    
    1 <= m, n <= 20
    
    grid[i][j] is either 0 or 1.

Takeaway:

    You can switch an integer with:

    a = 1 - a

    use indexes to do stuff, row and col wise

"""

from collections import defaultdict

class Solution:
    def matrixScore_(self, 
                     grid: list[list[int]]) -> int:
        # doesnt work
        # NOT A GOOD IDEA
        # to try to make rows and cols
        # a parameter of a nested function
        
        # we will want to make 
        # all 1s in 0 col
        # just from left right, top bottom
        # flip values
        
        def flip(my_list):
            for i in range(len(my_list)):
                if my_list[i] == 1:
                    my_list[i] = 0
                else:
                    my_list[i] = 1
            return my_list
        
        def flip_on_total(a_col):
            pass
        
        r, c = len(grid), len(grid[0])
        
        for i in range(r):
            # only check leftmost bit
            if grid[i][0] == 0:
                grid[i] = flip(grid[i])
            """
            left, right = 0, c - 1
            while left < right:
                if grid[i][left] < grid[i][right]:
                    # flip
                    grid[i] = flip(grid[i])
                    break
                left += 1
                right -= 1
            """    
        for j in range(c):
            # if total 0's are more than 
            # 1's, flip
            total_1 = 0
            map = defaultdict(int)
            # cannot use star expression ?
            for elem in (zip(grid)):
                # jth col for every row
                for index in range(r):
                    map[elem[index]] += 1
                if map[1] < map[0]:
                    for index_2 in range(r):
                        grid[index_2][j] = 1 \
                            if grid[index_2][j] == 0 else 0
        
        return sum(int("".join(elem for elem in grid)), 
                   base = "2")        
            
    def matrixScore(self, 
                    grid: list[list[int]]) -> int:
        # get number of cols, rows
        r, c = len(grid), len(grid[0])
        
        # Make the leftmost column all 1's
        for i in range(r):
            # if the first value is 0
            # flip all
            if grid[i][0] == 0:
                for j in range(c):
                    grid[i][j] = 1 - grid[i][j]
        
        # Make the rest of the columns 
        # have more 1's than 0's
        # careful!
        # j starts from 1! 
        for j in range(1, c):
            ones = sum(grid[i][j] for i in range(r))
            if ones <= r // 2:
                for i in range(r):
                    grid[i][j] = 1 - grid[i][j]
        
        # Calculate the score
        score = 0
        for row in grid:
            score += int(''.join(str(x) for x in row), 2)
        
        return score
    
sol = Solution()
print(sol.matrixScore(grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]))
