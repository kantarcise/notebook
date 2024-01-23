"""
Given a signed 32-bit integer x, return x with its 
digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.

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

    -231 <= x <= 231 - 1

Takeaway:

Yeah you can use str and int conversions

BUT

Modding is the key to popping

And floor division is key to get tid of values!

"""
class Solution:
    def reverse_(self, x: int) -> int:
        # my first approach
        # works
        negative = False
        if x < 0:
            negative = True
            
        x_str = str(abs(x))
        
        
        if negative:
            if (int(x_str[::-1]) * -1) < (-2 ** 31):
                return 0
            else:
                return int(x_str[::-1]) * -1
        else:
            if int(x_str[::-1]) > (2 ** 31 - 1):
                return 0
            else:
                return int(x_str[::-1])
            
    def reverse(self, x):
        # clear solution from a homie!
        res = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        
        while x:
            # which value is going to be popped ?
            popped = x % 10
            # which value is going to be added?
            res = res * 10 + popped
            # trim off x
            x //= 10
        
        return 0 if res > 2**31 else res * symbol

    