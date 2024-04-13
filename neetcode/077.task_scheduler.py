"""
Given a characters array tasks, representing the tasks a CPU needs 
to do, where each letter represents a different task. 

Tasks could be done in any order. 

Each task is done in one unit of time. 

For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown 
period between two same tasks (the same letter in the array), that is 
that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will 
take to finish all the given tasks.

Example 1:

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    
    Output: 8
    
    Explanation: 
        
        A -> B -> idle -> A -> B -> idle -> A -> B
        There is at least 2 units of time between any two same tasks.

Example 2:

    Input: tasks = ["A","A","A","B","B","B"], n = 0

    Output: 6

    Explanation: 
    
        On this case any permutation of size 6 would 
            work since n = 0.
        
        ["A","A","A","B","B","B"]
        ["A","B","A","B","A","B"]
        ["B","B","B","A","A","A"]
        ...
        And so on.

Example 3:

    Input: tasks = ["A","A","A","A","A","A","B",
        "C","D","E","F","G"], n = 2
    
    Output: 16
    
    Explanation: 
        
        One possible solution is
        A -> B -> C -> A -> D -> E -> A -> F -> G 
            -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:

    1 <= task.length <= 10^4

    tasks[i] is upper-case English letter.
    
    The integer n is in the range [0, 100].

Takeaway:

    we have a tasks list
    we need to make sure that there is at least 
    n difference between same tasks

    we need to know the most frequent task
    because it will occur first in our solution

    we will use a max heap
    whichch task is most frequent - time complexity o(log n)

    we will also use a queue to hold the frequencies of tasks
    and the time they will be scheduled again
"""

from collections import Counter, deque
import heapq

class Solution:

    def leastInterval__(self, tasks: "list[int]", n: int) -> int:
        # does not work
        
        # edge case
        if n == 0: return len(tasks)
        
        # most optimal way would be running 
        # distinct tasks if possible
        freq_map = {}
        for elem in tasks:
            freq_map[elem] = freq_map.get(elem, 0) + 1
        
        print(freq_map)
        
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

    def leastInterval_(self, tasks: "list[int]", n: int) -> int:
        
        # we have a tasks list
        # we need to make sure that there is at least 
        # n difference between same tasks
        
        # we need to know the most frequent task
        # because it will occur first in our solution

        # we will use a max heap
        # whichch task is most frequent - time complexity o(log n)

        # we will also use a queue to hold the frequencies of tasks
        # and the time they will be scheduled again

        # count the occurrences of each task
        count = Counter(tasks)
        
        # Create a max heap to store negative task 
        # counts (most frequent tasks first)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        # Initialize time to keep track of the current time
        time = 0
        
        # Create a queue to hold frequencies of 
        # tasks and the time they will be scheduled again
        q = deque()

        # Main loop
        while max_heap or q:
            time += 1

            if max_heap:
                # Retrieve the most frequent task and 
                # update its count
                cnt = 1 + heapq.heappop(max_heap)
                
                # If the count is not zero, schedule it for later
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                # Check if a task is scheduled to be 
                # executed at the current time
                heapq.heappush(max_heap, q.popleft()[0])

        # Return the total time taken to complete 
        # the tasks with intervals
        return time

    def leastInterval(self, tasks: "list[int]", n: int) -> int:
        # much smaller code in size

        # edge case
        if n == 0:
            return len(tasks)

        # Get the count of each task using Counter and
        #  store them in a list
        counts = list(Counter(tasks).values())
        
        # Find the maximum count, i.e., the most repeated task
        most_repeats = max(counts)
        
        # Count how many tasks have the maximum count
        num_longest = counts.count(most_repeats)
        
        # Calculate the minimum time required to 
        # complete the tasks
        # 
        # This is based on the maximum count and the
        # cooling interval (n)
        # 
        # If there are gaps between the most repeated 
        # tasks, consider them
        # 
        # Otherwise, return the length of the tasks list
        return max(len(tasks), (most_repeats-1) * (n+1) + num_longest)
