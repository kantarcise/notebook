"""
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. 

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
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:

  1 <= s.length <= 2 * 10^5
  s consists only of printable ASCII characters.

Takeaway:

  Palindrome simply means that reverse of the string is equal to original string

  strings have wonderful methods:

  string.isalpha()        and         string.lower()

  str_seq[::-1] is reversed of str_seq

  Other wonderful string methods:

  string.strip() , string.split() , string.capitalize()

  string.isdigit(), string.title(), string.starswith(), string.endswith()

  You can use two pointers approach.
  In this example, this basically means to check some conditions for each of the 
  pointers and progress both of them.

"""

class Solution:
   
    def is_palindrome_wrong_and_confused(self, s: str) -> bool:
        # my first attempt, does not work
        lower_s = "".join(s.lower())

        alphabetical_s = lower_s.maketrans("_=.*", "    ")
        # lowercase all of it

        # remove non alphanumeric characters

        # if empty, its palindrome is palindrome
        if len(alphabetical_s) == 0:
            return True
        else:
            # if the last element and first element is the same for all elements
            middle = len(s) //  2
            if s[:middle:-1] == s[middle:]:
                return True
        return False

    def is_palindrome(self, s:str):
        # we can simply use string methods.
        new_str = ""

        # basically for every alphabetic character, 
        # construct a new string
        for c in s:
            if c.isalnum():
                new_str += c.lower()

        # reverse a sequence
        return new_str == new_str[::-1]
    
    def isPalindrome_(self, s: str):
        # we can use two pointers and not worry about 
        # reversing the string
        
        l, r = 0 , len(s) - 1

        while l < r:
            # pass all non alphanumeric characters
            while l < r and not s[l].isalpha():
                l += 1
            while r > l and not s[r].isalpha():
                r -= 1

            # check equality
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        # if all passed, we found a Palindrome
        return True

 
    def is_palindrome_two_pointers(self, s: str):
        """You can write the alphanumeric function yourself.
        Also you dont need to reverse the string. You can 
        compare the characters one by one"""

        l, r = 0 , len(s) - 1

        while l < r:
            # pass all non alphanumeric characters
            while l < r and not self.alphanumeric(s[l]):
                l += 1
            while r > l and not self.alphanumeric(s[r]):
                r -= 1
            
            # check equality
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        
        # if all passed, we found a Palindrome
        return True
        
    def alphanumeric(self, s):
        return (ord("A") <= ord(s) <= ord("Z")) or \
            (ord("a") <= ord(s) <= ord("z")) or \
            (ord("0") <= ord(s) <= ord("9"))


if __name__ == '__main__':
    sol = Solution()
    print(sol.is_palindrome_wrong_and_confused("A man, a plan, a canal: Panama"))
    print(sol.is_palindrome_wrong_and_confused("race a car"))
    print(sol.is_palindrome_wrong_and_confused(" "))
    print(sol.is_palindrome("A man, a plan, a canal: Panama"))
    print(sol.is_palindrome("race a car"))
    print(sol.is_palindrome(" "))
    print(sol.is_palindrome_two_pointers("A man, a plan, a canal: Panama"))
    print(sol.is_palindrome_two_pointers("race a car"))
    print(sol.is_palindrome_two_pointers(" "))

