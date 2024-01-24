"""
Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's.

You must do it in place.

 
Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

 
Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

 
Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?


Takeaway:

Simply, find the zeroes.

For all row and col values, swipe 
the row or column completely


"""
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we can get the coordinates of all 
        # 0's in single traversion
        zeros = []
        
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
                    
        # for all row and col values, we need to swipe 
        # the row or column completely
        for r, _ in zeros:
            for col in range(cols):
                matrix[r][col] = 0
                
        for _, c in zeros:
            for row in range(rows):
                matrix[row][c] = 0
            
    
        