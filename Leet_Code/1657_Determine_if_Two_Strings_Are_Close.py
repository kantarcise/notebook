"""
Two strings are considered close if you can attain one from 
the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb

Operation 2: Transform every occurrence of one existing character into 
another existing character, and do the same with the other character.

For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and 
word2 are close, and false otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true

Explanation: You can attain word2 from word1 in 2 operations.

Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false

Explanation: It is impossible to attain word2 from word1, or 
vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.

Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.

Takeaway:

Calm down and understand the cases, one by one.

list.sort() runs inplace and returns None
You need sorted() if you are going to do a comparison

Counter.items()
Counter.keys()
Counter.values()
"""

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # to be close strings
        # len should be the same
        if len(word1) != len(word2):
            return False
        
        # frequency dict keys should be the same 
        counter_1, counter_2 = Counter(word1), Counter(word2)
        
        if counter_1.keys() != counter_2.keys():
            print(counter_1.keys())
            print(counter_2.keys())            
            print("keys")
            return False
        
        # frequency dict values should be equal
        if sorted([elem for elem in counter_1.values()]) != sorted([elem for elem in counter_2.values()]):
            print("values")
            return False
        
        return True
    
    def closeStrings_(word1, word2):
        
        # homie
        # Since we can swap frequency of characters and position 
        # hence we just need to make sure that there are 
        # same unqiue characters and same frequencies 
        # in both the strings

        c1, c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())
