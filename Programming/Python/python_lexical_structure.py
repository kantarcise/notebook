# Excessively long lines of code are generally considered poor practice. 
# In fact, there is an official Style Guide for Python Code put forth by the Python Software Foundation, and one of 
# its stipulations is that the maximum line length in Python code should be 79 characters.

# Implicit Line Continuation

# This is the more straightforward technique for line continuation, and the one that is preferred according to PEP 8.

a = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# If you need to continue a statement across multiple lines, it is usually 
# possible to use implicit line continuation to do so. This is because parentheses, brackets, and
# curly braces appear so frequently in Python syntax.

a = [
    'foo', 'bar', 'string', 'another', 'and', 'one',  
    'more', 'baz', 'qux', 'some', 'folks', 'do', 'that'
]

# To indicate explicit line continuation, you can specify a backslash (\) character as the final character on the line.

x = 1 + 2 \
    + 3 + 4 \
    + 5 + 6

x
# 21

# Comment your code. Just do it.

# Calculate and display the area of a circle.
pi = 3.1415926536
r = 12.35
area = pi * (r ** 2)

print('The area of a circle with radius', r, 'is', area)
# The area of a circle with radius 12.35 is 479.163565508706

"""
You can use this
method for commenting code.
The triple-quotes
"""

# The earliest versions of Fortran, one of the first programming languages created, 
# were designed so that all whitespace was completely ignored.
# But most modern languages are not following this path to become much more readable.

'qux' not in ['foo', 'bar', 'baz']
# True

'qux' notin ['foo', 'bar', 'baz']
# SyntaxError: invalid syntax


