"""
Roman numerals are represented by seven 
different symbols: 

I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just 
two ones added together. 

12 is written as XII, which is simply X + II. 

The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest 
to smallest from left to right. 

However, the numeral for four is not IIII. 

Instead, the number four is written as IV. 

Because the one is before the five we subtract 
it making four. 

The same principle applies to the number nine, which 
is written as IX. 

There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 

    X can be placed before L (50) and C (100) to make 40 and 90. 

    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

    Input: s = "III"
    
    Output: 3
    
    Explanation: III = 3.

Example 2:

    Input: s = "LVIII"
    
    Output: 58
    
    Explanation: L = 50, V= 5, III = 3.

Example 3:

    Input: s = "MCMXCIV"
    
    Output: 1994
    
    Explanation: 
    
        M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

    1 <= s.length <= 15
    
    s contains only the characters 
        ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    
    It is guaranteed that s is a valid 
        roman numeral in the range [1, 3999].

Takeaway:

    Control flows require mastery.

    Dict and reverse traversal.

"""

class Solution:

    def romanToInt__(self, s: str) -> int:
        # from a homie - different approach
        total = 0
        
        # dictionary for roman numerals
        val_map = {"0": 0, 
                   "I": 1, 
                   "V": 5, 
                   "X": 10, 
                   "L": 50, 
                   "C": 100, 
                   "D": 500, 
                   "M": 1000}
        
        # Adding a special "0" character to the end 
        # of every input,  

        # so that we iterate from index 1:n and look 
        # back at the previous character.
        s += "0"
        
        for i in range(1, len(s)):
            
            v = val_map[s[i-1]]
            
            if val_map[s[i]] > v:
                total -= v
            
            else:
                total += v
        
        return total   
    
    
    def romanToInt_(self, s: str) -> int:
        # we can make a map for values
        # for each element, lookup the value
        # do not forget the edge cases

        # a sliding window can work

        roman_map = {"I": 1,
                     "V": 5, 
                     "X": 10,
                     "L": 50,
                     "C": 100,
                     "D": 500,
                     "M": 1000}

        edge_cases = {"IV": 4,
                      "IX": 9,
                      "XL": 40,
                      "XC": 90,
                      "CD": 400,
                      "CM": 900} 

        start = 0
        result = 0

        for end in range(1, len(s)+1):

            if start >= end:
                continue

            if s[start:end] in ("I", "X", "C"):
                if s[start:end + 1] in edge_cases:
                    result += edge_cases[s[start:end + 1]]
                    start += 2
                else:
                    result += roman_map[s[start:end]]
                    start += 1
            else:
                result += roman_map[s[start:end]]
                start += 1

        return result

    def romanToInt(self, s: str) -> int:
        # another appproach would be, traversing in reverse
        
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize variables to keep track of 
        # the total value and the previous value
        result = 0
        prev = 0

        # Iterate through the string in reverse
        for i in s[::-1]:
            # integer value of current roman numeral
            curr = roman_map[i]  

            # If the previous value is greater than 
            # the current value, subtract the current value

            # like a "IV", the total should be subtracted by I
            if prev > curr:
                result -= curr
            else:
                # If the current value is greater than or 
                # equal to the previous value, 
                # add the current value
                result += curr
                
                # Update the previous value to the 
                # current value for the next iteration
                prev = curr

        return result  # Return the total integer value


sol = Solution()

print(sol.romanToInt_(s = "LVIII")) # 58
print(sol.romanToInt_(s = "III"))   # 3
print(sol.romanToInt_(s = "MCMXCIV")) # 1994

print()

print(sol.romanToInt(s = "LVIII")) # 58
print(sol.romanToInt(s = "III"))   # 3
print(sol.romanToInt(s = "MCMXCIV")) # 1994