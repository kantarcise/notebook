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

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where
 n is the array's size.


Takeaway:

USE COLLECTIONS. A library that is written by competent 
people is way better your weird approach.

COunter has most_common method.

    List the n most common elements and their counts from the most 
    common to the least. If n is None, then list all element counts.


"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        
        #  we need a data structure that holds certain keys and values
        # the keys can be occurances of elements
        # we willl access the result with a simple getitem

        count = {}

        freq = [[] for i in range(len(nums) +1 )]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def top_k_frequent(self, nums, k):
        
        counts = Counter(nums)
        
        most_frequent = counts.most_common(k)

        return [elem[0] for index, elem in enumerate(most_frequent)]
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.top_k_frequent([1,1,1,2,2,3], 2))
