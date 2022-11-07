# Stacks (LIFOs)

# A stack is a collection of objects that supports fast last-in, first-out
# (LIFO) semantics for inserts and deletes. Unlike lists or arrays, stacks
# typically don’t allow for random access to the objects they contain.

# The insert and delete operations are also often called push and pop.

# Stacks and queues are similar. They’re both linear collections of items,
# and the difference lies in the order that the items are accessed:
# With a queue, you remove the item least recently added (first-in, first-
# out or FIFO); but with a stack, you remove the item most recently
# added (last-in, first-out or LIFO).

# Performance-wise, a proper stack implementation is expected to take
# O(1) time for insert and delete operations.

# Stacks have a wide range of uses in algorithms, for example, in 
# language parsing and runtime memory management (“call stack”). A
# short and beautiful algorithm using a stack is depth-first search (DFS)
# on a tree or graph data structure.

# ------------------------------------------------------------------

# list – Simple, Built-In Stacks

# Python’s built-in list type makes a decent stack data structure as it
# supports push and pop operations in amortized O(1) time.
# Python’s lists are implemented as dynamic arrays internally, which
# means they occasionally need to resize the storage space for elements
# stored in them when elements are added or removed. The list over-
# allocates its backing storage so that not every push or pop requires
# resizing, and as a result, you get an amortized O(1) time complexity
# for these operations.

# The downside is that this makes their performance less consistent
# than the stable O(1) inserts and deletes provided by a linked list based
# implementation (like collections.deque, see below). On the other
# hand, lists do provide fast O(1) time random access to elements on the
# stack, and this can be an added benefit.

# Here’s an important performance caveat you should be aware of when
# using lists as stacks:

# To get the amortized O(1) performance for inserts and deletes, new
# items must be added to the end of the list with the append() method
# and removed again from the end using pop(). For optimum performance,
# stacks based on Python lists should grow towards higher indexes
# and shrink towards lower ones.

# Adding and removing from the front is much slower and takes O(n)
# time, as the existing elements must be shifted around to make room for the new element.

# This is a performance antipattern that you should avoid as much as possible.

s = []
s.append("add value first")
s.append("only thing that is needed")
s.append("simple life.")

s

# ["add value first", "only thing that is needed", "simple life"]

s.pop()
# "simple life"

s.pop()
# "only thing that is needed"

s.pop()
# "add value first"

s.pop()
# IndexError: "pop from empty list"

# ----------------------------------------------------------------------

# collections.deque – Fast & Robust Stacks

# The deque class implements a double-ended queue that supports
# adding and removing elements from either end in O(1) time (non amortized).
# Because deques support adding and removing elements
# from either end equally well, they can serve both as queues and as stacks.

# Python’s deque objects are implemented as doubly-linked lists which
# gives them excellent and consistent performance for inserting and
# deleting elements, but poor O(n) performance for randomly accessing
# elements in the middle of a stack.

# Overall, collections.deque is a great choice if you’re looking for a
# stack data structure in Python’s standard library that has the performance
# characteristics of a linked-list implementation.

from collections import deque
s = deque()
s.append('eat')
s.append('sleep')

s.append('code')

s
# deque(['eat', 'sleep', 'code'])

s.pop()
# 'code'

s.pop()
# 'sleep'

s.pop()
# 'eat'

s.pop()
# IndexError: "pop from an empty deque"

# ----------------------------------------------------------------------

# queue.LifoQueue – Locking Semantics for Parallel Computing

# This stack implementation in the Python standard library is synchronized
# and provides locking semantics to support multiple concurrent
# producers and consumers.

# Besides LifoQueue, the queue module contains several other classes
# that implement multi-producer/multi-consumer queues that are useful
# for parallel computing.

# Depending on your use case, the locking semantics might be helpful,
# or they might just incur unneeded overhead. In this case you’d be
# better off with using a list or a deque as a general-purpose stack.

from queue import LifoQueue

s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')

s
# <queue.LifoQueue object at 0x108298dd8>

s.get()
# 'code'

s.get()
# 'sleep'

s.get()
# 'eat'

s.get_nowait()
# queue.Empty

s.get()
# Blocks / waits forever...


# ----------------------------------------------------------------------

# Comparing Stack Implementations in Python

# As you’ve seen, Python ships with several implementations for a stack
# data structure. All of them have slightly different characteristics, as
# well as performance and usage trade-offs.

# If you’re not looking for parallel processing support (or don’t want to
# handle locking and unlocking manually), your choice comes down to
# the built-in list type or collections.deque. The difference lies in
# the data structure used behind the scenes and overall ease of use:

# • list is backed by a dynamic array which makes it great for fast
# random access, but requires occasional resizing when elements
# are added or removed. The list over-allocates its backing storage
# so that not every push or pop requires resizing, and you get
# an amortized O(1) time complexity for these operations. But
# you do need to be careful to only insert and remove items “from
# the right side” using append() and pop(). Otherwise, perfor-mance slows down to O(n).

# • collections.deque is backed by a doubly-linked list which optimizes
# appends and deletes at both ends and provides consistent O(1)
# performance for these operations. Not only is its performance
# more stable, the deque class is also easier to use because
# you don’t have to worry about adding or removing items from “the wrong end.”

# In summary, I believe that collections.deque is an excellent choice
# for implementing a stack (LIFO queue) in Python.

# Key Takeaways
# • Python ships with several stack implementations that have
# slightly different performance and usage characteristics.
# • collections.deque provides a safe and fast general-purpose
# stack implementation.
# • The built-in list type can be used as a stack, but be careful
# to only append and remove items with append() and pop() in
# order to avoid slow performance.



