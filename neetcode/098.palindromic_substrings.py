"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

Takeaway:

There are ways to solve DP problems in single traversion.

a a a b

index = 0  - a

index = 1 - a AND a a a

"""

class Solution:
    def countSubstrings__(self, s: str) -> int:
        # brute force
        # check every combination
        # works but can be better
        # this is O(N^2)
        
        combs = []
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                combs.append(s[i:j]) 
        
        def palindrome(seq):
            if seq == "":
                return 0
            if seq == seq[::-1]:
                return 1
            return 0
        
        return list(map(palindrome, combs)).count(1)

    def countSubstrings(self, s: str) -> int:
        # neet
        count = 0
        for i in range(len(s)):
            # start from 0, check all indexes
            # and find palindromes, as indexes in their centers
            
            # for example 
            # a a a b
            # i = 0 a
            # i = 1 - "a" and "a a a"
            
            l, r = i, i
            # check out of bounds condition and character equality
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # move left and right pointers
                # in expansion direction
                l = l - 1
                r = r + 1
                # increment count
                count = count + 1
            
            l, r = i, i + 1
			# This loop takes Care of the even palindromes
            # check out of bounds condition and character equality
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # move left and right pointers 
                # in expansion direction
                l = l - 1
                r = r + 1
                # increment count
                count = count + 1   
                
        return count
    
    def countSubstrings_(self, s: str) -> int:
        
        n = len(s)
        # make a memoization list of lists
        dp = [[False] * n for _ in range(n)]
        print(dp)
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if i+1 >= j:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        
                if dp[i][j]:
                    ans += 1
        print(dp)        
        return ans