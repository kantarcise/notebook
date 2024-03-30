"""
You are given an integer array height of length n. 

There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a 
container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:

    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49

    Explanation: The above vertical lines are represented
        by array [1,8,6,2,5,4,8,3,7]. In this case, the max area
        of water (blue section) the container can contain is 49.

Example 2:

    Input: height = [1,1]
    Output: 1


Constraints:

    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4

Takeaway:

    - Brute Force can help you find a pattern in which you can expand on.

    - Two pointers keep being the same, define them first and on condition
        increase/ decrease them.

"""
class Solution():

    def maxArea_(self, height):
        # brute force
        # this exceeds time limit
        result = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                result = max(result, area)
        
        return result
    
    def maxArea(self, height):
        # we need the highest towers in that are 
        # most apart from each other
        
        max_area = 0

        # because we want to maximize the area with 
        # biggest width if possible.
        l, r = 0, len(height) - 1

        while l < r: # basic condition for an area to exist.
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                # move the left pointer
                l += 1
            else:
                # move the right, because keeping left makes sense.
                r -= 1

        return max_area


sol = Solution()
print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))
print(sol.maxArea_(height = [1,8,6,2,5,4,8,3,7]))
