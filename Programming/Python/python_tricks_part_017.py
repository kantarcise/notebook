#  Queues (FIFOs)

# In this chapter you’ll see how to implement a FIFO queue data structure
# using only built-in data types and classes from the Python standard
# library. But first, let’s recap what a queue is:

# A queue is a collection of objects that supports fast first-in, first-out
# (FIFO) semantics for inserts and deletes. The insert and delete operations
# are sometimes called enqueue and dequeue. Unlike lists or arrays, queues
# typically don’t allow for random access to the objects they contain.

# With a queue, you remove the item least recently added (first-in, first-
# out or FIFO); but with a stack, you remove the item most recently
# added (last-in, first-out or LIFO).

# Performance-wise, a proper queue implementation is expected to take
# O(1) time for insert and delete operations. These are the two main
# operations performed on a queue, and in a correct implementation,
# they should be fast.

# list — Terribly Sloooow Queues

# It’s possible to use a regular list as a queue but this is not ideal from
# a performance perspective.34 Lists are quite slow for this purpose because
# inserting or deleting an element at the beginning requires shifting
# all of the other elements by one, requiring O(n) time.

q = []
q.append('eat')
q.append('sleep')
q.append('code')
q
# ['eat', 'sleep', 'code']

# Careful: This is slow!
q.pop(0)
'eat'

# --------------------------------------------------------------

# collections.deque – Fast & Robust Queues

# The deque class implements a double-ended queue that supports
# adding and removing elements from either end in O(1) time (non amortized).
# Because deques support adding and removing elements
# from either end equally well, they can serve both as queues and a stacks.

# Python’s deque objects are implemented as doubly-linked lists.36 This
# gives them excellent and consistent performance for inserting and
# deleting elements, but poor O(n) performance for randomly accessing
# elements in the middle of the stack.

# As a result, collections.deque is a great default choice if you’re looking
# for a queue data structure in Python’s standard library.

from collections import deque
q = deque()
q.append('eat')
q.append('sleep')

q.append('code')
q
# deque(['eat', 'sleep', 'code'])

q.popleft()
# 'eat'

q.popleft()
# 'sleep'
q.popleft()
# 'code'
q.popleft()
# IndexError: "pop from an empty deque"

# --------------------------------------------------------------------

# queue.Queue – Locking Semantics for Parallel Computing

# This queue implementation in the Python standard library is synchronized
# and provides locking semantics to support multiple concurrent producers and consumers.

# The queue module contains several other classes implementing multi-
# producer/multi-consumer queues that are useful for parallel computing.

# Depending on your use case, the locking semantics might be helpful or
# just incur unneeded overhead. In this case, you’d be better off using
# collections.deque as a general-purpose queue.

from queue import Queue

q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')

q
# <queue.Queue object at 0x1070f5b38>

q.get()
# 'eat'

q.get()
# 'sleep'

q.get()
# 'code'

q.get_nowait()
# queue.Empty

q.get()
# Blocks / waits forever...

# --------------------------------------------------------------------

# multiprocessing.Queue – Shared Job Queues

# This is a shared job queue implementation that allows queued items
# to be processed in parallel by multiple concurrent workers.38 Process-
# based parallelization is popular in CPython due to the global inter-
# preter lock (GIL) that prevents some forms of parallel execution on a
# single interpreter process.

# As a specialized queue implementation meant for sharing data
# between processes, multiprocessing.Queue makes it easy to distribute
# work across multiple processes in order to work around
# the GIL limitations. This type of queue can store and transfer any
# pickle-able object across process boundaries.

from multiprocessing import Queue
q = Queue()
q.put('eat')
q.put('sleep')

q.put('code')

q
# <multiprocessing.queues.Queue object at 0x1081c12b0>
q.get()
# 'eat'
q.get()
# 'sleep'
q.get()
# 'code'

q.get()
# Blocks / waits forever...

# --------------------------------------------------------------------

# Key Takeaways
# • Python includes several queue implementations as part of the
# core language and its standard library.
# • list objects can be used as queues, but this is generally not
# recommended due to slow performance.
# • If you’re not looking for parallel processing support, the implementation
#  offered by collections.deque is an excellent default choice
# for implementing a FIFO queue data structure in Python.
# It provides the performance characteristics you’d expect
# from a good queue implementation and can also be used as a stack (LIFO Queue).
