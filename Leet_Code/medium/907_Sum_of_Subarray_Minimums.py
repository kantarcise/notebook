"""
Given an array of integers arr, find the sum of min(b), where 
b ranges over every (contiguous) subarray of arr. Since the 
answer may be large, return the answer modulo 10**9 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104

Takeaway:

Use a stack to hold indices, not values.

"""

class Solution:
    def sumSubarrayMins_(self, arr: List[int]) -> int:
        # did not work
        result = 0
        # all subarrays
        # [3,1,2]
        # 0, 1, 2
        for i in range(len(arr)):
            # 1, 2, 3
            for j in range(i+1, len(arr)+1):
                result += min(arr[i:j])
                
        return result % (int(10e9) + 7)
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # for the answer
        MOD = 10**9 + 7
        
        # stack is initialized with -1. It will be used to 
        # keep track of indices in a way that ensures the 
        # elements in arr are in non-decreasing order within the stack.
        stack = [-1] 
        
        res = 0
        # append an additional 0 to the end of the arr. 
        # This is done to ensure that all elements in the stack
        # are eventually popped
        arr.append(0)
        
        for i, val in enumerate(arr):
            # Inside the loop, as long as the current element (val) is 
            # less than the element at the index stored at the top of the 
            # stack, we pop elements from the stack and perform calculations.
            while stack and val < arr[stack[-1]]:
                index = stack.pop()
                # left represents the distance from the current 
                # popped index to the previous index in the stack.
                left = index - stack[-1] 
                # right represents the distance from the current 
                # index to the current iteration index.
                right = i - index
                # The product (right * left * arr[index]) is added to res.
                res += (right * left *arr[index]) %MOD
            # add current index to stack
            stack.append(i)
        
        return res % MOD
