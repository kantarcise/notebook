"""
In a string s of lowercase letters, these letters 
form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the 
groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where 
start and end denote the start and end indices (inclusive) 
of the group. In the above example, "xxxx" has the 
interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in 
increasing order by start index.

Example 1:

    Input: s = "abbxxxxzzy"

    Output: [[3,6]]

    Explanation: 
    
        "xxxx" is the only large group with start 
            index 3 and end index 6.

Example 2:

    Input: s = "abc"

    Output: []

    Explanation: 
        
        We have groups "a", "b", and "c", none of 
          which are large groups.

Example 3:

    Input: s = "abcdddeeeeaabbbcd"

    Output: [[3,5],[6,9],[12,14]]

    Explanation: 
    
        The large groups are "ddd", "eeee", and "bbb".
 
Constraints:

    1 <= s.length <= 1000
    
    s contains lowercase English letters only.

Takeaway:

    slightly favoring while loops for sliding windows

"""

class Solution:
    def largeGroupPositions_(self, s: str) -> List[List[int]]:
        # this works
        # for loop solution for a sliding window
        res = []
        char = s[0]
        start = 0
    
        for end, c in enumerate(s):
            if c != char:
                # if large group
                if end - start > 2:
                    res.append([start, end - 1])
                # update to latest character in s
                char = c
                # move start
                start = end
        
        # check the last window in the end
        if end - start + 1 > 2:
            res.append([start, end])
        
        return res
                
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        # this works
        # even better!
        # while loop for a sliding window
        res = []
        l, r = 0, 1
        
        # until end of string
        while r <= len(s):
            # if we are at the end or
            # characters do not match
            if r == len(s) or s[l] != s[r]:
                if r - l >= 3:
                    # large group
                    res.append([l, r - 1])
                # move start 
                l = r
            # move end by default
            r += 1
        return res
