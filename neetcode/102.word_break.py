"""
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused 
multiple times in the segmentation.

Example 1:

    Input: s = "leetcode", wordDict = ["leet","code"]
    
    Output: true
    
    Explanation: 
        Return true because "leetcode" can be segmented as "leet code".

Example 2:

    Input: s = "applepenapple", wordDict = ["apple","pen"]
    
    Output: true
    
    Explanation: 
        
        Return true because "applepenapple" can be 
            segmented as "apple pen apple".
        
        Note that you are allowed to reuse a dictionary word.

Example 3:

    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    
    Output: false
    
Constraints:

    1 <= s.length <= 300
    
    1 <= wordDict.length <= 1000
    
    1 <= wordDict[i].length <= 20
    
    s and wordDict[i] consist of only lowercase English letters.
    
    All the strings of wordDict are unique.

Takeaway:

    We can make  decision tree and the dp cache will 
    be starting from the end

    Nothing fancy, just need to understand dp

"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # start from words in dict 
        # if we find a match, check the remaining, the same
        
        # the cache will be a 1D list
        # we will end when we meet the end of s
        dp = [False] * (len(s) + 1)
        
        # base case is True
        dp[len(s)] = True
        
        
        # from the last index of the string, decrement until first character
        for i in range(len(s) - 1, -1, -1):
            # for each i we want to try if there is a word match
            for w in wordDict:
                # if there are enough characters and the word is matching
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # if index i is True, we can look at the next index
                if dp[i]:
                    break
        return dp[0]
