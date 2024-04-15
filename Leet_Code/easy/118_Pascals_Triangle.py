"""
Given an integer numRows, return the first 
numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the 
two numbers directly above it as shown:

Example 1:

    Input: numRows = 5
    
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

    Input: numRows = 1
    
    Output: [[1]]

Constraints:

    1 <= numRows <= 30

Takeaway:

    Simply, understand the problem, walk line by line.
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # we can make a result list

        # based on the row level
        # we can calculate inner values
        # based on the upper level values

        # each level will have 1's in the both ends
        result = []

        # we should start at 1 to make the top of pyramid
        for i in range(1, numRows + 1):
            
            # a simple template, 1 in boths sides 
            row = [1] * i

            for j in range(1, i - 1):
                # starting from 1st index,
                # fill the row with upper level values
                row[j] = result[i - 2][j] + result[i - 2][j - 1]
            
            # add current row to result
            result.append(row)

        # return result.
        return result

    def generate_(self, numRows: int) -> list[list[int]]:
        # another approach
        
        # we can start with top of pyramid
        triangle = [[1]]
        
        for i in range(1, numRows):
            
            # deepest row will always be in the end 
            # of the triangle list
            prev_row = triangle[-1]
            
            # new row can initialize with a 1 on left 
            new_row = [1]
            
            for j in range(1, len(prev_row)):
                # pascal calculation
                new_row.append(prev_row[j-1] + prev_row[j])
            
            # the 1 on right
            new_row.append(1)

            # add to triangle
            triangle.append(new_row)
        
        return triangle

sol = Solution()
print(sol.generate(5))
print(sol.generate_(5))