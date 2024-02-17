"""
Given an integer array nums sorted in non-decreasing 
order, return an array of the squares of each number 
sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: 
  After squaring, the array becomes [16,1,0,9,100].
  After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

  1 <= nums.length <= 104
  -104 <= nums[i] <= 104
  nums is sorted in non-decreasing order.

Takeaway:

Great one to optimize, think from two ends.

Follow up: Squaring each element and sorting the new array 
is very trivial, could you find an O(n) solution 
using a different approach?

"""

from heapq import heapify, heappop
from collections import deque

class Solution:
    def sortedSquares_(self, nums: List[int]) -> List[int]:
        # this just works
        
        res = []
        for elem in nums:
            res.append(elem ** 2)
        res.sort()
        return res

    def sortedSquares__(self, nums: List[int]) -> List[int]:
        # Another approach - still o(nlogn)
        res = []
        pos_nums = [abs(elem) for elem in nums]
        heapify(pos_nums)
        while pos_nums:
            res.append((heappop(pos_nums)) ** 2)
            
        return res
        
    def sortedSquares___(self, A: List[int]) -> List[int]:
        # using two pointers
        # o(n) time complexity
        
        result = [0] * len(A)
        # we will start writing from the end
        write_pointer = len(A) - 1
        left_read_pointer, right_read_pointer = 0, len(A) - 1

        left_square = A[left_read_pointer] ** 2
        right_square = A[right_read_pointer] ** 2
        
        while write_pointer >= 0:
            if left_square > right_square:
                # left side is bigger
                result[write_pointer] = left_square
                left_read_pointer += 1
                # calculate at new index
                left_square = A[left_read_pointer] ** 2
            else:
                result[write_pointer] = right_square
                right_read_pointer -= 1
                # calculate at new index
                right_square = A[right_read_pointer] ** 2
            # decrease after each write
            write_pointer -= 1
        return result
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        # we can use a deque too
        number_deque = deque(A)
        reverse_sorted_squares = []
        while number_deque:
            left_square = number_deque[0] ** 2
            right_square = number_deque[-1] ** 2
            if left_square > right_square:
                reverse_sorted_squares.append(left_square)
                number_deque.popleft()
            else:
                reverse_sorted_squares.append(right_square)
                number_deque.pop()
        return reverse_sorted_squares[::-1]
