"""    
Given an integer num, repeatedly add all its digits until the 
result has only one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

Constraints:

0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?

Takeaway:

Learn to use Augmented assignment arithmetic. It will save you memory.

floor division, if consistently applied, will result to 0 in the end. 
You can use this property in a while condition.

12 % 10 = 2
4 // 10 = 0

"""

class Solution:
    def addDigits_(self, num: int) -> int:
        # my first approach
        if num < 10: 
            return num
        while num >= 10 :
            # get each digit
            # 38
            seq = []
            for _ in range(len(str(num))):
                seq.append(num % 10)
                num, _ = divmod(num, 10) 
            # sum them
            # point num to the result
            num = sum(seq)
        return num            
    
    def addDigits__(self, num):
        # cleaner, less memory
        while num > 9:
            total = 0
            # 38
            while num:
                total += num % 10
                num //= 10
        return num
    
    def addDigits(self, num):
        # hard.
        return num if num == 0 else num % 9 or 9
