"""
Given an unsorted array of integers nums, return the length of the 
longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].

         Therefore its length is 4.
     
Example 2:

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
 

Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

Takeaway:

    To get rid of reapparent values, you can use a set,

    Imply defining the question in ENGLISH is the first step.

    you can override a value in an iteration with 

        current = max(current, new)

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # o(n) means no sorting
        
        # we are interested in unique elements
        nums_set = set(nums)

        # we are only interested in longest streak
        longest_streak = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                # a new streak starts
                current_num = num
                current_streak = 1
                
                while current_num + 1 in nums_set:
                    # streak continues
                    current_num += 1
                    current_streak +=1

                # update the longest streak         
                longest_streak = max(current_streak, 
                                        longest_streak)
                
        return longest_streak

sol = Solution()

print(sol.longestConsecutive(nums = [100,4,200,1,3,2])) # 4
print(sol.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1])) # 9
