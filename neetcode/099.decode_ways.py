"""

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back 
into letters using the reverse of the mapping above (there may 
be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 
Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

Takeaway:

bottom up approach is really cool. 

Understand the question. Do not rush into writing code.

"""

class Solution:
    def numDecodings_(self, s: str) -> int:
        # for double selection. char should be 1 or 2
        # otherwise single selections.
        # print(chr(65))
        # print(chr(90))   

        # "11106"
        # we cannot just start with 0 - return 0 
        # if 1 or 2 we can select single or double
        # actually if we have a 2 we can only go to 6 max 
        # at every decision we have o(1) selection
        # either take 1 character and solve for remaining
        # or take 2 characters solve for remaining 
        
        
        # two later results will give us current one
        # dp[i] = dp[i + 1] + dp [i + 2]
        
        dp = {len(s) : 1}
        
        def dfs(i):
            """i is the position where we are in s"""
            # base case 1
            if i in dp:
                # already been cached
                # or i is the last position in our string
                return dp[i]
            # base case 2
            if s[i] == "0":
                # if it is starting with 0
                # that is invalid
                return 0
            
            # number is between 1 - 9
            res = dfs(i+1)
            
            # the i + 2 case
            # if we have a second character after current one
            # and it is in 10-19 or 20-26 range
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
                
            # cache the result    
            dp[i] = res
            return res
        return dfs(0)
            
    def numDecodings(self, s: str) -> int:
        
        dp = {len(s): 1}
        
        # bottom up - iterate in reverse order
        for i in range(len(s) - 1, -1, -1):
            if s[i] ==  "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
                
        return dp[0]