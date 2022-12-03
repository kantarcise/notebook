# The Craziest Dict Expression in the West

# First Case
my_dict = {True: 'yes', 1: 'no', 1.0: 'maybe'}
print(my_dict)
# {True: 'maybe'}

# Well this is awkward. If you try:

# Second Case
my_dict = {"True": 'yes', 1: 'no', 1.0: 'maybe'}
print(my_dict)
# {'True': 'yes', 1: 'maybe'}

# Third Case
my_dict = {"True": 'yes', "1": 'no', 1.0: 'maybe'}
print(my_dict)
# {'True': 'yes', '1': 'no', 1.0: 'maybe'}

# While they are keywords (in Python 3), True and False are still names of objects (they are, respectively bool(1) and bool(0)).

# Lets break down the First case:


# When Python processes our dictionary expression, it first constructs
# a new empty dictionary object; and then it assigns the keys and values
# to it in the order given in the dict expression.

# Therefore, when we break it down, our dict expression is equivalent
# to this sequence of statements that are executed in order:

xs = dict()
xs[True] = 'yes'
xs[1] = 'no'
[1.0] = 'maybe'

# Oddly enough, Python considers all dictionary keys used in this example to be equal:

True == 1 == 1.0
# True

# Okay, but wait a minute here. I’m sure you can intuitively accept that
# 1.0 == 1, but why would True be considered equal to 1 as well? The
# first time I saw this dictionary expression it really stumped me.

# After doing some digging in the Python documentation, I learned that
# Python treats bool as a subclass of int. This is the case in Python 2
# and Python 3:

# “The Boolean type is a subtype of the integer type, and
# Boolean values behave like the values 0 and 1, respectively,
# in almost all contexts, the exception being that
# when converted to a string, the strings ‘False’ or ‘True’
# are returned, respectively.”

# Boolean is a SUBTYPE of the integer type!

# And yes, this means you can technically use bools as indexes into a list or tuple in Python:

['no', 'yes'][True]
# 'yes'

# But you probably should not use boolean variables like that for the
# sake of clarity (and the sanity of your colleagues.)

# Anyway, let’s come back to our dictionary expression.

# As far as Python is concerned, True, 1, and 1.0 all represent the same
# dictionary key. As the interpreter evaluates the dictionary expression,
# it repeatedly overwrites the value for the key True. This explains why,
# in the end, the resulting dictionary only contains a single key.

# Before we move on, let’s have another look at the original dictionary expression:

{True: 'yes', 1: 'no', 1.0: 'maybe'}
# {True: 'maybe'}

# Why do we still get True as the key here? Shouldn’t the key also change
# to 1.0 at the end, due to the repeated assignments?

# After some mode research in the CPython interpreter source code, I
# learned that Python’s dictionaries don’t update the key object itself
# when a new value is associated with it:

ys = {1.0: 'no'}
ys[True] = 'yes'
ys
# {1.0: 'yes'}

# Of course this makes sense as a performance optimization—if the keys
# are considered identical, then why spend time updating the original?


# In the last example you saw that the initial True object is never re-
# placed as the key. Therefore, the dictionary’s string representation
# still prints the key as True (instead of 1 or 1.0.)

# With what we know now, it looks like the values in the resulting dict
# are getting overwritten only because they compare as equal. However,
# it turns out that this effect isn’t caused by the __eq__ equality check
# alone, either.

# Python dictionaries are backed by a hash table data structure. When
# I first saw this surprising dictionary expression, my hunch was that
# this behavior had something to do with hash collisions.

# You see, a hash table internally stores the keys it contains in different
# “buckets” according to each key’s hash value. The hash value is derived
# from the key as a numeric value of a fixed length that uniquely identifies the key.

# This allows for fast lookups. It’s much quicker to search for a key’s
# numeric hash value in a lookup table instead of comparing the full
# key object against all other keys and checking for equality.

# However, the way hash values are typically calculated isn’t perfect.
# And eventually, two or more keys that are actually different will have
# the same derived hash value, and they will end up in the same lookup table bucket.

# If two keys have the same hash value, that’s called a hash collision,
# and it’s a special case that the hash table’s algorithms for inserting
# and finding elements need to handle.

# Based on that assessment, it’s fairly likely that hashing has something
# to do with the surprising result we got from our dictionary expression.
# So let’s find out if the keys’ hash values also play a role here.

# I’m defining the following class as our little detective tool:

class AlwaysEquals:
    def __eq__(self, other):
        return True
    def __hash__(self):
        return id(self)

# This class is special in two ways.
# First, because its __eq__ dunder method always returns True, all instances
# of this class will pretend they’re equal to any other object:

AlwaysEquals() == AlwaysEquals()
# True
AlwaysEquals() == 42
# True
AlwaysEquals() == 'waaat?'
# True

# And second, each AlwaysEquals instance will also return a unique
# hash value generated by the built-in id() function:

objects = [AlwaysEquals(),
           AlwaysEquals(),
           AlwaysEquals()]

[hash(obj) for obj in objects]
# [4574298968, 4574287912, 4574287072]

# In CPython, id() returns the address of the object in memory, which is guaranteed to be unique.

# With this class we can now create objects that pretend to be equal to
# any other object but have a unique hash value associated with them.
# That’ll allow us to test if dictionary keys are overwritten based on their
# equality comparison result alone.

# And, as you can see, the keys in the next example are not getting over-
# written, even though they always compare as equal:

{AlwaysEquals(): 'yes', AlwaysEquals(): 'no'}
# { <AlwaysEquals object at 0x110a3c588>: 'yes',
# <AlwaysEquals object at 0x110a3cf98>: 'no' }

# We can also flip this idea around and check to see if returning the same
# hash value is enough to cause keys to get overwritten:

class SameHash:
    def __hash__(self):
        return 1

# Instances of this SameHash class will compare as non-equal with each
# other but they will all share the same hash value of 1:

a = SameHash()
b = SameHash()
a == b
# False

hash(a), hash(b)
# (1, 1)
# Let’s look at how Python’s dictionaries react when we attempt to use
# instances of the SameHash class as dictionary keys:

{a: 'a', b: 'b'}
# { <SameHash instance at 0x7f7159020cb0>: 'a',
# <SameHash instance at 0x7f7159020cf8>: 'b' }

# As this example shows, the “keys get overwritten” effect isn’t caused
# by hash value collisions alone either.

# Dictionaries check for equality and compare the hash value to determine
# if two keys are the same. Let’s try and summarize the findings
# of our investigation:

# The {True: 'yes', 1: 'no', 1.0: 'maybe'} dictionary expres-
# sion evaluates to {True: 'maybe'} because the keys True, 1, and
# 1.0 all compare as equal, and they all have the same hash value:

True == 1 == 1.0
# True
(hash(True), hash(1), hash(1.0))
# (1, 1, 1)

# Perhaps not-so-surprising anymore, that’s how we ended up with this
# result as the dictionary’s final state:

{True: 'yes', 1: 'no', 1.0: 'maybe'}
# {True: 'maybe'}

# We touched on a lot of subjects here, and this particular Python Trick
# can be be a bit mind-boggling at first—that’s why I compared it to a
# Zen kōan in the beginning.

# If it’s difficult to understand what’s going on in this chapter, try playing
# through the code examples one by one in a Python interpreter session.
# You’ll be rewarded with an expanded knowledge of Python’s internals.

# Key Takeaways
# • Dictionaries treat keys as identical if their __eq__ comparison
# result says they’re equal and their hash values are the same.
# • Unexpected dictionary key collisions can and will lead to surprising results.
