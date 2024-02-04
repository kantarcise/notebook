"""
You are given a 2D integer array intervals, where 
intervals[i] = [lefti, righti] describes the ith interval 
starting at lefti and ending at righti (inclusive). 
The size of an interval is defined as the number of 
integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to 
the jth query is the size of the smallest interval i such 
that lefti <= queries[j] <= righti. If no such interval 
exists, the answer is -1.

Return an array containing the answers to the queries.

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]

Explanation: The queries are processed as follows:
    - Query = 2: The interval [2,4] is the smallest 
        interval containing 2. The answer is 4 - 2 + 1 = 3.
    
    - Query = 3: The interval [2,4] is the smallest 
        interval containing 3. The answer is 4 - 2 + 1 = 3.
    
    - Query = 4: The interval [4,4] is the smallest 
        interval containing 4. The answer is 4 - 4 + 1 = 1.
    
    - Query = 5: The interval [3,6] is the smallest 
        interval containing 5. The answer is 6 - 3 + 1 = 4.

    
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]

Explanation: The queries are processed as follows:
    - Query = 2: The interval [2,3] is the smallest 
        interval containing 2. The answer is 3 - 2 + 1 = 2.
    
    - Query = 19: None of the intervals contain 19. 
        The answer is -1.
    
    - Query = 5: The interval [2,5] is the smallest 
        interval containing 5. The answer is 5 - 2 + 1 = 4.
    
    - Query = 22: The interval [20,25] is the smallest 
    interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:

    1 <= intervals.length <= 105
    1 <= queries.length <= 105
    intervals[i].length == 2
    1 <= lefti <= righti <= 107
    1 <= queries[j] <= 107

Takeaway:

Brute Force exceeds time limit.

We Obviously need sorting.

sort based on second val - l.sort(key = lambda x : x[1])

We will also use a min_heap to add/remove the intervals

"""

from heapq import heappop, heappush

class Solution:
    def minInterval_(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # simple 
        # TIME LIMIT EXCEEDED
        intervals.sort()
        
        result = []
        for elem in queries:
            # Initialize min_size to positive infinity
            min_size = float('inf')  
            for interval in intervals:
                if interval[0] <= elem <= interval[1]:
                    current_size = interval[1] - interval[0] + 1
                    min_size = min(current_size, min_size)
            
            if min_size == float("inf"):
                result.append(-1)
            else:
                result.append(min_size) # if min_size == float("inf") else -1
        
        return result
    
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # Is there a way to order the intervals and queries 
        # such that it takes less time to query?
        
        # Is there a way to add and remove intervals
        # by going from the smallest query to the largest 
        # query to find the minimum size?
        
        # we will sort bot intervals and queries,
        # we will use a min heap
        
        # bruteforce is o(m*q) we will get to o(mlogm * q*logq)
        
        # we will sort intervals based on left value
        
        # Intervals
        #  
        # 
        #             |-----------|
        #         |-------|
        #     |-----------|
        #                 |
        # ----------------------------------
        # 0   1   2   3   4   5   6   7   8
        #         x   x   x   x
        # 
        # Queries
        
        # min_heap
        # (4, 4), (3, 4), (4, 6), (1, 4)
        
        # result
        # [3, 3, 1, ]
        
        # while and intervals left value is less then or equal 
        # to the value of query, 
        # we will add that interval our min_heap
        
        # the tiebreaker for the intervals should be the right value
        # we want to drop leftmost intervals as we go from
        # left to right
        
        # min_heap elements - (size, right_value)
        
        # if right value is smaller than query, pop from min_heap
        
        intervals.sort()
        
        min_heap = []
        # i is beginning of the intervals index, 0
        res, i = {}, 0
        
        # because we will need the original
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                # keep adding intervals to min_heap
                l, r = intervals[i]
                heappush(min_heap, (r - l + 1, r))
                i += 1
                
            while min_heap and min_heap[0][1] < q:
                # if right value of interval is less than query value
                # pop it!
                heappop(min_heap)
                
            # size of the interval if we have an element in our heap
            res[q] = min_heap[0][0] if min_heap else -1
            
        # we have to return the result such that
        # it matches the original order of the queries
        return [res[q] for q in queries]                