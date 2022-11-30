# Comprehending Comprehensions

# You should use list comprehensions, they are awesome.

even_squares = [x * x for x in range(10)
               if x % 2 == 0]

# Generally
values = [expression for item in collection if condition]

# Python not only supports list comprehensions but
# also has similar syntactic sugar for sets and dictionaries.

{ x * x for x in range(-9, 10) }
# set([64, 1, 36, 0, 49, 9, 16, 81, 25, 4])

{ x: x * x for x in range(5) }
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Key Takeaways
# • Comprehensions are a key feature in Python. Understanding
# and applying them will make your code much more Pythonic.
# • Comprehensions are just fancy syntactic sugar for a simple for-
# loop pattern. Once you understand the pattern, you’ll develop
# an intuitive understanding for comprehensions.
# • There are more than just list comprehensions.

# List Slicing Tricks and the Sushi Operator

lst = [1, 2, 3, 4, 5]
lst
# [1, 2, 3, 4, 5]

lst[start:end:step]
lst[1:3:1]
# [2, 3]

# If you leave out the step size, it defaults to one:
lst[1:3]
# [2, 3]

# If you ask for a [::-1] slice, you’ll get a copy of the original list, but in the reverse order:
numbers[::-1]
# [5, 4, 3, 2, 1]

# Here’s another list-slicing trick: You can use the :-operator to clear
# all elements from a list without destroying the list object itself.
# This is extremely helpful when you need to clear out a list in your program
# that has other references pointing to it. In this case, you often
# can’t just empty the list by replacing it with a new list object, since
# that wouldn’t update the other references. But here’s the sushi operator coming to your rescue:

lst = [1, 2, 3, 4, 5]
del lst[:]
lst
[]

original_lst = lst
lst[:] = [7, 8, 9]
lst
# [7, 8, 9]
original_lst
# [7, 8, 9]
original_lst is lst
# True

# Yet another use case for the sushi operator is creating (shallow) copies of existing lists:
copied_lst = lst[:]
copied_lst
# [7, 8, 9]
copied_lst is lst
# False

# Creating a shallow copy means that only the structure of the elements
# is copied, not the elements themselves. Both copies of the list share
# the same instances of the individual elements.


# Key Takeaways
# • The : “sushi operator” is not only useful for selecting sublists
# of elements within a list. It can also be used to clear, reverse,
# and copy lists.
# • But be careful—this functionality borders on the arcane for
# many Python developers. Using it might make your code less
# maintainable for everyone else on your team.
