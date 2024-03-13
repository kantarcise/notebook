"""
Given a positive integer n, find the pivot 
integer x such that:

The sum of all elements between 1 and x inclusively 
equals the sum of all elements between 
x and n inclusively.

Return the pivot integer x. If no such integer 
exists, return -1. It is guaranteed that there 
will be at most one pivot index for the given input.

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 
  1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such 
    integer exist.
 
Constraints:

  1 <= n <= 1000

Takeaway:

  Brute Force -> prefix sum -> binary search

"""
class Solution:
    def pivotInteger__(self, n: int) -> int:
        # 1 to x == x to n
        # brute force
        
        if n == 1:
            return 1
        for i in range(1, n):
            if sum(range(1, i+1)) == sum(range(i, n+1)):
                return i
        return -1
    
    def pivotInteger_(self, n: int) -> int:
        # faster solution
        # using the classic total property
        
        if n == 1:
            return 1
        
        total = (n * (n + 1)) // 2
        left_sum = 0

        for i in range(1, n):
            left_sum += i
            if left_sum == total + i - left_sum:
                return i

        return -1
    
    def pivotInteger(self, n: int) -> int:
        # even faster solution - binary search
        
        left, right = 1, n
        
        total_sum = n * (n + 1) // 2

        # Binary search for the pivot point
        while left < right:
            mid = (left + right) // 2

            # Check if the difference between the square 
            # of mid and the total sum is negative
            if mid * mid - total_sum < 0:
                # Adjust left bound if the sum is smaller
                left = mid + 1  
            else:
                # Adjust right bound if the sum is equal or greater
                right = mid 

        # Check if the square of the left 
        # pointer minus the total sum is zero
        if left * left - total_sum == 0:
            return left
        else:
            return -1
