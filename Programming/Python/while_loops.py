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

