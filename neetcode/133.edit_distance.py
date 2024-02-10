"""
Given two strings word1 and word2, return the minimum 
number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
 
Example 1:

Input: word1 = "horse", word2 = "ros"

Output: 3

Explanation: 
    
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"

Output: 5

Explanation: 
    
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')

Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.

Takeaway:

2D DP, using pointers within words

starting from example to find the grid relation is really cool

homie - from functools import cache ?

"""
from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # neet
        
        # analyze some simple cases

        #  case 1
        # ""
        # ""
        # both empty, we do not need to do anything
        # result is 0

        # case 2
        # "abc"
        # "abc"
        # same - we do not need to do anythin
        # result is 0


        # case 3
        # "abc"
        # ""        
        # if the word2 is empty, we just need to insert 
        # all characters from word1
        # result is len(word1)

        # case4
        # ""
        # "abc"
        # if the word1 is empty, we need insertion 
        # action of len(word2) times

        # brute force, we have two pointers.

        #          i
        # word1 = "abc"
        # word2 = "abc"
        #          j

        # if same, move on to the next pointer
        # if w1[i] == w2[j]:
        #     (i + 1, j + 1) - both incremented

        #          i
        # word1 = "abd"
        # word2 = "acd"
        #          j

        # if not same
        # else:
        #     insert() - we insert a "c" before "b" in word1
        #     the i pointer is still the same, j moved
        #     this is a single operation
        #     
        #     1 + (i, j + 1)

        #     delete() - we can delete the "b" from word1
        #     i moved next, but we still have not found a match for j

        #     1 + (i + 1, j)

        #     replace() - we can force them to match
        #       we can replace "b" in word1 we can change it to the "c"
        #       both pointers is going to increment
        
        #      1 + (i + 1, j + 1)
        
        
        # 2D DP solution: bottom up DP
        
        #              word2
        #            a  c  d  _  
        #          -------------
        #        a | x        3 |
        # word1  b |    y     2 |
        #        d |          1 |
        #        _ | 3  2  1  0 |
        #          -------------
        
        # we can have empty strings so we have "_"

        # bottom right - two empty strings - 0
        
        # top right - if word2 is empty, solution is len(word1)
        
        # bottom left - if word1 is empty, solution is len(word2)
        
        # x depends on y

        # at y, characters are not equal
        # so we need to look at, bottom, right and diagonal
        # which are insert, delete, replace

        # to find the value at x
        # we can start from bottom and fill our matrix

        # if charachers are different, look at 3 directions
        # find the min and ADD 1
        
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # initialize the base cases
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # now get to the actual strings
            
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                # same chars
                if word1[i] == word2[j]: 
                    cache[i][j] = cache[i + 1][j + 1]

                # check all 3 directions
                else:
                    cache[i][j] = 1 + min(cache[i+1][j],
                                          cache[i][j + 1],
                                          cache[i+1][j+1])
        
        return cache[0][0]
    
    def minDistance_(self, word1: str, word2: str) -> int:
        # from a homie - using functools cache
        l1, l2 = len(word1), len(word2)

        @cache
        def dfs(p1, p2):
            if p2 == l2:
                return l1 - p1
            if p1 == l1:
                return l2 - p2

            ret = 0
            if word1[p1] == word2[p2]:
                ret = dfs(p1+1, p2+1)
            else:
                insert = dfs(p1, p2+1)
                delete = dfs(p1+1, p2)
                replace = dfs(p1+1, p2+1)
                ret = min(insert, delete, replace) + 1
            return ret
        
        return dfs(0, 0)