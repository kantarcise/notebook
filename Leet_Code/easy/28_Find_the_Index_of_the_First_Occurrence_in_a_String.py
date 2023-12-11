"""

Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Takeaway:

str.find("substring") is pretty

But if you can't, just match patterns:

if equal length slice is equal to needle

"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # honestly, skill issue if you dont know this
        # I do thank lord.
        return haystack.find(needle)
    
    def strStr(self, haystack: str, needle: str) -> int:
        # from 0 to end + 1
        for i in range(len(haystack)):
            # if equal length slice is equal to needle
            if haystack[i:i+len(needle)] == needle:
                # you got it!
                return i
        return -1
    
