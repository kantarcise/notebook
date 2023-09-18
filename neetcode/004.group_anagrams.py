"""
Given an array of strings strs, group the anagrams together. You can 
return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters
 of a different word or phrase, typically using 
 all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


Takeaway:

We can use a dictionary to keep key value relationships 
between sequence elements and their Counters

We can sort all elements in sequence to unify the frequency of characters

if not seen before in the dictionary, we can initialize an empty list
later to append on it.

"""

from collections import Counter , defaultdict

class Solution:
    def group_anagrams(self, strs):
        # We use a dictionary to store anagram groups. The keys will be the sorted strings,
        # and the values will be lists of strings that are anagrams of each other.
        strs_table = {}

        for string in strs:
            # to equalize all strings in the sequence
            sorted_string = ''.join(sorted(string))

            # not seen before
            if sorted_string not in strs_table:
                # make an empty list so we can append this key
                strs_table[sorted_string] = []

            # already known
            strs_table[sorted_string].append(string)

        return list(strs_table.values())

    def another_group_anagrams(self, strs):
        
        groups = defaultdict(list)
        
        # - we obtain frequencies of all characters using 'Counter';
        # - these frequencies are used as a key for hashmap/dict;
        # - to uniquely identify groups, we use 'frozenset'
        #   (note that 'set' is mutable, thus, can't be used as key)
        for s in strs:
            groups[frozenset(Counter(s).items())].append(s)
        
        return groups.values()

if __name__ == "__main__":
    sol = Solution()
    print(sol.group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(sol.group_anagrams([""]))
    print(sol.group_anagrams(["a"]))
