"""
Given a non-negative integer x, return the square root of x rounded 
down to the nearest integer. The returned integer should 
be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 
Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we 
round it down to the nearest integer, 2 is returned.

Constraints:

0 <= x <= 231 - 1

Takeaway:

You don't need to check every single number possible, you have x

Of course, using Binary search is feasible here.

"""

class Solution:
    def mySqrt_(self, x: int) -> int:
        # my first try
        
        # we can look within a 
        # specific range until we find the number 
        
        # let x be 5436324562
        # 256 
        # 16
        # make a huge hashmap?
        
        # my_sqrts = {elem: elem * elem for elem in range(0,256)}
        
        # for index, values in enumerate(my_sqrts):
        #     if x < values:
        #         return index
        #     else:
        #         pass
    
        # we dont have to make this.
        # LOL 
        # No 2**31 -1 please
        # all_integers = [elem for elem in range(x)]
        
        low, high = 0 , len(all_integers) -1

        # cannot use this
        target = x ** 0.5
        while low <= high:
            middle = low + ((high - low) // 2)
            if target == all_integers[middle]:
                return middle
            elif target < all_integers[middle]:
                high = middle - 1
            else:
                low = middle + 1
        
        return middle
    
    def mySqrt(self, x: int) -> int:
        # here is a better approach
        if x == 0 | x == 1 : 
            return x

        low, high = 1, x
        while low <= high:
            middle = low + ((high - low) // 2)
            # if middle value is equal to x divide by middle
            if middle == x // middle:
                # return it
                return middle
            elif middle > x // middle:
                high = middle - 1
            else:
                low = middle + 1
        # we are looking for the floored value
        return high
        
