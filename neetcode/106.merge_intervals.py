"""
Given an array of intervals where 

intervals[i] = [starti, endi], merge all overlapping 
intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

Takeaway:

CALM DOWN and think about the problem 

list.sort(key = lambda ...) is a classic

You can solve it in a single traverse.

"""

class Solution:
    def merge_(self, intervals: list[list[int]]) -> list[list[int]]:
        # could not make this work
        
        """Given the list of interval lists,
        merge overlapping intervals and return the 
        list of non-verlapping intervals"""
        
        # [[1,3],[2,6],[8,10],[15,18]]
        
        # we can populate a result list
        # by starting and finishing at min max values
        # and updating them
        
        result = []
        current_min = 0
        current_max = 0
        
        for elem in intervals:
            if elem[0] <= current_min:
                result.append(elem)
                current_min = elem[0]
                current_max = elem[1]
                continue
                
            # not overlapping
            if elem[1] > current_min and elem[0] > current_max:
                result.append(elem)
                current_min = elem[0]
                current_max = elem[1]
            
            # overlap
            if elem[0] < current_max:
                temp = [elem[0], elem[1]]
                # ?
        return result
        
        
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """Given the list of interval lists,
        merge overlapping intervals and return the 
        list of non-overlapping intervals"""
        
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        result = []
        
        for elem in intervals:
            # this NOT RESULT is a sneaky edge case
            if not result or elem[0] > result[-1][1]:
                # If no overlap 
                # OR 
                # the current interval starts after the last one ends, 
                # add elem to result
                result.append(elem)
            else:
                # If there's an overlap, merge the intervals
                # by updating second element of the interval 
                # in the last elemen of the result list.
                result[-1][1] = max(result[-1][1], elem[1])
        
        return result
    
    
    def merge__(self, intervals: list[list[int]]) -> list[list[int]]:
        # neet
        intervals.sort(key = lambda x : x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output
