"""
Given an array of intervals intervals where 

intervals[i] = [starti, endi], 

return the minimum number of 
intervals you need to remove to make the rest of the 
intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1

Explanation: [1,3] can be removed and the rest of the 
intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest 
of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals 
since they're already non-overlapping.
 
Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104

Takeaway:

This is actually a really good problem.

WE check interval overlapping as the incoming start
being smaller than previous end.

Which one should we remove?

IN two overlapping intervals, we should remove 
the one which ends first to minimize the chance of overlaps
in the incoming intervals.

Obviously, we should start by sorting with starting point.

"""
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Start by sorting the intervals by start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for elem in intervals[1:]:
            if elem[0] < result[-1][1]:
                # If new elem's start is smaller than last elem's end, there is an overlap
                # Choose the interval with the smaller end time to remove
                result[-1][1] = min(elem[1], result[-1][1])
            else:
                result.append([elem[0], elem[1]])

        print(result)
                
        return len(intervals) - len(result)
    
    def eraseOverlapIntervals_(self, intervals: list[list[int]]) -> int:
        # neet
        intervals.sort(key = lambda x: x[0])
        
        res = 0
        # initial first value  end
        prev_end = intervals[0][1]
        # start from 1st index
        for start, end in intervals[1:]:
            # not overlapping
            if start >= prev_end:
                # update the prev_end
                prev_end = end
            # overlapping
            else:
                # we will remove
                res += 1
                # remove the min end value one
                prev_end = min(end, prev_end)
        return res
        
