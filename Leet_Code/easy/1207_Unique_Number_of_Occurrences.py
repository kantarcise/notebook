"""
Given an array of integers arr, return true if the number of 
occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]

Output: true
 
Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

Takeaway:

Counter is pretty cool. You know the methods:

c.items(), c.values(), c,keys()

Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

c = Counter(a=10, b=5, c=0)
c.total()

"""
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return True if len(c.values()) == len(set(c.values())) else False
