"""
You are given an array of CPU tasks, each represented by letters 
A to Z, and a cooling time, n. 

Each cycle or interval allows the completion of one task. 

Tasks can be completed in any order, but there's a constraint: identical 
tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

Example 1:

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8
    Explanation: 
      A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

      After completing task A, you must wait two cycles before doing 
        A again. The same applies to task B. In the 3rd interval, neither 
        A nor B can be done, so you idle. By the 4th cycle, you can do 
        A again as 2 intervals have passed.

Example 2:

    Input: tasks = ["A","C","A","B","D","B"], n = 1
    Output: 6
    Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
        With a cooling interval of 1, you can repeat a task after just 
        one other task.

Example 3:

    Input: tasks = ["A","A","A", "B","B","B"], n = 3
    Output: 10
    Explanation: A possible sequence 
        is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

    There are only two types of tasks, A and B, which need to be 
      separated by 3 intervals. This leads to idling twice between 
      repetitions of these tasks.

Constraints:

    1 <= tasks.length <= 10^4
    tasks[i] is an uppercase English letter.
    0 <= n <= 100

Takeaway:

    RuntimeError: dictionary changed size during iteration

    We can use heaps and deques

"""

from collections import Counter

class Solution:
    def leastInterval__(self, tasks: List[str], n: int) -> int:
        # does not work
        
        # edge case
        if n == 0: return len(tasks)
        
        # most optimal way would be running 
        # distinct tasks if possible
        freq_map = {}
        for elem in tasks:
            freq_map[elem] = freq_map.get(elem, 0) + 1
        
        # print(freq_map)
        
        length = 0
        
        # RuntimeError: dictionary changed size during iteration
        # you cannot do that
        
        while freq_map:
            for k in freq_map:
                if freq_map[k] == 0:
                    del freq_map[k]
                    continue
                freq_map[k] -= 1
                length += 1
                
        return length
    
    def leastInterval_(self, tasks: List[str], n: int) -> int:
        # this works
        # using heaps!
        
        # we have a tasks list
        # we need to make sure that there is at least 
        # n difference between same tasks
        
        # we need to know the most frequent task
        # because it will occur first in our solution

        # we will use a max heap
        # which task is most frequent - time complexity o(log n)

        # we will also use a queue to hold the frequencies of tasks
        # and the time they will be scheduled again

        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
    
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using Counters.
        
        # edge case
        if n == 0:
            return len(tasks)

        # count the frequency of each task
        freq_map = Counter(tasks)

        # get the maximum frequency
        max_freq = max(freq_map.values())

        # count the number of tasks with the maximum frequency
        max_freq_count = sum(1 for v in freq_map.values() if v == max_freq)

        # calculate the minimum number of intervals required
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_count)
