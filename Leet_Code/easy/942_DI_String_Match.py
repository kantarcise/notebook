"""
A permutation perm of n + 1 integers of all the integers in 
the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. 
If there are multiple valid permutations perm, return any of them.

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:

Input: s = "III"
Output: [0,1,2,3]

Example 3:

Input: s = "DDI"
Output: [3,2,0,1]

Constraints:

1 <= s.length <= 105
s[i] is either 'I' or 'D'.

Takeaway:

Taking a look at the examples and understanding the pattern is invaluable.

"""

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        # if we got an I we should start from 0
        # if we got an D we should start from len(s) + 1
        
        result = [0] * (len(s) + 1)
        left, right = 0, len(s)
        for i in range(len(s)):
            if s[i] == "I":
                result[i] = left
                left +=1
            else:
                result[i] = right
                right -=1
                
        # last elem - has to be the smaller one if possible
        result[-1] = left
        return result
        
