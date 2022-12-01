# Sorting Dictionaries for Fun and Profit

# Python dictionaries don’t have an inherent order.

# Let's try to sort them.
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

# To get a sorted list of the key/value pairs in this dictionary, you could
# use the dictionary’s items() method and then sort the resulting sequence in a second pass:

sorted(xs.items())
# [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

# The key/value tuples are ordered using Python’s standard lexico graphical ordering for comparing sequences.

# To compare two tuples, Python compares the items stored at index
# zero first. If they differ, this defines the outcome of the comparison.
# If they’re equal, the next two items at index one are compared, and so on.

# Now, because we took these tuples from a dictionary, all of the former
# dictionary keys at index zero in each tuple are unique. Therefore,
# there are no ties to break here.

# In some cases a lexicographical ordering might be exactly what you want.
# In other cases you might want to sort a dictionary by value instead.

# Luckily, there’s a way you can get complete control over how items
# are ordered. You can control the ordering by passing a key func to
# sorted() that will change how dictionary items are compared.

# Key function !! 

# A key func is simply a normal Python function to be called on each
# element prior to making comparisons. The key func gets a dictionary
# item as its input and returns the desired “key” for the sort order comparisons.

# Unfortunately, the word “key” is used in two contexts simultaneously
# here—the key func doesn’t deal with dictionary keys, it merely maps
# each input item to an arbitrary comparison key.

# Let’s say you wanted to get a sorted representation of a dictionary
# based on its values. To get this result you could use the following key
# func which returns the value of each key/value pair by looking up the
# second element in the tuple:

sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# See how the resulting list of key/value pairs is now sorted by the values
# stored in the original dictionary? It’s worth spending some time
# wrapping your head around how key funcs work. It’s a powerful concept
# that you can apply in all kinds of Python contexts.

# In fact, the concept is so common that Python’s standard library includes
# the operator module. This module implements some of the most frequently used
# key funcs as plug-and-play building blocks, like operator.itemgetter and operator.attrgetter.

# Here’s an example of how you might replace the lambda-based index
# lookup in the first example with operator.itemgetter:

import operator
sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Using the operator module might communicate your code’s intent
# more clearly in some cases. On the other hand, using a simple lambda
# expression might be just as readable and more explicit. In this particular case,
# I actually prefer the lambda expression.

# Another benefit of using lambdas as a custom key func is that you get
# to control the sort order in much finer detail. For example, you could
# sort a dictionary based on the absolute numeric value of each value stored in it:

sorted(xs.items(), key=lambda x: abs(x[1]))

# If you need to reverse the sort order so that larger values go first, you
# can use the reverse=True keyword argument when calling sorted():

sorted(xs.items(),
      key=lambda x: x[1],
      reverse=True)

# [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

# Like I said earlier, it’s totally worth spending some time getting a good
# grip on how key funcs work in Python. They provide you with a ton of
# flexibility and can often save you from writing code to transform one
# data structure into another.

# Key Takeaways
# • When creating sorted “views” of dictionaries and other collections,
# you can influence the sort order with a key func.

# • Key funcs are an important concept in Python. The most frequently
# used ones were even added to the operator module in the standard library.
# • Functions are first-class citizens in Python. This is a powerful
# feature you’ll find used everywhere in the language.
