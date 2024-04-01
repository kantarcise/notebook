"""
Given a string s consisting of words and spaces, return 
the length of the last word in the string.

A word is a maximal substring consisting of 
non-space characters only.

Example 1:

    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.

Example 2:

    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.

Example 3:

    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.
 
Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

Takeaway:

  Wonderful string methods. strip() split()
"""

class Solution:
    def lengthOfLastWord_(self, s: str) -> int:
        # if you split from " "
        # you have to check for all elements
        l = s.split(" ")
        for i in range(len(l) - 1, -1 , -1):
            if l[i] != "":
                return len(l[i])
            
    def lengthOfLastWord__(self, s: str) -> int:
        # default split will get rid of all spaces
        return(len(s.split()[-1]))
    
    def lengthOfLastWord(self, s: str) -> int:
        # we can also strip away from right and left        
        return(len(s.strip().split()[-1]))
