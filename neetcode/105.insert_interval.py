"""
You are given an array of non-overlapping intervals 
`intervals` where intervals[i] = [start_i, end_i] represent the start 
and the end of the ith interval and intervals is 
sorted in ascending order by start_i. 

You are also given an interval newInterval = [start, end] that represents 
the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is 
still sorted in ascending order by start_i and intervals still does not 
have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    
    Output: [[1,5],[6,9]]

Example 2:

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], 
            newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]

    Explanation: 
    
        Because the new interval [4,8] overlaps 
            with [3,5],[6,7],[8,10].

Constraints:

    0 <= intervals.length <= 10^4

    intervals[i].length == 2

    0 <= starti <= endi <= 10^5

    intervals is sorted by starti in ascending order.
    
    newInterval.length == 2
    
    0 <= start <= end <= 10^5

Takeaway:

    Sorting is a great tool in interval questions.

    We gotta think of all edge cases.
"""

class Solution:

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        # intervals = [[1,3],[6,9]], newInterval = [2,5]
        # Output: [[1,5],[6,9]]
        # interval could be at the start
        # could be at the end
        # could be overlapping with single element
        # could be overlapping with multiple elements
        # could be non overlapping, just fitting between 2 elements
        res = []
        
        for i in range(len(intervals)):
            # if newInterval end is smaller than a current elements start
            if newInterval[1] < intervals[i][0]:
                # no overlapping so just return
                res.append(newInterval)
                # use result and rest of intervals
                return res + intervals[i:]
            # if newInterval start is greater than current elements end
            elif newInterval[0] > intervals[i][1]:
                # append the current element
                res.append(intervals[i])
                # do not append the new interval just yet, there could be some overlaps
            else:    
                # there is a overlap, we want to update new interval
                # overlapping can be decided with,
                # newInterval end being bigger than current element start 
                # newInterval start being smaller than current element end
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
                # do not add this newInterval just yet, because it might 
                # be overlapping with other elements

        # after the loop ends
        # now append the new interval
        res.append(newInterval)
        return res
    
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # from a homie
        new_start, new_end = newInterval[0], newInterval[1]
        res = []
        for i in range(len(intervals)):
            cur_start, cur_end = intervals[i][0], intervals[i][1]
            if new_end < cur_start:
                res.append([new_start, new_end])
                new_start, new_end = cur_start, cur_end
            elif cur_end < new_start:
                res.append([cur_start, cur_end])
            else:
                # new_start <= cur_end:
                # merge
                new_start = min(cur_start, new_start)
                new_end = max(cur_end, new_end)
        res.append([new_start, new_end])
        return res
