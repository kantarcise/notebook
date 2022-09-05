# 14. Longest Common Prefix
# Easy
# 
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# 14. Longest Common Prefix
# Easy
# 
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".

# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=""
        # No common Prefix
        if len(strs)==0: 
            return answer
        # Common Prefix cannot be longer than the shortest string
        for i in range(len(min(strs))):
            # the first character
            c=strs[0][i]
            # If the first character is the same in all strings:
            if all(a[i]==c for a in strs):
                answer+=c
            else:
                break
        return answer
