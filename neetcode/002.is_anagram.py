"""
Given two strings s and t, return true if t is an
anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using 
all the original letters exactly once.
 
Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false
 
Constraints:

    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

Takeaway:

    Counter is just made for the job!
"""

from collections import Counter

class Solution:

    def isAnagram__(self, s: str, t: str) -> bool:
        # my first solution - brute force
        dict_1 = {character: s.count(character)  for character in set(s)} # o(n^2)
        dict_2 = {character: t.count(character)  for character in set(t)} # o(n^2)
        return dict_1 == dict_2
    
    def isAnagram_(self, s: str, t: str) -> bool:
        # second solution - way better for bigger sized strings\
        return Counter(s) == Counter(t)  

    def isAnagram___(self, s: str, t: str) -> bool:
        # adding elements and comparing the dicts would work
        map_1, map_2 = {}, {}

        for elem in s:
            map_1[elem] = map_1.get(elem, 0) + 1

        for elem in t:
            map_2[elem] = map_2.get(elem, 0) + 1

        return map_1 == map_2

    def isAnagram(self, s:str, t:str) -> bool:
        # even faster one
        # o(n) time complexity

        if len(s) != len(t):
            return False

        # let's use only a single dict 
        char_count = {}
        for char in s:
            # if it already exists, add 1 to value
            char_count[char] = char_count.get(char, 0 ) + 1

        for char in t:
            # if t has a different character
            if char not in char_count:
                return False
            char_count[char] -= 1

            # if we expire ther count of a character
            if char_count[char] == 0:
                del char_count[char]

        # expecting an empty dict in the end
        return not char_count

sol = Solution()
print(sol.isAnagram(s = "rat", t  = "car")) # False
print(sol.isAnagram(s = "anagram", t  = "nagaram")) # True

print(sol.isAnagramMap(s = "rat", t  = "car")) # False
print(sol.isAnagramMap(s = "anagram", t  = "nagaram")) # True
