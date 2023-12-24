"""
You are given a string s consisting only of the characters '0' 
and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. 
For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".

Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.

Takeaway:

Try both ways, and check for each way, the number of changes 
needed to reach it from the given string. The answer 
is the minimum of both ways.
"""
class Solution:
    def minOperations(self, s: str) -> int:
        # two patterns for alternating
        # 0101010.. let it be pat_0 (pattern 0)
        # 1010101.. let it bee pat_1 (patter_1)
        
        pat_1 , pat_2 = 0, 0
        for i in range(len(s)):
            # one part should look at even elements
            # other one should look at odd ones.
            if i % 2 == 0:
                # even ones
                if s[i] == "0":
                    pat_1 += 1
                else:
                    pat_2 += 1
            else:
                # odd ones
                if s[i] == "1":
                    pat_1 += 1
                else:
                    pat_2 += 1
                    
        return min(pat_1, pat_2)
    
    
