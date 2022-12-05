# So Many Ways to Merge Dictionaries

# Have you ever built a configuration system for one of your Python programs?
# A common use case for such systems is to take a data structure
# with default configuration options, and then to allow the defaults to
# be overridden selectively from user input or some other config source.

# I often found myself using dictionaries as the underlying data structure
# for representing configuration keys and values. And so I frequently
# needed a way to combine or to merge the config defaults and
# the user overrides into a single dictionary with the final configuration values.

# Or, to generalize: sometimes you need a way to merge two or more
# dictionaries into one, so that the resulting dictionary contains a combination 
# of the keys and values of the source dicts.

# In this chapter I’ll show you a couple of ways to achieve that. Let’s look
# at a simple example first so we have something to discuss. Imagine you had these two source dictionaries:

xs = {'a': 1, 'b': 2}
ys = {'b': 3, 'c': 4}

# Now, you want to create a new dict zs that contains all of the keys
# and values of xs and all of the keys and values of ys. Also, if you read
# the example closely, you saw that the string 'b' appears as a key in
# both dicts—we’ll need to think about a conflict resolution strategy for
# duplicate keys as well.

# The classical solution for the “merging multiple dictionaries” problem
# in Python is to use the built-in dictionary update() method:

zs = {}
zs.update(xs)
zs.update(ys)

# If you’re curious, a naive implementation of update() might look
# something like this. We simply iterate over all of the items of
# the right-hand side dictionary and add each key/value pair to the
# left-hand side dictionary, overwriting existing keys as we go along:

def update(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = value

# This results in a new dictionary zs which now contains the keys defined in xs and ys:

zs
# {'c': 4, 'a': 1, 'b': 3}

# You’ll also see that the order in which we call update() determines
# how conflicts are resolved. The last update wins and the duplicate
# key 'b' is associated with the value 3 that came from ys, the second source dictionary.

# Of course you could expand this chain of update() calls for as long
# as you like in order to merge any number of dictionaries into one.

# It’s a practical and well-readable solution that works in Python 2 and Python 3.

# Another technique that works in Python 2 and Python 3 uses the
# dict() built-in combined with the **-operator for “unpacking”
# objects:

zs = dict(xs, **ys)
zs
# {'a': 1, 'c': 4, 'b': 3}

# However, just like making repeated update() calls, this approach
# only works for merging two dictionaries and cannot be generalized
# to combine an arbitrary number of dictionaries in one step.

# Starting with Python 3.5, the **-operator became more flexible.4 So
# in Python 3.5+ there’s another—and arguably prettier—way to merge
# an arbitrary number of dictionaries:

zs = {**xs, **ys}

# This expression has the exact same result as a chain of update() calls.
# Keys and values are set in a left-to-right order, so we get the same
# conflict resolution strategy: the right-hand side takes priority, and
# a value in ys overrides any existing value under the same key in xs .

# This becomes clear when we look at the dictionary that results from
# the merge operation:
zs
{'c': 4, 'a': 1, 'b': 3}

# Personally, I like the terseness of this new syntax and how it still remains
# sufficiently readable. There’s always a fine balance between
# verbosity and terseness to keep the code as readable and maintainable as possible.

# In this case, I’m leaning towards using the new syntax if I’m working
# with Python 3. Using the **-operator is also faster than using chained
# update() calls, which is yet another benefit.

# Key Takeaways
# • In Python 3.5 and above you can use the **-operator to merge
# multiple dictionary objects into one with a single expression,
# overwriting existing keys left-to-right.
# • To stay compatible with older versions of Python, you might
# want to use the built-in dictionary update() method instead.
