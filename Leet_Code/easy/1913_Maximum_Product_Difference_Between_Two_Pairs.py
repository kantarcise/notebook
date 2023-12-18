"""

The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that 
the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.

Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.

Constraints:

4 <= nums.length <= 104
1 <= nums[i] <= 10e4

Takeaway:

You can sort but sorting is n log n

instead you can finish the job in one traverse.
"""

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # how to get the max?
        # max + , min +
        
        biggest, second_biggest, smallest, almost_smallest =  1, 1, 10e4, 10e4
        for elem in nums:
            # big numbers
            if elem > biggest :
                second_biggest = biggest
                biggest = elem
            elif elem > second_biggest:
                second_biggest = elem
            if elem < smallest:
                almost_smallest = smallest
                smallest = elem
            elif elem < almost_smallest:
                almost_smallest = elem
        return (biggest * second_biggest) - (smallest * almost_smallest)

    
    def maxProductDifference_(self, nums):
        # from a homie
        # this is n log n
        # NO
        d = sorted((nums))
        return int(d[-1]*d[-2]) - int(d[0]*d[1])
    
    
    def maxProductDifference__(self, nums: List[int]) -> int:
        # one > two, the biggest two nums
        one, two = float('-inf'), float('-inf')
        # three > four, the smallest two nums
        three, four = float('+inf'), float('+inf')

        for num in nums:
            if num > one:
                two = one
                one = num
            elif num > two:
                two = num
            if num < four:
                three = four
                four = num
            elif num < three:
                three = num

        return one * two - three * four
