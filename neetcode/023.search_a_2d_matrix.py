"""

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104


Takeaways:

```
l, r = 0, len(seq) - 1
mid = l + ((r-l)//2) 
```

We dont have to iterate over all elements, not even every row.

we can do double binary search to decide which row we are interested in
and search for the target

This should be obvious also

```ROWS, COLS = len(matrix), len(matrix[0])```


"""


class Solution:
    
    # this time complexity is o(n^2)
    def search_matrix(self, matrix, target):
        # we can simply make a long list from the matrix and run binary search on it
        long_seq = []

        for list in matrix:
            for elem in list:
                long_seq.append(elem)


        low, high = 0 , len(long_seq) - 1

        while low <= high:

            mid = low + ((high - low)//2)

            if target == long_seq[mid]:
                return True
            elif target < long_seq[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False

    # we can check every element one by one at o(m*n)
    # we can run binary search on each row by m * o(log n)

    # instead of m - log (m)
    # we can run a binary search on for which row we are interested in

    def search_matrix_better(self, matrix, target):
        
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # look for the row we are interested in
        top, bottom = 0 , ROWS - 1

        # run until we find target row
        while top <= bottom:
            
            row = bottom + ((top - bottom)//2)

            # if target is even bigger that the last element at the row
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else: 
                # target is in the current row
                break
        
        # if none of the rows contain target value
        if not (top <= bottom):
            # we can immediately return False
            return False

        # second binary search in the row itself:
        # this is the row we are going to run binary search on
        row = bottom + ((top - bottom)//2)
        # COLS because that will be the last element in the row
        l, r = 0, COLS - 1

        while l <= r:
            m = l + ((r-l)//2)
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            else:
                l = m + 1

        return False



if __name__ == '__main__':
    sol = Solution()
    print(sol.search_matrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(sol.search_matrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))

    print("In logn + logm time:")
    print(sol.search_matrix_better(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(sol.search_matrix_better(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))