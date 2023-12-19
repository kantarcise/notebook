"""
An image smoother is a filter of the size 3 x 3 that can be applied to 
each cell of an image by rounding down the average of the cell and the eight 
surrounding cells (i.e., the average of the nine cells in the blue smoother). 
If one or more of the surrounding cells of a cell is not present, we do 
not consider it in the average (i.e., the average 
of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an 
image, return the image after applying the smoother on each cell of it. 

Example 1:

Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:

Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
 
Constraints:

m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255

Takeaway:

Using min() and max() for edge cases is so cool.

"""

class Solution:
    def imageSmoother_(self, img: List[List[int]]) -> List[List[int]]:
        # I have failed.
        # I understood that there is an different situation for each pixel
        # but I could not find a solution in time
        # we have an m by n matrix
        
        m = len(img)
        n = len(img[0])
        
        filter = [ [1] * 3 for _ in range(3)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    img[i][j] = img[i-1][j-1] 
                img[i][j] = img[i][j]  * filter[i][j]
                
        return img
    
    def imageSmoother__(self, img):
        # from a homie
        rows = len(img)
        cols = len(img[0])
        
        # make the result matrix
        
        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # for each pixel:
                total_sum = 0
                count_of_nonzero = 0

                
                # max(0, i-1): Ensures that the iteration starts from the 
                #       maximum of 0 and i-1 to avoid going below the first row of the image.
                # min(rows, i+2): Ensures that the iteration stops at the minimum of the 
                #       total number of rows (rows) and i+2 to avoid going beyond the last row of the image.
                for l in range(max(0, i-1), min(rows, i+2)):
                    
                    # max(0, j-1): Ensures that the iteration starts from the maximum of 
                    #       0 and j-1 to avoid going to the left of the first column of the image.
                    # min(cols, j+2): Ensures that the iteration stops at the minimum of the 
                    #       total number of columns (cols) and j+2 to avoid going beyond the 
                    #       right of the last column of the image.
                    for k in range(max(0, j-1), min(cols, j+2)):
                        total_sum += img[l][k]
                        count_of_nonzero += 1

                result[i][j] = total_sum // count_of_nonzero

        return result
    
    def imageSmoother(self, img):
        
        rows = len(img)
        cols = len(img[0])
        
        # make the result matrix
        
        result = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                # make the calculation
                total_sum = 0
                count_of_nonzero = 0
                for l in range(max(0, i -1), min(rows, i+2)):
                    for k in range(max(0, j - 1), min(cols, j + 2)):
                        total_sum += img[l][k]
                        count_of_nonzero +=1
                
                result[i][j] = total_sum // count_of_nonzero                
                
        return result
