"""
Given a string s, return the longest palindromic substring in s.

Example 1:

    Input: s = "babad"
    
    Output: "bab"
    
    Explanation: "aba" is also a valid answer.

Example 2:

    Input: s = "cbbd"

    Output: "bb"

Constraints:

    1 <= s.length <= 1000
    
    s consist of only digits and English letters.

Takeaway:

    One liners are generally great dynamic programming questions
    
    you can check if palindrome by starting from middle
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # one liners are generally really good dynamic programming questions

        # for checking if a substring is a palindrome:
        # you can either traverse the string
        # or you can start from middle and expand outwards
        
        res = ""
        res_len = 0
        
        for i in range(len(s)):
            # odd length - "aba"
            l, r = i, i
            # pointers are inbound and values are equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    # update values
                    res = s[l:r+1]
                    res_len = r - l + 1
                # move pointers
                l -= 1
                r += 1
                
            # even length - "cbbc"
            l, r  = i, i + 1
            # pointers inbound and characters equal
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    # update result
                    res = s[l:r+1]
                    res_len = r - l + 1
                # update pointers
                l -= 1
                r += 1
        return res
    
    def longestPalindrome_(self, s: str) -> str:
        # from a homie
        
        # fast solution
        if s == s[::-1]:
            return s
        # smallest size is 1
        size = 1
        # start from beginning
        start = 0
        
        for i in range(1, len(s)):
            # define pointers
            left = i - size
            right = i + 1
            
            # two substrings - odd and even
            big = s[left - 1:right]
            lil = s[left:right]
            
            if big == big[::-1] and len(big) > size:
                # found an even palindrome substring bigger than size
                size += 2
                start = left - 1
            elif lil == lil[::-1] and len(lil) > size:
                # found an odd palindrome substring bigger than size
                size += 1
                start = left
        
        # return biggest substring
        return s[start:start+size]
