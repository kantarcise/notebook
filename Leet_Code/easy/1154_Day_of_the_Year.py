"""
Given a string date representing a Gregorian 
calendar date formatted as YYYY-MM-DD, return the
day number of the year.

Example 1:

    Input: date = "2019-01-09"

    Output: 9

    Explanation: 
      Given date is the 9th day of the year in 2019.

Example 2:

    Input: date = "2019-02-10"

    Output: 41
 
Constraints:

    date.length == 10
    
    date[4] == date[7] == '-', and all other 
      date[i]'s are digits
    
    date represents a calendar date between Jan 
      1st, 1900 and Dec 31th, 2019.

Takeaway:

# 1	January	31
# 2	February	28 (29 in leap years)
# 3	March	31
# 4	April	30
# 5 May	31
# 6	June	30
# 7	July	31
# 8	August	31
# 9	September	30
# 10	October	31
# 11	November	30
# 12	December	31

    leap year and control flow.
"""

class Solution:
    def dayOfYear_(self, date: str) -> int:
        # works!
        
        y, m, d = date.split("-")
        
        normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
        leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
        
        # is 1900 leap year ??
        
        # To be a leap year, the year number 
        # must be divisible by four 
        # Except for end-of-century years, 
        # which must be divisible by 400. 
         
        # 1900 is not leap year
        
        total = 0
        
        if y == "1900" or int(y) % 4 != 0:
            # not leap
            for i in range(int(m) - 1):
                total += normal_year[i]
            
            total += int(d)
            
        else:
            # leap year
            for i in range(int(m)- 1):
                total += leap_year[i]
            
            total += int(d)
            
        return total
    
    def dayOfYear(self, date: str) -> int:
        # cool solution
        y, m, d = map(int, date.split('-'))
        
        # add 1 on leap years 
        if (y % 400 == 0 or 
            (y % 100 != 0 and y % 4 == 0)) and m > 2: 
            d += 1
            
        # normal years
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        for i in range(1, m):
            d += months[i-1]
        
        return d
