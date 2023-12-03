"""
Given an unsorted array of integers nums, return the length of 
the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

Takeaway:

Using a set is a great way for faster lookups.

A sequence starts when there is no smaller element in the collection.

you can keep the length of streak with checking the consequative numbers..

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)  # Convert the list to a set for faster lookup
        
        longest_streak = 0
        
        for num in nums_set:
            # Check if num is the start of a consecutive subsequence
            if num - 1 not in nums_set:
                # this is a sequence start
                current_num = num
                current_streak = 1

                # Find the length of the consecutive subsequence
                while current_num + 1 in nums_set:
                    # oh wait there is more
                    current_num += 1
                    current_streak += 1

                # there might be even bigger streaks in the list.
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
