"""
We have n jobs, where every job is scheduled to be done 
from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the 
maximum profit you can take such that there are no two jobs in 
the subset with overlapping time range.

If you choose a job that ends at time X you will be able 
to start another job that starts at time X.

Example 1:

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 
Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104

Takeaway:

bisect provides support for maintaining a list in sorted order 
without having to sort the list after each insertion.

bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
Locate the insertion point for x in a to maintain sorted order.

bisect.insort_left(a, x, lo=0, hi=len(a), *, key=None)
Insert x in a in sorted order.

bisect.bisect(a, x, lo=0, hi=len(a), *, key=None)¶
Similar to bisect_left(), but returns an insertion point which 
comes after (to the right of) any existing entries of x in a.
"""

class Solution: 
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # from a homie
        # bottom up with bisect
        
        # zip em together in a list, so you can do a single iteration
        # zip would return a zip object..
        jobs = sorted(zip(startTime, endTime, profit))

        n = len(jobs)
        startTime.sort()
        
        # print("Jobs:", jobs)
        
        # from bottom up, 
        # make the cache
        dp = [0 for _ in range(n + 1)]
        
        # from the end of the length of jobs..
        for i in range(n - 1, -1, -1):
            
            # based on endtime of the last job
            # find the index on right for the endTime for the current element
            j = bisect.bisect_left(startTime, jobs[i][1])
            # print(j)
          
            # update memoization table
            dp[i] = max(dp[i + 1], dp[j] + jobs[i][2])
            # print(f"With {j}, dp is currently {dp}")
        # print(dp)
        # [120, 70, 70, 70, 0]
        return dp[0]
    
    
    def jobScheduling__(self, startTime, endTime, profit):
        # Explanation
        # Sort the jobs by endTime.

        # dp[time] = profit means that within the first time duration,
        # we cam make at most profit money.
        # Initial dp[0] = 0, as we make profit = 0 at time = 0.
    
        # For each job = [s, e, p], where s,e,p are its start time, end time and profit,
        # Then the logic is similar to the knapsack problem.
        # If we don't do this job, nothing will be changed.
        # If we do this job, binary search in the dp to find the largest profit we can make before start time s.
        # So we also know the maximum cuurent profit that we can make doing this job.

        # Compare with last element in the dp,
        # we make more money,
        # it worth doing this job,
        # then we add the pair of [e, cur] to the back of dp.
        # Otherwise, we'd like not to do this job.

        # Complexity
        # Time O(NlogN) for sorting
        # Time O(NlogN) for binary search for each job
        # Space O(N)

        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]] # endtime, profit
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                # if profit and found element profit 
                # is bigger than last one
                # add this end time with its profit
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
