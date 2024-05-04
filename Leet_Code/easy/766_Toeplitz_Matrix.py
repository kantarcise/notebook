"""
Given an m x n matrix, return true if 
the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal 
from top-left to bottom-right has the same elements.

Example 1:

    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

    Output: true

    Explanation:
        In the above grid, the diagonals are:
      "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
      In each diagonal all elements are the same, so the answer is True.

Example 2:

    Input: matrix = [[1,2],[2,2]]

    Output: false

    Explanation:
        The diagonal "[1, 2]" has different elements.
 
Constraints:

    m == matrix.length

    n == matrix[i].length

    1 <= m, n <= 20
  
    0 <= matrix[i][j] <= 99
 
Follow up:

What if the matrix is stored on disk, and the 
memory is limited such that you can only load 
at most one row of the matrix into the memory 
at once?

What if the matrix is so large that you can 
only load up a partial row into the memory at once?

Takeaway:

    Sometimes, only way is through.
"""
class Solution:
    def isToeplitzMatrix_(self, matrix: List[List[int]]) -> bool:
        # for every element in the first row
        # and for every element in the first col
        # check diagonals
        m, n = len(matrix), len(matrix[0])
        
        def check_diagonal(i, j):
            val = matrix[i][j]
            while i < m - 1 and j < n - 1:
                i += 1
                j += 1
                if matrix[i][j] != val:
                    return False
            return True
        
        for i in range(m - 1):
            if not check_diagonal(i, 0):
                return False
        for j in range(1, n - 1):
            if not check_diagonal(0, j):
                return False
        return True
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # simple brute force
        flag = False
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    flag = True
                    break
        return flag==False
