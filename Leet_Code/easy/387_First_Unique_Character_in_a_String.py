"""
Given a string s, find the first non-repeating character 
in it and return its index. 

If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

Takeaway:

str.find returns -1 if not found

str.index returns ValueError.

Counter is wonderful.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # we have to traverse the string at least once
        counter = Counter(s)
        for c in s:
            if counter[c] == 1:
                # find returns -1
                # index returns ValueError
                return s.find(c) 
        return -1
