"""
Given an integer array nums, return the third distinct maximum 
number in this array. 

If the third maximum does not exist, return the maximum number.

Example 1:

    Input: nums = [3,2,1]
    Output: 1

    Explanation:
      
        The first distinct maximum is 3.
        The second distinct maximum is 2.
        The third distinct maximum is 1.

Example 2:

    Input: nums = [1,2]
    Output: 2
    
    Explanation:
        
        The first distinct maximum is 2.
        The second distinct maximum is 1.
        The third distinct maximum does not exist, so the
            maximum (2) is returned instead.

Example 3:

    Input: nums = [2,2,3,1]
    Output: 1

    Explanation:
          
        The first distinct maximum is 3.
        
        The second distinct maximum is 2 (both 2's are 
            counted together since they have the same value).
        
        The third distinct maximum is 1.
 
Constraints:

    1 <= nums.length <= 104
    -2^31 <= nums[i] <= 2^31 - 1
 
Follow up: 

    Can you find an O(n) solution?

Takeaway:

    deque is a cool idea, but seems tough to implement.

    Only 3 possibilities really.

"""
class Solution:
    
    def thirdMax(self, nums):
        # tried deque approach, did not work
        # but it is cool that you can index 
        # with 0 and -1
        
        v = [float('-inf'), float('-inf'), float('-inf')]
        
        for num in nums:
            if num not in v:
                # basically 3 cases for an element to be
                if num > v[0]:
                    v = [num, v[0], v[1]]
                elif num > v[1]:
                    v = [v[0], num, v[1]]
                elif num > v[2]:
                    v = [v[0], v[1], num]
        
        return max(nums) if float('-inf') in v else v[2]
