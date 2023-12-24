"""
Given a string s of zeros and ones, return the maximum score 
after splitting the string into two non-empty 
substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros 
in the left substring plus the number of 
ones in the right substring.

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:

Input: s = "1111"
Output: 3
 
Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.

Takeaway:

O(n^2) is straight forward. str.count("a") is cool. 

You can do better, understanding the question.

You can do 2 traverses to leverage double O(N) being O(N) anyway.

"""

class Solution:
    def maxScore_(self, s: str) -> int:
        # we can make a list containing all results 
        # an return max of it
        # edge case:
        if len(s) == 2:
            return s[0].count("0") + s[1].count("1")
        
        result = []
        # smallest left window is length 1
        # smallest right window is also length 1
        for i in range(1, len(s)):
            result.append(self.calc(s[:i], s[i:]))
        return max(result)
    
    def calc(self, s1, s2):
        return s1.count("0") + s2.count("1")
    
    def maxScore(self, s: str) -> int:
        # from a homie
        # O(n) - We iterate through the string once.
        max_score = count_zeros_left = 0
        count_ones_right = s.count('1')

        # looking from left to right. Without the latest item
        for i in range(len(s) - 1):
            if s[i] == '0':
                count_zeros_left += 1
            if s[i] == '1':
                # decrement what you already calculated because you will 
                # add two score components  
                count_ones_right -= 1
            # update max score
            max_score = max(max_score, count_zeros_left + count_ones_right)

        return max_score
