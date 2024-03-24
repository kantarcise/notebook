"""

Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return 
this repeated number.

You must solve the problem without modifying the 
array nums and uses only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

Constraints:

  1 <= n <= 10^5
  nums.length == n + 1
  1 <= nums[i] <= n
  All the integers in nums appear only once except for precisely
    one integer which appears two or more times.

Follow up:

  How can we prove that at least one duplicate 
    number must exist in nums?
  Can you solve the problem in linear runtime complexity?

Takeaway: 

  Counter, dict, set are cool. Gotta use Floyd

"""
from collections import Counter

class Solution:
    def findDuplicate_(self, nums: List[int]) -> int:
        # this works but not constant space
        c = Counter(nums)
        return c.most_common(1)[0][0]
    
    def findDuplicate__(self, nums: List[int]) -> int:
        # another way would be just to use a set
        # still not constant space
        
        seen = set()
        for num in nums:
            if num in seen:
                return num

            seen.add(num)
            
    def findDuplicate(self, nums: List[int]) -> int:
        
        # we can use tortoise - hare 
        
        # how?
        # we can think of this nums list's elements as
        # pointers to other indexes:
        
        # [1,3,4,2,2]
        # all elements are pointing to somewhere in range [2, n]
        # noone is pointing to element 1 because the 
        # value cannot be 0 (index 0)
        
        # so in that case, this is a linked list and it has cycles in it!
        
        slow, fast = 0, 0

        # find the duplicate!
        while True:
            # move slow once
            slow = nums[slow]
            # move fast twice
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        
        # slow starts over
        # the meeting point from start and the intersection
        # will have equal distances.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
