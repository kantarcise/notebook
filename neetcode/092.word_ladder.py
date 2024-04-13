"""
A transformation sequence from word beginWord to word endWord using 
a dictionary wordList is a sequence of words 
beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.

    Every si for 1 <= i <= k is in wordList. 
        Note that beginWord does not need to be in wordList.
    
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return 
the number of words in the shortest transformation sequence from 
beginWord to endWord, or 0 if no such sequence exists.

Example 1:

    Input: 
        beginWord = "hit", endWord = "cog", 
        wordList = ["hot","dot","dog","lot","log","cog"]
    
    Output: 5

    Explanation: 
    
    One shortest transformation sequence 
        is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

    Input: 
        beginWord = "hit", endWord = "cog", 
        wordList = ["hot","dot","dog","lot","log"]
    
    Output: 0

    Explanation: 
        The endWord "cog" is not in wordList, therefore 
            there is no valid transformation sequence.

Constraints:

    1 <= beginWord.length <= 10
    
    endWord.length == beginWord.length
    
    1 <= wordList.length <= 5000
    
    wordList[i].length == beginWord.length
    
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    
    beginWord != endWord
    
    All the words in wordList are unique.

Takeaway:

    BFS - A SET AND A DEQUE IS A CLASSIC

    Make a adjacency map with a defaultdict

    For shortest path, BFS is GOOD
"""

from collections import deque
from collections import defaultdict
from collections import Counter

class Solution:
    def ladderLength_(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # every word with one letter difference is connected.
        # if there is a path from start to end, we found the solution!
        
        # brute force
        # DOES NOT WORK 
        
        if beginWord not in wordList or endWord not in wordList:
            return 0
        
        adj = {}
        
        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                if self.one_diff(wordList[i], wordList[j]):
                    adj[wordList[i]] = wordList[j]
            
        visited = set()
        
        def bfs(word):
            if word in visited:
                return 
            
            visited.add(word)
            
            pass
        
        return bfs(beginWord)
            
    def one_diff_(self, word1, word2):
        # part of what does not work 
        return True if len(Counter(word1) - Counter(word2)) == 1 else False
    
    def ladderLength__(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # expert help, works
        if endWord not in wordList:
            return 0

        wordList = set(wordList)

        queue = deque([(beginWord, 1)])  # Initial word and its level

        while queue:
            current_word, level = queue.popleft()

            if current_word == endWord:
                return level

            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + char + current_word[i + 1:]

                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append((next_word, level + 1))

        return 0  # No transformation sequence found
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # we need to make the graph ourselves,
        # beginning word might not be in wordList
        
        # making the graph in a nested loop takes O(N^2*M) time where
        # m is the length of word, n is the number of words
        # this does not cut it
        
        # To make the adjacency list, use patters:
        
        #      / *it
        #   hit- h*t  
        #      \ hi*
        
        # for every pattern, make a dictionary
        
        # To find the shortest path, BFS is really good
        
        if endWord not in wordList:
            return 0
        
        # a defaultdict for adjacency map
        neigh = defaultdict(list)
        wordList.append(beginWord)
        
        # make the adjacency list
        for word in wordList:
            for j in range(len(word)):
                # every word is same len
                pattern = word[:j] + "*" + word[j+1:]
                neigh[pattern].append(word)
        
        visit = set(beginWord) # to mark visit
        
        # BFS THING
        # add the beginning word, 
        #  pop elements and go layer by layer
        q = deque([beginWord]) 
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    # the end!
                    return res
                # using the pattern, visit all neighbours in BFS
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neigh_word in neigh[pattern]:
                        if neigh_word not in visit:
                            visit.add(neigh_word)
                            q.append(neigh_word)
            res += 1
            
        # could not reach
        return 0
