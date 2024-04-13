"""
You are given an n x n 2D matrix representing an image, rotate 
the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to 
modify the input 2D matrix directly. 

DO NOT allocate another 2D matrix and do the rotation.

Example 1:

    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
Constraints:

    n == matrix.length == matrix[i].length
    
    1 <= n <= 20
    
    -1000 <= matrix[i][j] <= 1000

Takeaway:

    We got a really smart solution, and a simple one.

    Understanding both is cool.
"""

class Solution:
    
    def rotate_(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we need to hold values before moving them.
        
        # set top, bottom, left, right boundaries.
        # we make movements based on offsets by these boundaries
       
        #       left    right    
        #        ___________
        # top    |          |
        #        |          |
        #        |          |
        #        |          |
        # bottom |__________|
        
        
        # after we shift the outer most layer, we will just 
        # move out pointers to be fitting for the matrix inside 
        
        #     left  right
        #        ___
        #   top |   |
        #       |   |    
        # bottom|___|
        #       
        
        # when pointers cross each other, we can stop
        
        # instead of A LOT of temporary variables, just keep top left inside temp
        # move values starting from the end
        # at LAST, move the temp to its place
        
        l , r = 0, len(matrix[0]) - 1
        
        while l < r:
            # we will use i for coordinates that are not corners
            for i in range(r - l):
                
                top, bottom = l, r
                
                # save the top_left
                # add +i to shift 1 position to the right
                top_left = matrix[top][l + i]
                
                # move bottom left into top_left
                # - i from bottom which will shift us up by 1
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move the top left into top right,
                # we saved it!
                matrix[top + i][r] = top_left
                
            # move pointers so that you can go in for inner matrix
            r -= 1
            l += 1
                
    def rotate(self, matrix: list[list[int]]) -> None:
        """Instead of the solution above, you can do two operations on the matrix
        """
        
        # 90 degree rotation == Transpose and reflect the matrix
        
        def transpose(matrix):
            n = len(matrix[0])
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reflect(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]

        
        transpose(matrix)
        reflect(matrix)
