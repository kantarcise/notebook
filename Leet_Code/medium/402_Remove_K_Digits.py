"""
Given string num representing a non-negative integer num, and 
an integer k, return the smallest possible integer 
after removing k digits from num.

Example 1:

    Input: num = "1432219", k = 3
    
    Output: "1219"
    
    Explanation: 
        
        Remove the three digits 4, 3, and 2 to form 
        the new number 1219 which is the smallest.

Example 2:

    Input: num = "10200", k = 1
    
    Output: "200"
    
    Explanation: 
        
        Remove the leading 1 and the number is 200. 
        Note that the output must not contain leading zeroes.

Example 3:

    Input: num = "10", k = 2
    
    Output: "0"
    
    Explanation: 
        
        Remove all the digits from the number and 
        it is left with nothing which is 0.
 
Constraints:

    1 <= k <= num.length <= 105
    
    num consists of only digits.
    
    num does not have any leading zeros except for the zero itself.

Takeaway:

    Stacks can be used in a sliding window kind of way.

"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # make a stack
        result = []

        # initialize with first element
        result.append(num[0])

        # based on condition decide if you want to
        # keep the current element
        for i in range(1, len(num)):
            temp = num[i]
            
            # condition
            # we do not want peak elements 
            # if we have coins to pop from out stack
            while result and result[-1] > temp and k:
                # remove peak element
                result.pop()
                k -= 1
            
            result.append(temp)
        
        # even after the condition
        # if there are k's left,
        while k:
            # remove from end
            result.pop()
            k -= 1
            
        # remove leading zeroes
        res = "".join(result).lstrip("0")
        
        # return string if not empty
        return res if res != "" else "0"
    
sol = Solution()
print(sol.removeKdigits(num = "1432219", k = 3)) # 1219
print(sol.removeKdigits(num = "10200", k = 1)) # 200
