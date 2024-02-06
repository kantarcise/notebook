"""
Given strings s1, s2, and s3, find whether s3 is formed 
by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration 
where s and t are divided into n and m 
substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1

The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... 
                    
                    or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Explanation: One way to obtain s3 is:
    Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
    
    Interleaving the two splits, we 
            get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
    
    Since s3 can be obtained by interleaving s1 and s2, we return true.


Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Explanation: Notice how it is impossible to interleave 
    s2 with any other string to obtain s3.

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 
Constraints:

    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

Takeaway:

Both memoization and bottom up will work.

Simply understand the decision tree, which is based on
indexes of two strings, to try to result in s3. 

We are usually making out of bounds within the grid,
just to have a simpler calculation.

"""
class Solution:
    def isInterleave_(self, s1: str, s2: str, s3: str) -> bool:
        # memoization solution        
        
        # relative order is maintained.
        # we an split the strings in any way we want
        
        # s3 start character,
        # one of them has to start with the 
        # same character in s1 or s2
        
        # two pointers on s1 and s2, added to make s3's pointer
        
        # decision Tree !
        
        # s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        
        # indices of strings:
        
        #                0, 0
        #          1, 0            start with s1 
        #      2,0                 continue s1
        #           2,1            continue s2
        #       3,1     2,2        both s1 and s2 is possible!
        # 
        # 
        
        # for any particular subproblem, we will store True/False
        
        # if we just find a single True, we can just return True
        
        dp = {}

        # length base case.
        if len(s1) + len(s2) != len(s3):
            return False
        
        # k = i + j
        def dfs(i, j):
            
            # if i or j is out of bounds
            if i == len(s1) and j == len(s2):
                return True
            
            # already computed
            if (i, j) in dp:
                return dp[(i, j)]
            
            # i is inbounds, character in s1 match the s3[i+j]
            # increment i and recur
            if i < len(s1) and s1[i] == s3[i+j] and dfs(i+1, j):
                return True
            
            # j is inbounds, character in s2 match the s3[i+j]
            # increment j and call again
            if j < len(s2) and s2[j] == s3[i+j] and dfs(i, j+1):
                return True
            # if neither of those are True, set it False
            dp[(i, j)] = False
            
            return False
        
        # starting at the beginning of the strings, call dfs
        return dfs(0, 0)
               
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # bottom up solution    
        
        # relative order is maintained.
        # we an split the strings in any way we want
        
        # s3 start character,
        # one of them has to start with the 
        # same character in s1 or s2
        
        # two pointers on s1 and s2, added to make s3's pointer
        
        # s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        
        # we will use a matrix, WITH out of bounds
        
        # 
        #    d  b  b  c  a   
        #   --------------
        #  a|                 |
        #  a|                 |
        #  b|      X          |
        #  c|                 |
        #  c|               T |
        #   |         F  F  T |
        
        
        # Two empty strings will make the base case for True (T)
        # which is out of bounds!

        # F because we cannot end with an "a" (s2)
       
        # F because we cannot end with an "ca" (s2)
        
        # T because we can end with a "c" (s1)
        
        # for "bb" cell {X}, we will look to the right and down
        # if both are True, the cell is True
        # if either are True, the cell is True
        
        # if we used the b in (s1)
        # we are looking at the bottom position because
        # we possibly used the current character and need 
        # to check remaining 
        
        # if we used the b in (s2)
        # we are looking at the right position 
        # because that's what remains
        
        # we will calculate every single cell in this matrix
        # even the out of bounds ones.
        
        # edge case
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        dp[len(s1)][len(s2)] = True
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1 , -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]