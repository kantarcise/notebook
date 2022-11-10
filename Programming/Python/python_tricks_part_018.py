# Priority Queues

# A priority queue is a container data structure that manages a set of
# records with totally-ordered39 keys (for example, a numeric weight
# value) to provide quick access to the record with the smallest or largest key in the set.

# You can think of a priority queue as a modified queue: instead of 
# retrieving the next element by insertion time, it retrieves the highest-
# priority element. The priority of individual elements is decided by
# the ordering applied to their keys.

# Priority queues are commonly used for dealing with scheduling problems,
# for example, to give precedence to tasks with higher urgency.

# Think about the job of an operating system task scheduler:
# Ideally, high-priority tasks on the system (e.g., playing
# a real-time game) should take precedence over
# lower-priority tasks (e.g., downloading updates in the
# background). By organizing pending tasks in a priority
# queue that uses the task urgency as the key, the task
# scheduler can quickly select the highest-priority tasks
# and allow them to run first.

# -----------------------------------------------

# list – Maintaining a Manually Sorted Queue
# You can use a sorted list to quickly identify and delete the smallest
# or largest element. The downside is that inserting new elements into
# a list is a slow O(n) operation.

# While the insertion point can be found in O(log n) time using
# bisect.insort in the standard library, this is always dominated
# by the slow insertion step.

# Maintaining the order by appending to the list and re-sorting also
# takes at least O(n log n) time. Another downside is that you must manually
# take care of re-sorting the list when new elements are inserted.

# It’s easy to introduce bugs by missing this step, and the burden is always on you, the developer.
# Therefore, I believe that sorted lists are only suitable as priority queues when there will be few insertions.

q = []

q.append((2,'code'))
q.append((1,'eat'))
q.append((3,'sleep'))


# NOTE: Remember to re-sort every time
#  a new element is inserted, or use
#  bisect.insort().

q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)

# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')

# -----------------------------------------------
  
# heapq – List-Based Binary Heaps

# This is a binary heap implementation usually backed by a plain list,
# and it supports insertion and extraction of the smallest element in
# O(log n) time.

# This module is a good choice for implementing priority queues in
# Python. Since heapq technically only provides a min-heap implementation
# extra steps must be taken to ensure sort stability and other
# features typically expected from a “practical” priority queue.

import heapq

q = []

heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    print(next_item)

# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')

# -----------------------------------------------

# queue.PriorityQueue – Beautiful Priority Queues
# This priority queue implementation uses heapq internally and shares
# the same time and space complexities.

# The difference is that PriorityQueue is synchronized and provides
# locking semantics to support multiple concurrent producers and consumers.

# Depending on your use case, this might be helpful—or just slow your
# program down slightly. In any case, you might prefer the class-based
# interface provided by PriorityQueue over using the function-based
# interface provided by heapq.

from queue import PriorityQueue
q = PriorityQueue()

q.put((2,'code'))
q.put((1,'eat'))
q.put((3,'sleep'))


while not q.empty():
    next_item = q.get()
    print(next_item)

# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')

# Key Takeaways
# • Python includes several priority queue implementations for you to use.
# • queue.PriorityQueue stands out from the pack with a nice
# object-oriented interface and a name that clearly states its intent.
# It should be your preferred choice.
# • If you’d like to avoid the locking overhead of queue.PriorityQueue,
# using the heapq module directly is also a good option.
