"""
Given an input string s and a pattern p, implement regular 
expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false

Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding 
        element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true

Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there 
        will be a previous valid character to match.

Takeaway:

DP questions start with a decision tree it seems.

After you find the brute force solution, you try to optimize it.


"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # "." can be anything
        # "*" zero or more of the preceeding elements
        
        # cover the entire input string 
        
        # if we have a "*" within the pattern,
        # we can either use the charter before 0 times
        # or infinite times
        
        # "a*" -> "", "a", "aa", "aaa", "aaaa", ...
        
        
        # lets try the bruteforce - decision tree
        
        # s = "aa", p = "a*"
        
        # left selection means we used star 1 time
        # right selection means we did not use the * 
        
        #         .
        #        / \ 
        #       a   ""
        #      / \
        # (S) aa  a
        #    / \
        #  aaa aa
        
        # when we are at (S), we will return True 
        # because pattern matches the string
        
        # every time we see a "*" 
        # we will have 2 different decisions
        
        # this will have a O(2^n) time complexitry
        # with caching, this can be improved to O(n*m)
        
        #  quick tangent
        
        # another example
        
        # s = "aab" p = "c*a*b"
        #      i         j
        
        # use the start or not use it
        
        #                   .
        #                 */ \- (j = j + 2)
        #                 c   ""
        # (i = i + 1, j = j) */  \- ( i = i , j = j + 2)
        #                    a   ""
        #                  */ \-
        #      (i=i+1,j=j)aa   ab
        #                /  \
        #              aaa   aa (i = i , j = j + 2)
        #        last element is b
        #                       \
        #                      aab (s[i]=p[i]) -> (i = i + 1, j = j + 1)
        
        # if  i >= len(s) & j >= len(p) 
        # we found a match!
        
        # if i is still inbound and j is out of bounds?
        # no match - we still have some string that is not matched
        
        # if i is out of bounds, does not mean return False
        # s = "ab" p = "a*b*"
        
        # s ended but we still have p
        
        # thats okay, we can not use elements in p
        # it is a "*"
        
        # because we are starting with c, 
        # we do not want to use
        # that "c" not even once
        
        # we will SHIFT j
        
        # s = "aab" p = "c*a*b"
        #      i           j
        
        """
        # NO CACHE
        
        # top down solution - no cache
        
        # using two pointers within
        # s and p , i and j
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                # found a match!
                return True
            if j >= len(p):
                # we still have string that is not matched
                return False
            
            
            # matching is key
            # "." matches any character
            # i should be inbound
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            # is j + 1 inbound and is it a star 
            if (j+1) < len(p) and p[j + 1] == "*":
                return (dfs(i, j + 2) or # do not use the star
                        (match and dfs(i+1, j))) # use the star
            
            if match:
                return dfs(i + 1, j + 1)
            
            return False
        
        return dfs(0, 0)"""
        
        # WITH CACHE
        
        # top down solution - with cache
        
        # using two pointers within
        # s and p , i and j
        cache = {}
        
        def dfs(i, j):
            
            # if calculated
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                # found a match!
                return True
            if j >= len(p):
                # we still have string that is not matched
                return False
            
            
            # matching is key
            # "." matches any character
            # i should be inbound
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            # is j + 1 inbound and is it a star 
            if (j+1) < len(p) and p[j + 1] == "*":
                
                # use the star or do not use the star
                cache[(i, j)] = (dfs(i , j + 2) or (match and dfs(i+1, j)))
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False
        
        return dfs(0, 0)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            