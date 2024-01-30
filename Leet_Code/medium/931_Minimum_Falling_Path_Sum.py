"""
Given an n x n array of integers matrix, return the minimum 
sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the 
element in the next row that is either directly below or diagonally 
left/right. Specifically, the next element from position (row, col) will 
be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

Takeaway:

A DP question.

tabulation - bottom up solution

float("inf") is a classic.

"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # we will select single number from every row
        # we can always start at min ?
        
        # dp 
        # tabulation
        # bottom up solution
        # start from last row and go up as you add the values from the upper row
        
        # 2 1 3 
        # 6 5 4
        # 7 8 9
        
        # after one step
        
        # 2  1  3 
        # 13 12 12
        
        # after one more step
        
        # 14 13 15
        
        n = len(matrix)
        
        for r in range(1, n):
            for c in range(n):
                mid = matrix[r - 1][c]
                left = matrix[r - 1][c - 1] if c > 0 else float("inf")
                right = matrix[r - 1][c + 1] if c < n - 1 else float("inf")
                matrix[r][c] = matrix[r][c] + min(mid, left, right)
                
        # as we constructed a sum row, find the minimum of last row
        return min(matrix[-1])
