"""
Given an array of integers arr and an integer k. 

Find the least number of unique integers 
after removing  exactly k elements.

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the 
    two 1s or three 3s. 1 and 3 will be left.
 
Constraints:

  1 <= arr.length <= 10^5
  1 <= arr[i] <= 10^9
  0 <= k <= arr.length

Takeaway:

  Counter is great!

  most_common is a list of tuples.
"""
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        # we will remove k elements
        # we way almost all same items
        c = Counter(arr)
        # counter is great 
        commons = c.most_common()
        common_list = [list(elem) for elem in commons]
        
        for _ in range(k):
            if common_list[-1][-1] == 1:
                del c[common_list[-1][0]]
                del common_list[-1]
            else:
                c[common_list[-1][0]] -= 1
                common_list[-1][-1] -= 1
                
        return len(set(c.keys()))
