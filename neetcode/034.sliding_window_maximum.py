"""
You are given an array of integers nums, there is a
 sliding window of size k which is moving from the very left of the array
  to the very right. You can only see the k numbers in the window. 
  
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

Takeaway:

Pretty easy to solve in Exponential time

To solve it in linear time, we use deques

Both pointers can start from 0, right should be smaller than lenght of sequence.

For every window, append elements to the deque but pop 
all elements  if they are not bigger than current element

When you find the current max in the window, now you can update the left pointer

"""

from collections import deque

class Solution:
    
    # my first take
    # o(n^2) time complexity, not good.
    # time limit exceeded
    def maxSlidingWindow(self, nums, k):
        
        #  nums = [1,3,-1,-3,5,3,6,7]
        #  k = 3
        # Output: [3,3,5,5,6,7]

        result = []
        seq_length = len(nums) # 8

        for i in range(seq_length - k + 1):
            result.append(max(nums[i:i+k]))
        
        return result

    def max_sliding_window(self, nums, k):
        # can we make a linear time - o(n) solution

        # we do not need to make repeated work:
        # [1, 1, 1, 1, 1, 4, 5]   and k = 6
        # first window has the max 4
        # second window, we do NOT have to check all the 1s, we know they are not the max

        # we will use a deque (always decreasing)

        # for first window, we will add 1s first to deque
        # when we get 4, we will POP all the values smaller than 4
        # deque = [4]
        # when whole window is traversed, add deque element to the result

        # for second window, we will add 5 to deque,
        # 4 is no longer needed as it is already smaller than 5
        # deque = [5]
        # when whole window is traversed, add deque element to the result

        # adding and removing from deque is o(1) for n elements, o(n)

        output = []
        # two pointers
        l = r = 0 
        # This queue will contain indexes
        queue = deque()

        while r < len(nums):
            
            # make sure no smaller value exists in the queue
            # if there is an element in the queue and 
            # the top value in the queue (the rightmost value in the queue) is 
            # smaller than the value we are inserting
            while queue and nums[queue[-1]] < nums[r]:
                # just remove the smaller values
                queue.pop()

            # add the new element
            queue.append(r)

            # if leftmost value is out of bounds we have to remove it from the queue 
            if l > queue[0]:
                queue.popleft()

            # we have a window big enough, we can update the output
            if (r + 1) >= k:
                output.append(nums[queue[0]])
                # only increment left once the window is at least size k
                l += 1
            r += 1
        
        return output

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(sol.maxSlidingWindow(nums = [1], k = 1))

    print(sol.max_sliding_window(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(sol.max_sliding_window(nums = [1], k = 1))