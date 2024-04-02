"""
Given an array of integers heights representing the 
histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:

    |            __         |
    |         __|  |        |
    |        |     |        |
    |        |     |   __   |
    |   __   |     |__|  |  |
    |  |  |__|           |  |
    |__|                 |__|

    Input: heights = [2,1,5,6,2,3]
    Output: 10
    
    Explanation: The above is a histogram where 
        width of each bar is 1.
        The largest rectangle is shown in the red area, 
        which has an area = 10 units.

Example 2:

    Input: heights = [2,4]
    Output: 4


Takeaway:

    What is the limiter case? If there is a smaller rectangle 
        limiting the rectangle to extend beyond -> We cannot grow more.
    
    We can hold index - height pairs in a stack.

    When the current height is smaller than the height at the top 
        of the stack (i.e., stack[-1][1] > h), we can just calculate
        maximum area found so far.
    
    For each popped element from stack, we will calculate
        the (possibly) maximum area.

"""

class Solution:

    def largestRectangleArea(self, heights: list[int]) -> int:
        
        # we should focus on increasing heights, because a decrease will 
        # limit the rectangle
        
        # [2, 1, 5, 6, 2, 3]
        # lets use a stack with index - height pairs
        # also keep the max area so far.


        #                                      stack 
        #  index                                             height
        #    0                                               2 (popped when get to 1 at [1])  
        #    0 (not i 1 because we can extend the i to 0)    1 (not popped  until the end)   
        #    2                                               5 (popped when get to 2 at [4])
        #    3                                               6 (popped when get to 2 at [4])
        #    2 (not i 4 because we can extend the i to 2)    2 (not popped  until the end) 
        #    5                                               3 (not popped  until the end) 
        # 

        # max area

        # 2
        # 6
        # 10
        # 3 (from last element, not max)
        # 8 (from i 2 not max)
        # 6 (from i 1, not max)

        #  keep track of the maximum area of the rectangle found so far
        max_area = 0

        # stack will be used to keep track of pairs (index, height)
        #  as we traverse through the heights list.
        stack = [] 

        for i, h in enumerate(heights):
            
            # start at current index
            start = i

            # we want stack to be not empty to make our calculation
            # AND
            # check if the height of the last element in the stack
            #  (stack[-1][1]) is greater than the current height h.
            while stack and stack[-1][1] > h:
                #  We want to pop those previous elements from the stack 
                # and calculate the area of the rectangles formed by them.
                index, height = stack.pop()
                # update max area
                # the area of the rectangle formed by that element, which is given 
                # by height * (i - index), where i is the current index
                max_area = max(max_area, height * (i - index))
                # update the start index to be the index 
                start = index
            # This pair represents a rectangle in the histogram.
            # start might change in the loop
            stack.append((start, h))

        #  after processing all elements in the heights list, we iterate 
        # through any remaining elements in the stack.
        for i, h in stack:
            # update max_area if the current area is greater.
            max_area = max(max_area, h * (len(heights) - i))

        return max_area


if  __name__ == '__main__':

    sol = Solution()

    print(sol.largestRectangleArea([2,1,5,6,2,3]))
    print(sol.largestRectangleArea([2,4]))
