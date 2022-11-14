# Comprehending Comprehensions

# The key to understanding list comprehensions is that they’re just for loops
# over a collection but expressed in a more terse and compact syntax.

# This is sometimes referred to as syntactic sugar—a little shortcut for
# frequently used functionality that makes our lives as Python coders
# easier. Take the following list comprehension as an example:

# It computes a list of all integer square numbers from zero to nine:
squares = [x * x for x in range(10)]

squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# If you wanted to build the same list using a plain for -loop, you’d 
# probably write something like this:

squares = []
for x in range(10):
    squares.append(x * x)

# That’s a pretty straightforward loop, right? If you go back and compare
# the list comprehension example with the for-loop version, you’ll
# spot the commonalities and eventually some patterns will emerge. By
# generalizing some of the common structure here, you’ll eventually end
# up with a template similar to the one below:

values = [expression for item in collection]

# The above list comprehension “template” is equivalent to the following plain for-loop:

values = []
for item in collection:
    values.append(expression)

# Now, there’s one more useful addition we need to make to this template,
# and that is filtering elements with conditions.

# List comprehensions can filter values based on some arbitrary condition
# that decides whether or not the resulting value becomes a part of the output list. Here’s an example:

even_squares = [x * x for x in range(10) if x % 2 == 0]

# This list comprehension will compute a list of the squares of all even
# integers from zero to nine. The modulo (%) operator used here returns
# the remainder after division of one number by another. In this example,
# we use it to test if a number is even. And it has the desired result:

even_squares
# [0, 4, 16, 36, 64]

# Similar to the first example, this new list comprehension can be 
# transformed into an equivalent for-loop:

even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)
        
# Let’s try and generalize the above list comprehension to for-loop 
# transformation pattern some more. This time we’re going to add a filter
# condition to our template so we get to decide which values end up in
# the output list. Here’s the updated list comprehension template:

values = [expression for item in collection if condition]

# Again, we can transform this list comprehension into a for-loop with
# the following pattern:

values = []
for item in collection:
    if condition:
        values.append(expression)

# Once more, this was a straightforward transformation—we simply applied
# the updated cookie-cutter pattern. I hope this dispels some of
# the “magic” associated with how list comprehensions work. They’re a
# useful tool that all Python programmers should know how to use.

# Before you move on, I want to point out that Python not only supports
# list comprehensions but also has similar syntactic sugar for sets and
# dictionaries.

# Here’s what a set comprehension looks like:
  
{ x * x for x in range(-9, 10) }
# set([64, 1, 36, 0, 49, 9, 16, 81, 25, 4])

# Unlike lists, which retain the order of the elements in them, Python
# sets are an unordered collection type. So you’ll get a more or less 
# “random” order when you add items to a set container.

# And this is a dictionary comprehension:
{ x: x * x for x in range(5) }
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ----------------------------------------------------------------------------

# Key Takeaways

# • Comprehensions are a key feature in Python. Understanding
# and applying them will make your code much more Pythonic.
# • Comprehensions are just fancy syntactic sugar for a simple for-
# loop pattern. Once you understand the pattern, you’ll develop
# an intuitive understanding for comprehensions.
# • There are more than just list comprehensions.
   
