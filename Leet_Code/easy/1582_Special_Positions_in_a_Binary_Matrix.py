"""
Given an m x n binary matrix mat, return the number of 
special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all 
other elements in row i and column j are 0 (rows and 
columns are 0-indexed).

Example 1:

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:

Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.

Takeaway:

Using DFS is cool. 

Do not forget how you can get the # of rows and columns in a given matrix.

"""

class Solution:
    def numSpecial_(self, mat: List[List[int]]) -> int:
        # find all 1 positions
        # check if there are any 1's in the same row, 
        # check if there are any 1's in the same column
        output = 0
        for index, row in enumerate(mat):
            for j, elem in enumerate(row):
                if elem == 1:
                    if sum(row) == 1: # only one 1 in that row
                        if sum([elem[j] for elem in mat]) == 1: # only one 1 in that column 
                            output +=1
        return output
                    
    def numSpecial(self, mat: List[List[int]]) -> int:
        # from a homie, using dfs
        
        # number of rows
        n = len(mat)
        # number of columns
        m = len(mat[0])

        # specialized dfs for checking condition
        def dfs(x, y):
            for i in range(m):
                if mat[x][i] == 1 and i != y:
                    return False

            for j in range(n):
                if mat[j][y] == 1 and j != x:
                    return False
            return True


        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        
        return count
