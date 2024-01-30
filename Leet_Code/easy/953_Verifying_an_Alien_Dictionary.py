"""
In an alien language, surprisingly, they also use English lowercase letters, but 
possibly in a different order. The order of the alphabet is some 
permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order 
of the alphabet, return true if and only if the given words are 
sorted lexicographically in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this 
    language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string 
is shorter (in size.) According to lexicographical rules "apple" > "app", 
because 'l' > '∅', where '∅' is defined as the blank character which 
is less than any other character (More info).
 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

Takeaway:

Really cool question. 

zip() and a dict() for points.

"""

class Solution:
    def isAlienSorted_(self, words: List[str], order: str) -> bool:
        # could not make it work
        
        # None is smaller than all
        
        # I can map and score words based on order
        order_map = {elem: i for i, elem in enumerate(order)}
        
        # make this a list of lists
        a = [word[0] for word in words]
        
        for i in range(len(min(words, key= len))):
            temp = [word[i] for word in words]
            if temp == sorted(temp , key = lambda x: order_map[x]):
                continue
            else:
                return False
            
        return True
            
        
    def isAlienSorted(self, words, order):
        # from lee
        
        # same map
        m = {c: i for i, c in enumerate(order)}
        
        # list of lists
        words_points = [[m[c] for c in w] for w in words]
        
        # expecting all words to be in 
        # compare 0 to 1
        # compare 1 to 2
        # ...
        return all(w1 <= w2 for w1, w2 in zip(words_points, words_points[1:]))
