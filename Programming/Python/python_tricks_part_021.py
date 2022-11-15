# List Slicing Tricks and the Sushi Operator

# Python’s list objects have a neat feature called slicing. You can view
# it as an extension of the square-brackets indexing syntax. Slicing is
# commonly used to access ranges of elements within an ordered collection.
# For example, you can slice up a large list object into several smaller sublists with it.

# Here’s an example with “[start:stop:step]” pattern:

lst = [1, 2, 3, 4, 5]
lst
# [1, 2, 3, 4, 5]

# lst[start:end:step]
lst[1:3:1]
# [2, 3]

# Adding the [1:3:1] index returned a slice of the original list ranging
# from index 1 to index 2, with a step size of one element. To avoid
# off-by-one errors, it’s important to remember that the upper bound is
# always exclusive. This is why we got [2, 3] as the sublist from the
# [1:3:1] slice.

# If you leave out the step size, it defaults to one:
lst[1:3]
# [2,3]

# You can do other interesting things with the step parameter, also
# called the stride. For example, you can create a sublist that includes
# every other element of the original:

lst[::2]
# [1, 3, 5]

# Wasn’t that fun? I like to call “:” the sushi operator. It looks like a 
# delicious maki roll cut in half. Besides reminding you of delicious food
# and accessing ranges of lists, it has a few more lesser-known applications.

# Let me show you some more fun and useful list-slicing tricks!
# You just saw how the slicing step size can be used to select every other
# element of a list. Well, there’s more: If you ask for a [::-1] slice,
# you’ll get a copy of the original list, but in the reverse order:
 
numbers[::-1]
# [5, 4, 3, 2, 1]

# We asked Python to give us the full list (::), but to go over all of the
# elements from back to front by setting the step size to -1. This is pretty
# neat, but in most cases I’d still stick with list.reverse() and the
# built-in reversed() function to reverse a list.

# list.reverse !!

# Here’s another list-slicing trick: You can use the :-operator to clear
# all elements from a list without destroying the list object itself.
# This is extremely helpful when you need to clear out a list in your program 
# that has other references pointing to it. In this case, you often
# can’t just empty the list by replacing it with a new list object, since
# that wouldn’t update the other references. But here’s the sushi operator
# coming to your rescue:

lst = [1, 2, 3, 4, 5]
del lst[:]
lst
[]

# As you can see, this removes all elements from lst but leaves the list
# object itself intact. In Python 3 you can also use lst.clear() for the
# same job, which might be the more readable pattern, depending on
# the circumstances. However, keep in mind that clear() isn’t available in Python 2.

# Besides clearing lists, you can also use slicing to replace all elements
# of a list without creating a new list object. This is a nice shorthand for
# clearing a list and then repopulating it manually:

original_lst = lst
lst[:] = [7, 8, 9]

lst
# [7, 8, 9]
original_lst
# [7, 8, 9]
original_lst is lst
# True

# The previous code example replaced all elements in lst but did not
# destroy and recreate the list itself. The old references to the original
# list object are therefore still valid.
# Yet another use case for the sushi operator is creating (shallow) copies
# of existing lists:

copied_lst = lst[:]
copied_lst
# [7, 8, 9]
copied_lst is lst
# False

# Creating a shallow copy means that only the structure of the elements
# is copied, not the elements themselves. Both copies of the list share
# the same instances of the individual elements.

# If you need to duplicate everything, including the elements, then you’ll
# need to create a deep copy of the list. Python’s built-in copy module
# will come in handy for this.

# Key Takeaways

# • The : “sushi operator” is not only useful for selecting sublists
# of elements within a list. It can also be used to clear, reverse and copy lists.

# • But be careful—this functionality borders on the arcane for
# many Python developers. Using it might make your code less
# maintainable for everyone else on your team.
