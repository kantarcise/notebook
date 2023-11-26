"""

You are given a 0-indexed m x n integer matrix mat and an integer k. 
You have to cyclically right shift odd indexed rows k times and 
cyclically left shift even indexed rows k times.

Return true if the initial and final matrix are exactly the same and false otherwise.

Example 1:

Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
Output: true

Example 2:

Input: mat = [[2,2],[2,2]], k = 3
Output: true
Explanation: As all the values are equal in the matrix, even after performing 
cyclic shifts the matrix will remain the same. Therefeore, we return true.

Example 3:

Input: mat = [[1,2]], k = 1
Output: false
Explanation: After one cyclic shift, mat = [[2,1]] which is 
not equal to the initial matrix. Therefore we return false.
 
Constraints:

1 <= mat.length <= 25
1 <= mat[i].length <= 25
1 <= mat[i][j] <= 25
1 <= k <= 50

Takeaway:

The idea of comparing equality and returning was cool.

But you need to understand that cyclic shifting is really modding in disguise.

For lists, the absolute value for the index total is always the same

                      0  1   2   3   4
my_colleciton =     [ 1, 2 , 3 , 4 , 5]
                     -5 -4  -3  -2  -1

my_collection[2:]   # [3, 4, 5]

my_collection[-2:]  # [ 4, 5]

"""

class Solution:
    def areSimilar_(self, mat: List[List[int]], k: int) -> bool:
        
        # my solution did not work
        # skill issue.
        copy_mat = mat[:]
        for row_index, row in enumerate(mat):
            if row_index % 2  == 1:

                # right shift
                for i in range(k-1):
                    row.insert(0, row.pop())
                # pass
            else:
                # left shift
                for i in range(k-1):
                    row.insert(-1, row.pop(0))
        
        return mat == copy_mat
            
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # from a homie
        
        number_of_rows = len(mat)
        number_of_cols = len(mat[0])
        
        # its the modded value for it really.
        possible_shifts = k % number_of_cols
        
        if possible_shifts == 0:
            # its like not even shifting anything
            return True
        
        # other matrix
        mat2 = []
        
        for i in range(number_of_rows):
            # get the first row
            row = mat[i]
            
            # even
            if i % 2 == 0:
                # starting from shift position, concat the remainder
                # row2 = row[2:] + row[:2]
                row2 = row[possible_shifts:] + row[:possible_shifts]
                mat2.append(row2)
            
            # odd
            else:
                # the same bu other direction
                # row2 = row[-2:] + row[:4 - 2]
                row2 = row[-possible_shifts:] + row[:number_of_cols - possible_shifts]
                mat2.append(row2)
        
        return mat2 == mat
