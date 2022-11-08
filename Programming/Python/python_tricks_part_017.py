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

# collections.deque – Fast & Robust Queues

# The deque class implements a double-ended queue that supports
adding and removing elements from either end in O(1) time (non-
amortized). Because deques support adding and removing elements
from either end equally well, they can serve both as queues and as
stacks.35
Python’s deque objects are implemented as doubly-linked lists.36 This
gives them excellent and consistent performance for inserting and
deleting elements, but poor O(n) performance for randomly accessing
elements in the middle of the stack.
As a result, collections.deque is a great default choice if you’re look-
ing for a queue data structure in Python’s standard library.


