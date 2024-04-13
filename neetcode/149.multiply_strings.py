"""
Given two non-negative integers num1 and num2 represented 
as strings, return the product of num1 and num2, also represented 
as a string.

Note: You must not use any built-in BigInteger library 
or convert the inputs to integer directly.

Example 1:

    Input: num1 = "2", num2 = "3"
    
    Output: "6"

Example 2:

    Input: num1 = "123", num2 = "456"
    
    Output: "56088"
 
Constraints:

    1 <= num1.length, num2.length <= 200
    
    num1 and num2 consist of digits only.
    
    Both num1 and num2 do not contain any leading 
        zero, except the number 0 itself.

Takeaway:

    You can int(str_digit) by updating the value of a number

    starting from 0 and multipling with 10 each time 

    and adding the rightmost value
"""

class Solution:

    def multiply_(self, num1: str, num2: str) -> str:
        # this is not allowed.
        if num1 == "0" or num2 == "0":
            return "0"
        return str(int(num1) * int(num2))
    
    
    def multiply(self, num1: str, num2: str) -> str:
        # from a homie
        # this is way cooler
        n1 = 0
        n2 = 0

        # for every element in that string
        for i in num1:
            # update the number, using the unicode code
            # multiply by 10 in every hit
            # add the latest value on right
            n1 = n1 * 10 + (ord(i) - 48)
        for i in num2:
            # update the number, using the unicode code
            # multiply by 10 in every hit
            # add the latest value on right
            n2 = n2 * 10 + (ord(i) - 48)

        return str(n1 * n2)
        
    def multiply__(self, num1: str, num2: str) -> str:
        # works, but NOT good.
        
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10
            
        res, beg = res[::-1] , 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)

sol = Solution()
print(sol.multiply("123", "5"))
