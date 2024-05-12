"""
You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of 
size (n - 2) x (n - 2) such that:

    maxLocal[i][j] is equal to the largest 
    value of the 3 x 3 matrix in grid centered 
    around row i + 1 and column j + 1.

    In other words, we want to find the largest value 
    in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.

Example 1:

    Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    
    Output: [[9,9],[8,6]]
    
    Explanation: Notice that each value in the 
    generated matrix corresponds to the largest value 
    of a contiguous 3 x 3 matrix in grid.

Example 2:

    Input: grid = [[1,1,1,1,1],[1,1,1,1,1],
                    [1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    
    Output: [[2,2,2],[2,2,2],[2,2,2]]
    
    Explanation: Notice that the 2 is contained 
        within every contiguous 3 x 3 matrix in grid.
 
Constraints:

    n == grid.length == grid[i].length
    3 <= n <= 100
    1 <= grid[i][j] <= 100

Takeaway:

    If you do not think about your solution, you 
    have a chance of 0
"""

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        # we are looking for 3x3 maxes
        
        # find rows and cols
        # for each row, check
        
        # i, j would be base
        # find correct i, j == inbounds
        # find max
        # for those i,j set result
        # result[0][0] - 0,0
        # result[0][1] - 0,1

        def findmax(list_of_lists):
            return max([elem for sublist in list_of_lists for elem in sublist])

        r, c  = len(grid), len(grid[0])
        result = [[0] * (r - 2) for _ in range(c-2)]
        
        # print(result)
        for i in range(r-2):
            for j in range(c-2):
                result[i][j] = findmax([grid[i][j:j+3],
                                        grid[i+1][j:j+3],
                                        grid[i+2][j:j+3]])
        
        return result


sol = Solution()
print(sol.largestLocal(grid = [[9,9,8,1],
                               [5,6,2,6],
                               [8,2,6,4],
                               [6,2,2,2]]))

print(sol.largestLocal(grid = [[1,1,1,1,1],
                               [1,1,1,1,1],
                               [1,1,2,1,1],
                               [1,1,1,1,1],
                               [1,1,1,1,1]]))
