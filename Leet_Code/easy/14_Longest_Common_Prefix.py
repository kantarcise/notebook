"""
Write a function to find the longest common 
prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: strs = ["flower","flow","flight"]
    
    Output: "fl"

Example 2:

    Input: strs = ["dog","racecar","car"]
    
    Output: ""
    
    Explanation: 
    
        There is no common prefix among the input strings.

Constraints:

    1 <= strs.length <= 200
    
    0 <= strs[i].length <= 200
    
    strs[i] consists of only lowercase English letters.


Takeaway:

    lists instead of strings.

    zip([hello, dog, cat]) -> [(h, d, c), (e, o ,g)

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # we should use lists instead of concataneting strings.
        result = []

        # we are bottlenecked with the shortest string
        for i in range(len(min(strs))):
            # the first character
            c = strs[0][i]
            # If the first character is the same in all strings:
            if all(a[i] == c for a in strs):
                result.append(c)
            else:
                break

        return "".join(result)

    def longestCommonPrefix_(self, strs: list[str]) -> str:
        # we can use zip too!
        # this might be the fastest
        res = ""
        for a in zip(*strs):
            # this zips all input in a single indexed element
            # zip([hello, dog, cat]) -> [(h, d, c), (e, o ,g) ...]
            if len(set(a)) == 1: 
                res += a[0]
            else: 
                return res
        return res

    def longestCommonPrefix__(self, strs: list[str]) -> str:
        # another approach
        res = ""

        # this could be not the shortest
        # but we will deal with it later
        for i in range(len(strs[0])):
            for s in strs:
                # index is out of bounds
                # or
                # character not matching
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res

sol = Solution()
print(sol.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(sol.longestCommonPrefix(strs = ["dog","racecar","car"]))
print(sol.longestCommonPrefix(strs = ["plow", "flower", "flight"]))
print(sol.longestCommonPrefix(strs = ["grow", "grown", "growth"]))

print()

print(sol.longestCommonPrefix_(strs = ["flower","flow","flight"]))
print(sol.longestCommonPrefix_(strs = ["dog","racecar","car"]))
print(sol.longestCommonPrefix_(strs = ["plow", "flower", "flight"]))
print(sol.longestCommonPrefix_(strs = ["grow", "grown", "growth"]))

print()

print(sol.longestCommonPrefix__(strs = ["flower","flow","flight"]))
print(sol.longestCommonPrefix__(strs = ["dog","racecar","car"]))
print(sol.longestCommonPrefix__(strs = ["plow", "flower", "flight"]))
print(sol.longestCommonPrefix__(strs = ["grow", "grown", "growth"]))