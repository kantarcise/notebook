"""
You have a set of integers s, which originally contains all the 
numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s 
got duplicated to another number in the set, which results in repetition of one 
number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104

Takeaway:

Counter - List - Set

Sum of elements = n * n + 1 // 2

Pretty cool.
"""

from collections import Counter

class Solution:
    def findErrorNums_(self, nums: List[int]) -> List[int]:
        # first bad idea
        n = len(nums)
        normal_set = list(range(1, n+1))
        counter = Counter(nums) 
        return [max(counter, key = counter.get), list(set(normal_set) - set(nums))[0]]
    
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # we can use sum of elements and a single traverse
        s, n = set(nums), len(nums)
        for i in range (1,n+1):
            if i not in s:
                # found the missing
                t = i
                break
                
        # current sum
        s1 = sum(nums)
        # normal sum
        s2 = (n*(n+1))//2
        # difference
        d = s2 - s1
        
        return t - d, t
