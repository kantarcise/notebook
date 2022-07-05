# In this tutorial, you’ll:
#  Learn about the while loop, the Python control structure used for indefinite iteration
#  See how to break out of a loop or loop iteration prematurely
#  Explore infinite loops

n = 5
while n > 0:
     n -= 1
     print(n)
# 4
# 3
# 2
# 1
# 0

# Or with a list:

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

# baz
# bar
# foo

# break terminates the loop:

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')

# 4
# 3
# Loop ended.

# continue passes the arguments:

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# 4
# 3
# 1
# 0
# Loop ended.

#  Else Factor

while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>

# An example, loop down below is terminated prematurely with break, so the else clause isn’t executed.

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

# 4
# 3
# 2

# Quick note about searching in list:
# The list.index() method would also work. This method raises a ValueError exception
# if the item isn’t found in the list, so you need to understand exception
# handling to use it. In Python, you use a try statement to handle an exception. 

a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

try:
    print(a.index('corge'))
except ValueError:
    print(s, 'not found in list.')

# corge not found in list.

# Can nest the while loops.

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))

# foo
# > baz
# > qux
# bar
# > baz
# > qux

# If there was no (0) in pop, it would pop from the end of the list.

