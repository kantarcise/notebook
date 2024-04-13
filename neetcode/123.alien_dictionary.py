"""
There is a foreign language language which uses the latin 
alphabet, but the order among letters 
is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from 
the dictionary, where the words are sorted lexicographically 
based on the rules of this new language.

Derive the order of letters in this language. 

If the order is invalid, return an empty string. 

If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a 
string b if either of the following is true:

    The first letter where they differ is smaller in a than in b.
    
    There is no index i such that a[i] != b[i] and a.length < b.length.

Example 1:

    Input: ["z","o"]

    Output: "zo"
    
    Explanation:
        From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

    Input: ["hrn","hrf","er","enn","rfnn"]

    Output: "hernf"

    Explanation:

        from "hrn" and "hrf", we know 'n' < 'f'
        from "hrf" and "er", we know 'h' < 'e'
        from "er" and "enn", we know get 'r' < 'n'
        from "enn" and "rfnn" we know 'e'<'r'
        so one possibile solution is "hernf"

Constraints:

    The input words will contain characters only from 
        lowercase 'a' to 'z'.
    
    1 <= words.length <= 100
    
    1 <= words[i].length <= 100

Takeaway:

    Hard one. We will need an adjaceny list.

    The comparison is just like Python strings.

    DFS is fancy.
"""

from collections import defaultdict

class Solution:

    def foreignDictionary_(self, words: list[str]) -> str:
        # failed.
        # we can find set of rules for each duo
        # smaller bigger 
        compare_map = {}

        def compare(w1, w2):
            # longer word is not good because we will 
            # lose the order of the characters
            try:
                for i in range(len(w1)):                
                    if w1[i] != w2[i]:
                        compare_map[w1(i)] = w2[i] 
            except:
                pass

        for i in range(len(words) - 1):
            compare(words[i], words[i+1])

        return "".join([str(elem) for elem in list(compare.keys())])

    def foreignDictionary__(self, words: list[str]) -> str:
        # this fails on some test cases - idk
        # Create a default dictionary to 
        # store the order relationships
        compare_map = defaultdict(set)

        def compare(w1, w2):
            min_len = min(len(w1), len(w2))
            for i in range(min_len):
                if w1[i] != w2[i]:
                    compare_map[w1[i]].add(w2[i])
                    break

        for i in range(len(words) - 1):
            compare(words[i], words[i + 1])

        # Perform a topological sort to derive the order
        result = []
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in compare_map[node]:
                dfs(neighbor)
            result.append(node)

        for word in set("".join(words)):
            dfs(word)

        return "".join(reversed(result))

    def foreignDictionary(self, words: list[str]) -> str:
        # this works

        # this question will involve, topological sort
        # which means a Directed Acrilic Graph
        
        # longer word is always bigger than short one

        # wrt, wrf, er, ett, rftt 
        
        # t -> f
        # w -> e
        # r -> t       which results 
        # e -> r        w -> e -> r -> t -> f
        
        # if there is a cycle in the graph,
        # there is a problem, 
        # so return ""

        # if we have 2 or 3 or more different 
        # group of rules, no problem
        # just add them together, based on what you know

        # a, ba, bc, c

        # plain dfs will not work here - 
        # it might return "acb"

        # we will be doing PostOrderDFS
        # Add the leaf nodes before the start node
        # unlike normal DFS

        # we will get the result and can reverse it later
        # "cba" ---- "abc"

        # we will have a "visit" set
        # and a "path" too

        # make the adjacency list

        # we want every char to be mapped to a set
        # a set to make sure we do not have duplicates
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # if min_len of each word are the same,
            # meaning the prefixes of the words are same
            # but first word is longer than second word
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                # invalid ordering
                return ""

            # go through every single character
            for j in range(min_len):

                if w1[j] != w2[j]:
                    # the char in w2 comes after w1
                    adj[w1[j]].add(w2[j])
                    # we are not interested in the 
                    # rest of the characters
                    break

        # for each character, False or True          
        visit = {} # False = visited, True = current path
        
        # we will join the characters in the end in the 
        # reverse order
        res = []

        # use only the current character
        def dfs(c):
            if c in visit:
                # if already in visit,
                # return the value stored in visit
                return visit[c]

            visit[c] = True

            for nei in adj[c]:
                # for every neighbour of c
                # using the adjacency list
                if dfs(nei):
                    # if this is True,
                    # we can return True
                    # signaling we detected a loop
                    return True

            # still visited but no longer in path
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                # we detected a loop
                return ""
        res.reverse()
        return "".join(res)
