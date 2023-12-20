"""

Given an integer num, return a string of its base 7 representation. 

Example 1:

Input: num = 100
Output: "202"

Example 2:

Input: num = -7
Output: "-10"
 

Constraints:

-10^7 <= num <= 10^7

Takeaway: 

For base questions, use divmod() 

OR

just regular %(modulo) and // (floor division)

"""

class Solution:
    def convertToBase7_(self, num: int) -> str:
        # this solution is not idela because of repeated string making
        if num == 0:
            return "0"
    
        result = ""
        is_negative = num < 0
        num = abs(num)

        while num > 0:
            num, remainder = divmod(num, 7)
            result = str(remainder) + result

        return "-" + result if is_negative else result
    
    def convertToBase7(self, num):
        # from a homie, this is way better
        if num == 0:
            return "0"
        sign = "" if num > 0 else "-"
        num = abs(num)
        res = []
        while num > 0:
            ##  append the remainder
            # res.append(str(num % 7))
            ##  recalculate num for next digit
            # num //= 7
            # OR
            num, remainder = divmod(num, 7)
            res.append(str(remainder))
        return sign + "".join(res[::-1])
