"""
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward 
jump from index i. In other words, if you are at nums[i], you can 
jump to any nums[i + j] where:

0 <= j <= nums[i] and i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The 
test cases are generated such that you can 
reach nums[n - 1].


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2

Explanation: The minimum number of jumps to reach the last 
index is 2. Jump 1 step from index 0 to 1, then 3 
steps to the last index.


Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 
Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].

Takeaway:

This is a wonderful question

Think about windows and how you can move and take steps

It is like a BFS on a 1D list

"""

class Solution:
    def jump(self, nums: list[int]) -> int:
        # we are guaranteed to reach the goal
        
        # the solution for this problem is kinda like a BFS
        # 2 , 3, 1 , 1 , 4
        # _ , ____ , _____
        
        # we basically have these parts that 
        # are reachable from previous parts
        # these levels will tell us how many steps 
        # we need to get to the next level
        
        # once we reach the destination, we are done
        
        res = 0
        # define the window at the starting element
        l = r = 0
        
        while r < len(nums) - 1:
            # find the new r which is based on farthest we can go
            farthest = 0
            for i in range(l, r + 1): # r inclusive
                farthest = max(farthest, i + nums[i])
            
            # new left is next to old right
            l = r + 1
            # right is farthest
            r = farthest
            # increment result
            res += 1
            
        return res