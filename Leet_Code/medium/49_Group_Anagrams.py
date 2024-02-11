"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all 
the original letters exactly once.

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

If you need an immutable for the key, use a 
frozenset or a string!

Tuple might not work because ordering is important in a tuple.

"""

from collections import Counter
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        
        # - Get all character freqs using 'Counter';
        # - we need to use them as keys for all anagrams
        # - let's use 'frozenset'

        for s in strs:
            # dict_items([('e', 1), ('a', 1), ('t', 1)])
            # print(Counter(s).items())
            # print(frozenset(Counter(s).items()))
            # frozenset({('t', 1), ('e', 1), ('a', 1)})
            
            groups[frozenset(Counter(s).items())].append(s)
        
        return groups.values()
            
    def groupAnagrams__(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list)

        for word in strs:
            # we need an immutable for the key
            key = tuple(sorted(word))
            # we will use all the values of this dict
            group[key].append(word)
        
        return list(group.values())
    
    def groupAnagrams_(self, strs: List[str]) -> List[List[str]]:
        am=defaultdict(list)
        for w in strs:
            # make the word sorted
            sw="".join(sorted(w))
            # just use it as a key
            am[sw].append(w)
        return(am.values())
