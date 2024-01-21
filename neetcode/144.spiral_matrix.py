"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Takeaway:

Using pointers to keep doing an operation is really smart.

Which is the main takeaway here honestly.


"""

class Solution:
    def spiralOrder__(self, matrix: list[list[int]]) -> list[int]:
        """This is NOT a great idea"""

        # we can use sizesof the matrix to decide our approach
        rows, cols = len(matrix), len(matrix[0])
        
        # we can use an index set to keep visited coordinates
        visited = set() # (i, j)
        
        def forward():
            pass
        
        def down():
            pass
        
        def up():
            pass
        
        for i in range(rows):
            pass
        
    def spiralOrder_(self, matrix: list[list[int]]) -> list[int]:  
        # unreal
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        return res

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:  
        # neet
        # we can use 4 pointers to decide 
        # where our algorithm should stop
        
        # left, right, top, bottom
        
        # after outer layers, we will check the inner matrix
        
        # once pointers reach each other, we will stop
        
        # every time we bump into a edge, we increase a pointer
        
        res = []
        left, right = 0, len(matrix[0]) # not -1, right out of bounds start
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            
            # get every i in the top row
            for i in range(left, right):
                # right not inclusive, nice!
                res.append(matrix[top][i])
                
            top += 1
            
            # get every ith element on the right col
            
            for i in range(top, bottom):
                # bottom not inclusive, nice!
                res.append(matrix[i][right - 1])
                
            # decrement right by 1
            right -= 1
            
            # intermission check for single row or single col matrixes
            if not (left < right and top < bottom):
                break

            # get every ith range from bottom row
            for i in range(right - 1, left - 1, -1):
                # go from right to left in reverse order
                res.append(matrix[bottom - 1][i])
                
                
            # decrement bottom by 1
            bottom -= 1
            
            # get every i in the left most col
            for i in range(bottom -1, top - 1 , -1):
                # bottom to top in reverse order
                res.append(matrix[i][left])
            
            left += 1
            
        return res