"""
Given an array of meeting time interval objects consisting 
of start and end times 

    [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
    
find the minimum number of days required to schedule all 
meetings without any conflicts.

Example 1:

    Input: intervals = [(0,40),(5,10),(15,20)]

    Output: 2

    Explanation:
        
        day1: (0,40)
        day2: (5,10),(15,20)

Example 2:

    Input: intervals = [(4,9)]

    Output: 1

    Note: (0,8),(8,10) is not considered a conflict at 8

Constraints:

    0 <= intervals.length <= 100
    
    0 <= intervals[i].start < intervals[i].end <= 1000

Takeaway:

    Visualize the solution

    How many daysdo you need to seperate all meetings.

    You can keep track of the days needed in a single traversion

"""
class Interval(object):
    # Definition of Interval
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        # min number of days to get through meetings
        # if we have a conflict we have to have new day

        # 0                            40
        # ------------------------------
        #      5    10 
        #      -------
        #           10          15
        #            ------------

        # how many meetings are going on at the same time?

        # all start times in sorted order
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        # result is the max of count of days needed
        res, count = 0, 0

        # two pointers for both lists we made
        s, e = 0, 0

        # start will reach the end of intervals before end
        while s < len(intervals):
            if start[s] < end[e]:
                # a meeting, needs a new day
                s += 1
                count += 1
            else:
                # a meeting ended
                e += 1
                count -= 1
            # for each step, update the result 
            res = max(res, count)
        return res
