"""
Write a function that reverses a string. The input 
tring is given as an array of characters s.

You must do this by modifying the input 
array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

Takeaway:

2 pointers is cooler, thank god for tuple switching

l.reverse() is cool too.
"""

class Solution:
    def reverseString_(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # using the list method
        s = s.reverse()
        
    def reverseString(self, s: List[str]) -> None:
        low, high = 0, len(s) - 1 
        
        while low < high:
            s[low], s[high] = s[high], s[low]
            low +=1
            high -= 1
