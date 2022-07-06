# In this file:

#    You’ll start with a comparison of some different paradigms used by programming languages to implement definite iteration.
#    Then you will learn about iterables and iterators, two concepts that form the basis of definite iteration in Python.
#    Finally, you’ll tie it all together and learn about Python’s for loops.

# Python only implements collection-based iteration. 

for <var> in <iterable>:
    <statement(s)>

# <iterable> is a collection of objects—for example, a list or tuple. 
# The <statement(s)> in the loop body are denoted by indentation, as with all
# Python control structures, and are executed once for each item in <iterable>. The loop 
# variable <var> takes on the value of the next element in <iterable> each time through the loop

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

# foo
# bar
# baz

# Left at iterables.

