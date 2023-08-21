"""
Given two strings s and t, return true if t is an
 anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters
 of a different word or phrase, typically using all the original 
 letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

from collections import Counter


class Solution:
    # my first solution
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {character: s.count(character)  for character in set(s)} # o(n^2)
        dict_2 = {character: t.count(character)  for character in set(t)} # o(n^2)
        return dict_1 == dict_2

    # second solution - way better for bigger sized strings\

    # A faster solution is to use the collections.Counter() function
    # from the Python standard library. The Counter() function takes a
    #  sequence as input and returns a dictionary that maps each
    #  element in the sequence to its frequency.
    def isAnagram(self, s: str, t: str) -> bool:
        counter_1 = Counter(s) # o(n)
        counter_2 = Counter(t) # o(n)
        return counter_1 == counter_2

    # third solution - get dirty - o(n) time complexity
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False

        # single dict 
        char_count = {}
        for char in s:
            # if it already exists, add 1 to value
            char_count[char] = char_count.get(char, 0 ) + 1

        for char in t:
            # if t has a different character
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]

        # expecting an empty dict in the end
        return not char_count


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram("anagram","nagaram"))