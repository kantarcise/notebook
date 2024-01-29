"""
Given a matrix and a target, return the number of 
non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all 
cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are 
different if they have some coordinate 
that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:

Input: matrix = [[904]], target = 0
Output: 0

Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8

Takeaway:

Sometimes there is no other way to go with brute force

However, after that we can focus on optimizations.

Presum and caching is the key here
"""

from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget_(self, matrix: List[List[int]], target: int) -> int:
        # brute force would be check the every single submatrices
        # and compare sum to the target
        # use 4 pointers to decide the submatrices
        
        # 4 for loops to find the submatrice
        # 2 more to sum them
        
        # o(n^6)
        pass
    
    def numSubmatrixSumTarget__(self, matrix: List[List[int]], target: int) -> int:
        # can we optimize - o(n^6) ? 
        # WE CAN 
        # BUT THIS APPROACH TIME LIMIT EXCEEDS
        # we can use a prefix sum to find the submatrices sums!
        
        # [ - , - , - , - , - ]
        #           |   |
        #          total here
        # is the total of [:4] MINUS  first two [:2]
        
    
        # SUBMARTIX SUM
        
        #        c1 c2
        #    0   1   0
        # r1 1   0   1
        # r2 0   1   0 
        
        
        # for finding total at
        
        #    _   _   _  
        #    _   1   1
        #    _   1   0
        
        # WE SUBTRACT THE SMALL TOP LEFT TWICE, WE NEED TO ADD IT BACK
        
        # total  =  subsum[r2][c2] - sub_sum[r2][c1 - 1] - sub_sum][r1-1][c2] + sub_sum[r1-1][c1-1]        
        
        # this way we decreased time complexity to o(n^6) to o(n^4)
        
        rows, cols = len(matrix), len(matrix[0])
        sub_sum = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                top = sub_sum[r - 1][c] if r > 0 else 0
                left = sub_sum[r][c - 1] if c > 0 else 0
                top_left = sub_sum[r - 1][c - 1] if min(r, c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left
        
        res = 0 
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        top = sub_sum[r1-1][c2] if r1 > 0 else 0
                        left = sub_sum[r2][c1-1] if c1 > 0 else 0
                        top_left = sub_sum[r1-1][c1-1] if min(r1, c1) > 0 else 0
                        cur_sum = sub_sum[r2][c2] - top - left + top_left
                        if cur_sum == target:
                            res +=1
        return res
    
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # can we overcome the time limit exceeding?
        # we can use a prefix sum to find the submatrices sums!
        
        # WE SUBTRACT THE SMALL TOP LEFT TWICE, WE NEED TO ADD IT BACK
        
        # total  =  subsum[r2][c2] - sub_sum[r2][c1 - 1] - sub_sum][r1-1][c2] + sub_sum[r1-1][c1-1]        
        
        # this way we decreased time complexity to o(n^6) to o(n^4)
        
        rows, cols = len(matrix), len(matrix[0])
        sub_sum = [[0] * cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                top = sub_sum[r - 1][c] if r > 0 else 0
                left = sub_sum[r][c - 1] if c > 0 else 0
                top_left = sub_sum[r - 1][c - 1] if min(r, c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left
        
        res = 0 
        for r1 in range(rows):
            for r2 in range(r1, rows):
                count = defaultdict(int)
                count[0] = 1
                for c in range(cols):
                    cur_sum = sub_sum[r2][c] - (
                        sub_sum[r1 - 1][c] if r1 >  0 else 0
                    )
                    diff = cur_sum - target
                    res += count[diff]
                    count[cur_sum] += 1
        return res
    
