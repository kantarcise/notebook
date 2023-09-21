"""

Given n non-negative integers representing an elevation map where the
 width of each bar is 1, compute how much water it can trap after
  raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
 are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


takeaway:

- two pointers are still doing wonders.

- trying to find a pattern for each step is the key for approaching these problems.

- you need to be calm. you will be calm when you solve your 250th question.

- just a numbers game

"""

class Solution:

    # first try
    def trap_(self, height):
        
        # to be able to trap water, we need at least 2 unit width and 1 unit height difference
        # lets iterate over all elements, try to get increasing and decreasing  windows
        total_water = 0
        window = []
        for index, elem in enumerate(height):
            if elem > height[index + 1] and index != 0:
                window.append(elem)
            elif elem < height[index + 1] and index != 0:
                window.append(elem)
                window.append(height[index + 1])
                area = len(window) * abs(window[0] - window[-1])
                total_water += area
                window.clear()

    def trap(self, height):
        # the amount of trapped water is determined by min( left_boundary, right_boundary)
        # but wait, there is more.
        # for each element in the sequence the formula actually is:

        # min (left_boundary, right_boundary) - height [i] for each i.
        # 
        # iterate over the array and calculate for each element max height on left and right
        # sequence: [ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        
        # min_left: [ 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
        # min_right:[ 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0]
        
        # min(l,r): [ 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]

        # this was o(n) space usage, we can do o(1) without using all of this memory:

        # WITH TWO POINTERS

        if not height: return 0 
        l, r = 0 , len(height) - 1

        left_max, right_max = height[l], height[r]

        res = 0

        # before they meet
        while l < r:
            if left_max < right_max:
                # move the left pointer and update left max
                l += 1
                # current element can be the new left max
                left_max = max(left_max, height[l])
                # substract the element at that index as it holds space instead of water
                res += left_max - height[l]
            else:
                # move the right pointer and update right max
                r -= 1
                # current element can be the new right max
                right_max = max(right_max, height[r])
                # substract the element at that index as it holds space instead of water
                res += right_max - height[r]

        return res




if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sol.trap([4,2,0,3,2,5]))