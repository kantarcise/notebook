"""
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward 
and backward. 

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false

Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true

Explanation: s is an empty string "" after removing 
non-alphanumeric characters.

Since an empty string reads the same forward 
and backward, it is a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

Takeaway:

  str.isalpha() or str.isalnum() in a loop is cool

  or you can use a filter(func, iterable) too!
"""
class Solution:
    def isPalindrome_(self, s: str) -> bool:
        # solve with filter
        result = []
        for c in s:
            if c.isalpha():
                result.append(c.lower())
                
        return "".join(result) == "".join(result)[::-1]
    
    def isPalindrome(self, s: str) -> bool:
        # isalpha is for alhabetic characters
        # chr_list = [c.lower() for c in filter(lambda x: x.isalpha(), s)]
        chr_list = [c.lower() for c in filter(lambda x: x.isalnum(), s)]
        long_str = "".join(chr_list)
        return long_str == long_str[::-1]
