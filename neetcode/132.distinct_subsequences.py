"""
Given two strings s and t, return the number of distinct 
subsequences of s which equals t.

The test cases are generated so that the  answer fits on 
a 32-bit signed integer.

Example 1:

    Input: s = "rabbbit", t = "rabbit"

    Output: 3

    Explanation:

        As shown below, there are 3 ways you 
        can generate "rabbit" from s.

            rabbbit
            rabbbit
            rabbbit

Example 2:

    Input: s = "babgbag", t = "bag"
    
    Output: 5

    Explanation:

        As shown below, there are 5 ways 
        you can generate "bag" from s.
    
            babgbag
            babgbag
            babgbag
            babgbag
            babgbag
 

Constraints:

    1 <= s.length, t.length <= 1000
    
    s and t consist of English letters.

Takeaway:

    Simple DFS/ with caching

    the questions shrink as we solve them.

    think about what are the ways/paths we move forward as we 
    move in indexes of s and t

    the dragons get smaller as they are recognized.
"""

class Solution:
    def numDistinct_(self, s: str, t: str) -> int:
        # JUST THOUGHT process no solutions

        # use a decision tree
        # should I add the character or not?

        # order cannot change
        
        # the dp solution would be bottom up from the end.

        # target is t
        # s = "rabbbit", t = "rabbit"
        
        #                 ""
        #          0                     not 0
        #         "r"                    ""
        #     1       not 1        1           not 1 
        #    "ra"      "r"         "a"           ""
        #   2  not2    2  not2     XXXX        2  not2
        #  "rab" "ra"  "rb" "r"               "B"    ""    
        #                                     XX

        pass

    def numDistinct(self, s: str, t: str) -> int:
        # works
        
        # if first character match, we are looking for a different problem.
        
        # s = "rabbbit", t = "rabbit"

        # becomes

        # s = "abbbit", t = "abbit"

        # if s[i] == j[i]:
        #   i += 1
        #   j += 1

        # OR - pass the first "b" in s, keep j same
        # meaning do not use the current index in s to match
        # check for the other case
 
        #    i += 1
        #    j

        # if the characters do not match, we need to move in on s 

        # else:
        #    i +=1
        #    j

        # base cases
        # if t is empty, only single way to solve the problem
        # if s is empty, no way to solve

        # one optimization
        # we need enough elements in s to match to t

        cache = {}

        def dfs(i, j) -> int:

            # are there enough characters left in s to make t
            if len(s) - i < len(t) - j: 
                return 0

            # return the number of substrings from given indexes
            if j == len(t):
                # if j reached end of the string,
                # string t is empty
                return 1
            if i == len(s):
                # if we reached the end of string s
                # we cannot possibly match the string j anymore
                return 0
            
            # already computed
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]

        return dfs(0,0)
