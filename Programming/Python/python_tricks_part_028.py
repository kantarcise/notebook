# Emulating Switch/Case Statements With Dicts

# We can do a trick you can use to emulate switch/case statements
# in Python with dictionaries and first-class functions.


if cond == 'cond_a':
    handle_a()
elif cond == 'cond_b':
    handle_b()
else:
    handle_default()

# Of course, with only three different conditions, this isn’t too horrible
# yet. But just imagine if we had ten or more elif branches in this statement.
# Things would start to look a little different. I consider long if-chains
# to be a code smell that makes programs more difficult to read and maintain.

# The idea here is to leverage the fact that Python has first-class functions.
# This means they can be passed as arguments to other functions,
# returned as values from other functions, and assigned to variables and stored in data structures.


def myfunc(a, b):
    return a + b

funcs = [myfunc]
funcs[0]
# <function myfunc at 0x107012230>

# The syntax for calling this function works as you’d intuitively expect  
# we simply use an index into the list and then use the “()” call syntax
# for calling the function and passing arguments to it:

funcs[0](2, 3)
# 5

# Now, how are we going to use first-class functions to cut our chained
# if-statement back to size? The core idea here is to define a dictionary
# that maps lookup keys for the input conditions to functions that will
# carry out the intended operations:

func_dict = { 'cond_a': handle_a,
              'cond_b': handle_b
}

# Instead of filtering through the if-statement, checking each condition
# as we go along, we can do a dictionary key lookup to get the handler
# function and then call it:

cond = 'cond_a'
func_dict[cond]()


# So let’s look for a way to support a default case that would match the
# original else branch. Luckily all Python dicts have a get() method
# on them that returns the value for a given key, or a default value if the
# key can’t be found. This is exactly what we need here:

func_dict.get(cond, handle_default)()

# Here is a complete example:

# We’re going to write another function with an if-chain that we’ll then
# transform. The function takes a string opcode like "add" or "mul" and
# then does some math on the operands x and y:

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y

dispatch_if('mul', 2, 8)
# 16
dispatch_if('unknown', 2, 8)
# None

# Please note that the 'unknown' case works because Python adds an
# implicit return None statement to the end of any function.

# So far so good. Let’s transform the original dispatch_if() into a
# new function which uses a dictionary to map opcodes to arithmetic
# operations with first-class functions.

def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

# This dictionary-based implementation gives the same results as the
# original dispatch_if(). We can call both functions in exactly the
# same way:

dispatch_dict('mul', 2, 8)
# 16
dispatch_dict('unknown', 2, 8)
# None

# Production Grade code:

# First of all, every time we call dispatch_dict(), it creates a temporary
# dictionary and a bunch of lambdas for the opcode lookup. This
# isn’t ideal from a performance perspective. For code that needs to be
# fast, it makes more sense to create the dictionary once as a constant
# and then to reference it when the function is called. We don’t want to
# recreate the dictionary every time we need to do a lookup.

# Second, if we really wanted to do some simple arithmetic like x + y,
# then we’d be better off using Python’s built-in operator module instead
# of the lambda functions used in the example. The operator
# module provides implementations for all of Python’s operators, for
# example operator.mul, operator.div, and so on. This is a minor
# point, though. I intentionally used lambdas in this example to make
# it more generic. This should help you apply the pattern in other situations as well.


# Well, now you’ve got another tool in your bag of tricks that you can
# use to simplify some of your if-chains should they get unwieldy. Just
# remember—this technique won’t apply in every situation and some-
# times you’ll be better off with a plain if-statement.

# Key Takeaways
# ••Python doesn’t have a switch/case statement. (Before 3.10 - Match Case) But in some cases
# you can avoid long if-chains with a dictionary-based dispatc table.
# Once again Python’s first-class functions prove to be a powerful
# tool. But with great power comes great responsibility.
