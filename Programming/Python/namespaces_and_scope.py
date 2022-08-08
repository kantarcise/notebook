# An assignment statement creates a symbolic name that you can use to reference an object. 
# The statement x = 'foo' creates a symbolic name x that refers to the string object 'foo'.

# In a program of any complexity, you’ll create hundreds or thousands of such names, each pointing to a specific object. 
# How does Python keep track of all these names so that they don’t interfere with one another?

# Namespaces

# In a Python program, there are four types of namespaces:

#     Built-In
#     Global
#     Enclosing
#     Local

# These have differing lifetimes. As Python executes a program, it creates namespaces as necessary and deletes them when they’re no longer needed.
