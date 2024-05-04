"""
Given a 0-indexed string word and a character ch, 
reverse the segment of word that starts at index 
0 and ends at the index of the first occurrence 
of ch (inclusive). 

If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then 
you should reverse the segment that starts at 0 and 
ends at 3 (inclusive). The resulting string will be "dcbaefd".

Return the resulting string.

Example 1:

    Input: word = "abcdefd", ch = "d"

    Output: "dcbaefd"
    
    Explanation: 
    
        The first occurrence of "d" is at index 3. Reverse 
        the part of word from 0 to 3 (inclusive), the 
        resulting string is "dcbaefd".

Example 2:

    Input: word = "xyxzxe", ch = "z"

    Output: "zxyxxe"
  
    Explanation: 
      
        The first and only occurrence of "z" is at index 3. 
        Reverse the part of word from 0 to 3 (inclusive), 
        the resulting string is "zxyxxe".

Example 3:

    Input: word = "abcd", ch = "z"
    
    Output: "abcd"
    
    Explanation: 
    
        "z" does not exist in word.
        You should not do any reverse operation, the 
        resulting string is "abcd".

Constraints:

    1 <= word.length <= 250
    word consists of lowercase English letters.
    ch is a lowercase English letter.

Takeaway:

    strings have find and index methods.

    if no match, find will return -1
    if no match, index will give you an error.

    control flow.

"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # word = "abcdefd"
        # ch = "d"
        # result = "dcbaefd"
        
        # key decision is whether or not ch exist
        if word.find(ch) == -1:
            return word
        
        # lets make our own string
        # from a list because we do not want to 
        # make a lot of strings
        result = []
        
        # add the reverse to the start of result
        for i in range(word.find(ch), -1, -1):
            result.append(word[i])
        
        # add the rest to the result
        for j in range(len(result), len(word)):
            result.append(word[j])
            
        return "".join(result)
    
