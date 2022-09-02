# 7. Reverse Integer
# Medium
# 
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
# the signed 32-bit integer range [-231, 231 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# 
# 
# Example 1:
# 
# Input: x = 123
# Output: 321
# 
# Example 2:
# 
# Input: x = -123
# Output: -321
# 
# Example 3:
# 
# Input: x = 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        _negative = False
        _list = list(str(x))

        if _list[0] == "-":
            _negative = True
            _list.pop(0)

        # Now we have only numbers:
        for i in range(1,len(_list)):
            if _list[-1] == "0":
                _list.pop(-1)

        # Now we have number without the zeros in the end. 
        output_str = "".join(_list[::-1])

        if _negative:
            output_str = "-" + output_str
            
        output_int = int(output_str)

        upper_bound = 2**31 - 1
        lower_bound = 2**31 * (-1) 
        
        if output_int > upper_bound or output_int < lower_bound:
            output_int = 0
        
        return output_int
