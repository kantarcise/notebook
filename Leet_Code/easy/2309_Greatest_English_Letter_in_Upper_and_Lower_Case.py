"""
Given a string of English letters s, return the greatest English 
letter which occurs as both a lowercase and uppercase 
letter in s. The returned letter should be in 
uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another 
letter a if b appears after a in the English alphabet.

Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.

Example 2:

Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

Example 3:

Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.
 
Constraints:

1 <= s.length <= 1000
s consists of lowercase and uppercase English letters.

Takeaway:

Counter is cool. Use tenary if needed. 

set() is possible too. 

Classic str methods.
"""

from collections import Counter

class Solution:
    def greatestLetter(self, s: str) -> str:
        """This works but boy it made me work for it"""
        
        # my solution
        lower_map = Counter()
        upper_map = Counter()        
        
        for letter in s:
            if letter.islower():
                lower_map[letter] += 1
            else:
                upper_map[letter.lower()] +=1
                
        # print(lower_map)
        # print(upper_map)
        # print(type((lower_map & upper_map))) # a counter aswell
        
        # print(sorted(list((lower_map & upper_map))))
        
        # if there is an intersection, return the uppercase version of the last element in sorted order
        return (sorted(list((lower_map & upper_map)))[-1]).upper() if list((lower_map & upper_map)) else ""
    
    def greatestLetter_(self, s: str) -> str:
        # from a homie
        letters = set(s)
        greatest = ''
        
        for ltr in letters:
            # if a letter in uppercase and 
            # lowercase is inside of the letters too
            if ltr.isupper() and ltr.lower() in letters:
                # update greatest
                greatest = max(ltr, greatest)
                
        return greatest
