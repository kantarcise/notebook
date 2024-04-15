"""
Given a signed 32-bit integer x, return x with 
its digits reversed. 

If reversing x causes the value to go outside the signed 
32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to 
store 64-bit integers (signed or unsigned).

Example 1:

    Input: x = 123
    
    Output: 321

Example 2:

    Input: x = -123
    
    Output: -321

Example 3:

    Input: x = 120
    
    Output: 21

Constraints:

    -2^31 <= x <= 2^31 - 1

Takeaway:
    
    lstrip() will strip your strings.

    string conversion is cool.

    If you need digits, you will have to use modulo and floor div.

"""

import math

class Solution:
    def reverse__(self, x: int) -> int:
        # we can just use strings
        # this works, and it was fastest on website

        if x == 0: return 0
        
        # we can just use strings
        sign = "-" if x < 0 else ""

        num_str = str(abs(x))

        result = int(sign + num_str[::-1].lstrip("0"))        
        
        # check the condition
        return result if -2**31 <= result <= 2**31 else 0

    def reverse_(self, x: int) -> int:
        # another approach would be just to 
        # calculate based on value
        # this works too

        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = int("-" + str(abs(x))[::-1])

        return res if -2**31 <= res <= 2**31 - 1 else 0

    def reverse(self, x: int) -> int:
        # instead of calculating for every value, 
        # we can skip calculating for really big numbers

        MIN = -2**31
        MAX = 2**31 - 1

        res = 0

        while x:
            # python does weird stuff for negatives
            # -1 % 10 == 9
            
            digit = int(math.fmod(x, 10))

            # cannot do normal floor division
            # -1 // 10 = -1

            # to make sure we are rounding toward zero
            x = int(x / 10) 
            
            # we can only look at the last digit 
            # to stop the loop
            if (res > MAX // 10 or 
                (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            
            if (res < MIN // 10 or 
                (res == MIN // 10 and digit <= MIN % 10)):
                return 0

            res = (res * 10) + digit
        
        return res


sol = Solution()

print(sol.reverse__(x = 123)) # 321
print(sol.reverse__(x = -123)) # -321
print(sol.reverse__(x = 120)) # 21

print()

print(sol.reverse_(x = 123)) # 321
print(sol.reverse_(x = -123)) # -321
print(sol.reverse_(x = 120)) # 21

print()
print(sol.reverse(x = 123)) # 321
print(sol.reverse(x = -123)) # -321
print(sol.reverse(x = 120)) # 21