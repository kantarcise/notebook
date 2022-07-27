# How functions work in Python and why they’re beneficial
# How to define and call your own Python function
# Mechanisms for passing arguments to your function
# How to return data from your function back to the calling environment

# Here is a unusual intro:

# In life, you do this sort of thing all the time, even if you don’t explicitly think of it that way. If you wanted to move 
# some shelves full of stuff from one side of your garage to the other, then you 
# hopefully wouldn’t just stand there and aimlessly think, 
# “Oh, geez. I need to move all that stuff over there! How do I do that???”
# You’d divide the job into manageable steps:

#     Take all the stuff off the shelves.
#     Take the shelves apart.
#    Carry the shelf parts across the garage to the new location.
#     Re-assemble the shelves.
#     Carry the stuff across the garage.
#     Put the stuff back on the shelves.

# Breaking a large task into smaller, bite-sized sub-tasks helps 
# make the large task easier to think about and manage. As programs become more 
# complicated, it becomes increasingly beneficial to modularize them in this way.



# The usual syntax for defining a Python function is as follows:

# def <function_name>([<parameters>]):
#     <statement(s)>

# Positional Arguments
  
# The most straightforward way to pass arguments to a Python function is with
# positional arguments (also called required arguments). In the
# function definition, you specify a comma-separated list of parameters inside the parentheses:

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

# When the function is called, you specify a corresponding list of arguments:

f(6, 'bananas', 1.74)
# 6 bananas cost $1.74

# Using keyword arguments lifts the restriction on argument order.

f(item='bananas', price=1.74, qty=6)
# 6 bananas cost $1.74

# You can give default paramaters aswell.

def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')

    

