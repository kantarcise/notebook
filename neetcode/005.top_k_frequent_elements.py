"""
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:

    Input: nums = [1], k = 1
    Output: [1]
 
Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^ 4
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better 
than O(n log n), where n is the array's size.

Takeaway:

    USE COLLECTIONS. A library that is written by competent 
    people is way better your weird approaches.

    COunter has most_common method.

    List the n most common elements and their counts from the most 
    common to the least. If n is None, then list all element counts.

"""

from collections import Counter
from heapq import nlargest

class Solution:
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # we can use Counters with most_common
        c = Counter(nums)
        return [elem[0] for elem in c.most_common(k)]


    def topKFrequent_(self, nums: list[int], k: int) -> list[int]:
        # or we can take the heap route just to use, nlargest

        # edge case 
        if k == len(nums):
            return nums

        c = Counter(nums)
        
        return nlargest(k, c.keys(), key = c.get)


sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent(nums = [1], k = 1))

print(sol.topKFrequent_(nums = [1,1,1,2,2,3], k = 2))
print(sol.topKFrequent_(nums = [1], k = 1))
