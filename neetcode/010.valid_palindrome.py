"""
Q: A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same 
forward and backward. 

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or 
false otherwise.

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
        Since an empty string reads the same forward and 
        backward, it is a palindrome.

"""

class Solution:
    def isPalindrome_(self, s:str):
        # we can simply use string methods.

        result_string = ""

        for c in s:
            if c.isalnum():
                result_string += c.lower()

        return result_string == result_string[::-1]


    def isPalindrome(self, s: str):
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

    def isPalindrome__(self, s: str):
        """You can write the alphanumeric function yourself.
        Also you dont need to reverse the string. 
        You can compare the characters one by one"""

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

    # best approach ?
    print(sol.isPalindrome(s = "A man, a plan, a canal: Panama"))
    print(sol.isPalindrome(s = "race a car"))

    # second approach - string methods
    print(sol.isPalindrome_(s = "A man, a plan, a canal: Panama"))
    print(sol.isPalindrome_(s = "race a car"))

    # third approach, our own alphanumeric function
    print(sol.isPalindrome__(s = "A man, a plan, a canal: Panama"))
    print(sol.isPalindrome__(s = "race a car"))
