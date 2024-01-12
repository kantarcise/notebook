"""
You are given a string s of even length. Split this string into two 
halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels 
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s 
contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
Takeaway:

The usual.

"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # find middle point
        # make 2 strings
        # make 2 counters
        # 2 traversion and bool comparison
        middle = len(s) // 2
        s1 = s[:middle]
        s2 = s[middle:]
        
        counter_1 , counter_2 = 0, 0
        for elem in s1:
            if elem.lower() in "aeiou":
                counter_1 += 1
                
        for elem in s2:
            if elem.lower() in "aeiou":
                counter_2 += 1
                
        return counter_1 == counter_2
