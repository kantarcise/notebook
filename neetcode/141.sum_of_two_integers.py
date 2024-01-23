"""
Given two integers a and b, return the sum of the two 
integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5

Constraints:

    -1000 <= a, b <= 1000


Takeaway:

Addition without + - 

You gotta think of bitwise operations!

XOR for sum and Shifted AND for carry!

"""
class Solution:
    def getSum_(self, a: int, b: int) -> int:
        # this runs infinitely becuase there is no 
        # limit for an intereget in python
        while b != 0:
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        
        return a
    
    def getSum(self, a: int, b : int) -> int:
        #  The first step is to manually bound the length of sum 
        # and carry by setting up a mask 0xFFFFFFFF. & this mask with 
        # an (very long) integer will only keep the last 32 bits. 
        
        # Then, at each step of the loop, we & sum and carry with this 
        # mask, and eventually carry will be wiped out once it goes beyond 32 bits.

        #  1001 (9)
        #  1011 (11)
        #  ----
        #  0010 just a ^ b - sum
        # 10010 a & b << 1 - carry
        # -----
        # 10100 - (20) ! voila
        
        # Python doesn't handle negative numbers like C++/Java
        # Therefore, we need to use bitmask to simulate 32-bit integer overflow
        mask = 0xffffffff
        while b:
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry
            
        # If a is negative, use (~a & mask) to get its positive value.
        
        # If a is positive, its binary representation is the same as its original.
        # If a is negative, its binary representation is the same as its 
        # positive counterpart in a 32-bit system.
        
        # The mask here is used to simulate 32-bit integer overflow in Python.
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
