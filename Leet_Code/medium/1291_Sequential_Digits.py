"""
An integer has sequential digits if and only if 
each digit in the number is one more than 
the previous digit.

Return a sorted list of all the integers in the 
range [low, high] inclusive that have 
sequential digits.

Example 1:

    Input: low = 100, high = 300
    Output: [123,234]

Example 2:

    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:

    10 <= low <= high <= 10^9

Takeaway:

    String and int dance    

"""

from math import log

class Solution:
    def sequentialDigits__(self, low: int, high: int) -> List[int]:
        # DOES NOT work
        # way too complicated
        
        result = []
        
        # difference is always 11 111 1111 and so on
        
        # starts, 12 123 1234 12345
        
        # find the start
        start = (12 * 10 ** (low//10)) + (log(low, base = 10))
        
        # based on the start add 11 or 111 to start until it maxes out
        
        if low <= start <=high:
            result.append(start)
        
        add = 11 * (10 ** len(str(start))) + 1
        
        elem = start + add
        
        if low <= elem <=high:
            result.append(start)
        
        
        while not elem % 9 == 0:
            elem += add
            result.append(elem)
        
        pass


    def sequentialDigits_(self, low: int, high: int) -> List[int]:
        # from a homie
        result = []

        for digit in range(1,10):
            # get the digit and the next one
            num = digit
            nextDigit = num + 1

            while num <= high and nextDigit <= 9:
                # num smaller than high and 
                # next digit is single digit
                
                # move num upwards
                num = num*10 + nextDigit
                if num >= low and num <= high:
                    result.append(num)
                    
                # increase next digit
                nextDigit += 1

        return sorted(result)
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # best solution - from a homie
        
        # all digits as a string
        digits = "123456789"
        results = []
        
        # the number of digits for low and high
        dl, dh = len(str(low)), len(str(high))
        
        # digit number loop
        for i in range(dl, dh + 1):
            for j in range(0, 10 - i):
                # select part of digits
                num = int(digits[j : j+ i])
                # print(num)
                if num <= high and num >= low: 
                    # base condition
                    results.append(num)
                    
        return results
