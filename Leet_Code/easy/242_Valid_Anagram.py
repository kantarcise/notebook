"""
Given two strings s and t, return true if t is an anagram 
of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all 
the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Takeaway:

collections Counter is wonderful. Hashmaps work too.

"""

class Solution:
    def isAnagram_(self, s: str, t: str) -> bool:
        def make_map(s):
            map = {}
            for elem in s:
                if elem not in map:
                    map[elem] = 1 + map.get(elem, 0)
                else:
                    map[elem] +=1
            return map
        return make_map(s) == make_map(t)
    
    def isAnagram(self, s: str, t: str) -> bool:
        # we can use a map to compare the strings.
        from collections import Counter
        
        return Counter(s) == Counter(t)

