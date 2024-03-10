"""
Given two integer arrays nums1 and nums2, return an array 
of their intersection. Each element in the result must 
appear as many times as it shows in both arrays and 
you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 
Constraints:

  1 <= nums1.length, nums2.length <= 1000
  0 <= nums1[i], nums2[i] <= 1000

Follow up:

  1) What if the given array is already sorted? 
      How would you optimize your algorithm?
  2) What if nums1's size is small compared to 
      nums2's size? Which algorithm is better?
  3) What if elements of nums2 are stored on disk, and 
      the memory is limited such that you cannot 
      load all elements into the memory at once?

Follow-up 1: 

If the arrays are already sorted, we can use a two-pointer 
approach to find the intersection. We can iterate through 
both arrays simultaneously with two pointers, incrementing 
the pointer for the smaller value at each step. If 
we find a match, we add it to the result and move 
both pointers forward. This approach has a time complexity 
of O(n + m), where n and m are the lengths of the two arrays.

```     result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
```

Follow-up 2: 

?

Follow-up 3: 

If the elements of nums2 are stored on disk, we can read 
chunks of nums2 into memory, and then use a merge-like 
algorithm to find the intersection with nums1. 
So we avoid the need to load all elements 
into memory at once.

Takeaway:

  Both dicts and Counter will work.

"""

from collections import Counter

class Solution:
    def intersect_(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dictionary solution
        map_1 , map_2 = {}, {}
        for elem in nums1:
            map_1[elem] = map_1.get(elem, 0) + 1
        for elem in nums2:
            map_2[elem] = map_2.get(elem, 0) + 1
            
        intersection_keys = list(set(map_1) & set(map_2))
        result = []
        for k in intersection_keys:
            result.extend([k] * min(map_1[k], map_2[k]))
            
        return result
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # solution with counters
        result = []
        # make counters
        counter1, counter2 = Counter(nums1), Counter(nums2)

        # based on the keys of one Counter
        for key in counter1.keys():
            if key in counter2:
                # extend the result with min occurance
                result.extend([key] * min(counter1[key], counter2[key]))
        
        return result
