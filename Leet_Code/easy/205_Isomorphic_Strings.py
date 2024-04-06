"""
Given two strings s and t, determine if they 
are isomorphic.

Two strings s and t are isomorphic if the characters in 
s can be replaced to get t.

All occurrences of a character must be replaced with another 
character while preserving the order of characters. 

No two characters may map to the same character, but a 
character may map to itself.

Example 1:

    Input: s = "egg", t = "add"
    Output: true

Example 2:

    Input: s = "foo", t = "bar"
    Output: false

Example 3:

    Input: s = "paper", t = "title"
    Output: true
 
Constraints:

    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ascii character.

Takeaway:

    hashmaps, for mapping things.

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # I tried the ord approach with the difference 
        # between characters,
        # was not be able to make it work
        
        # here is the hash map solution
        
        # map all characters to each other, 
        s_map, t_map = {}, {}
        
        for i in range(len(s)):
            s_char , t_char = s[i], t[i]
            
            if s_char in s_map:
                if s_map[s_char] != t_char:
                    return False
            else:
                s_map[s_char] = t_char
                
            if t_char in t_map:
                if t_map[t_char] != s_char:
                    return False
            else:
                t_map[t_char] = s_char
        return True
    
    def isIsomorphic_(self, s: str, t: str) -> bool:
        # we can use a single dict for mapping elements
        # this is faster.
        
        hash_map = {}
        
        for i in range(len(s)):
            # get characters
            char1, char2 = s[i], t[i]
            
            if char1 not in hash_map:
                if char2 in list(hash_map.values()) :
                    # if char 1 is not encountered yet,
                    # char2 should not be in values
                    return False
                # set mapping
                hash_map[char1] = char2 
                continue
            
            if char2 == hash_map[char1] :
                # already mapped in reverse,
                # skip this index
                continue
            
            # if conditions does not hold
            # return False
            return False
        
        # print(hash_map)
        return True
