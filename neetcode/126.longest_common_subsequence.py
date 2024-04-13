"""
Given two strings text1 and text2, return the length of 
their longest common subsequence. 

If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from 
the original string with some characters (can be none) 
deleted without changing the relative order of the 
remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is 
common to both strings.

Example 1:

    Input: text1 = "abcde", text2 = "ace" 
    
    Output: 3  
    
    Explanation: 
        The longest common subsequence is "ace" and its length is 3.

Example 2:

    Input: text1 = "abc", text2 = "abc"
    
    Output: 3

    Explanation: 
        The longest common subsequence is "abc" and its length is 3.

Example 3:

    Input: text1 = "abc", text2 = "def"
    
    Output: 0

    Explanation: 
        There is no such common subsequence, so the result is 0.
 
Constraints:

    1 <= text1.length, text2.length <= 1000
    
    text1 and text2 consist of only lowercase English characters.

Takeaway:

    If you can simply visualize the question, that can help immensely.

    Think about what we are looking for. 

    We are looking for an number as output. 

    We will use 2D DP to find the solution. Bottom up DP.

    Which will be filled with numbers.

"""
class Solution:

    def longestCommonSubsequence_(self, text1: str, text2: str) -> int:
        # works
        
        # Get the lengths of both input strings
        len_text1, len_text2 = len(text1), len(text2)
      
        # Initialize a 2D array (list of lists) 
        # with zeros for dynamic programming
        
        # The array has (len_text1 + 1) rows 
        # and (len_text2 + 1) columns
        dp_matrix = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]
        
        # We fill in the dp array from the bottom up using 
        # the following recurrence relation:
        
        # If characters at indices i-1 and j-1 match, 
        #       dp[i][j] = dp[i-1][j-1] + 1.
        #
        # If characters do not match, 
        #       dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
      
        # Loop through each character index of text1 and text2
        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                # If the characters match, take the diagonal value and add 1
                if text1[i - 1] == text2[j - 1]:
                    # The cell dp[i][j] represents the length of the 
                    # longest common subsequence of substrings 
                    # text1[0...i-1] and text2[0...j-1].
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                else:
                    # If the characters do not match, take the maximum of 
                    # the value from the left and above
                    dp_matrix[i][j] = max(dp_matrix[i - 1][j],
                                           dp_matrix[i][j - 1])
      
        # The bottom-right value in the matrix contains the 
        # length of the longest common subsequence
        return dp_matrix[len_text1][len_text2]
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # works, and fast
        
        # this is a really popular question
        
        # the key!
        
        # lets think about "abcde" and "ace"
        
        # if the starts of the strings match
        # which they do, 
        # we have a new problem with the remaining strings :smile:
        # "bcde" and "ce"
        
        # if they do not,
        # we can either look at "bcde" and "ace"
        # OR
        # "bcde" and "ce"
        
        # we will make a matrix
        
        #    a  c  e
        #  ----------
        # a| k       |0
        # b|    l  m |0
        # c|    n    |0
        # d|       p |0 
        # e|       r |0 
        #  ----------
        #    0  0  0
        
        # we will put value(int) in these cells
        
        # finding the value at [0, 0] (a and a)
        # requires [1, 1] (b and c)
        # which requires [1, 2] (b and e) and [2, 1] (c and c)
        
        # if characters match, we go diagonally
        
        # out of bounds is 0 because of empty string
        
        # in the matrix
        # from k to r , go down and right..
        
        # we will solve the problem in bottom up
        
        # starting from last row, we will go up 
        # until we find [0, 0] cell !
        
        # when characters do not match, look down and right
        # and take the max of it!
        
        matrix = [[0] * (len(text2) + 1)  for _ in range(len(text1) + 1)]
        
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1 , -1):
                if text2[j] == text1[i]:
                    matrix[i][j] = 1 + matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i][j+1], matrix[i+1][j])
                    
        return matrix[0][0]
