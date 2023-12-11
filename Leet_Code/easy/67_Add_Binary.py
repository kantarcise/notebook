"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

Takeaway:

Format is pretty cool.

bin() for binary strings.

Also, int(n, 2) or int(j, 16) pretty aswell.

"""
class Solution:
    def addBinary_(self, a: str, b: str) -> str:
        # this is my way
        return bin(int(a, 2) + int(b, 2))[2:]
    
    def addBinary(self, a: str, b: str) -> str:
        # from a homie
        return format( int(a,2) + int(b,2),'b')
