# Effective Functions

# Python’s Functions Are First-Class

# What is that mean ?

# Python’s functions are first-class objects. You can assign them to variables,
# store them in data structures, pass them as arguments to other
# functions, and even return them as values from other functions.

def yell(text):
    return text.upper() + '!'

yell('hello')
# 'HELLO!'

bark = yell

bark("woof")
# "WOOF!"

del yell

yell("hello?")
# NameError: "name 'yell' is not defined"

bark("hey")
# "HEY!"

bark.__name__
# "yell"

# Since functions are first-class citizens, you can store them in data
# structures, just like you can with other objects. For example, you can
# add functions to a list:

funcs = [bark, str.lower, str.capitalize]

funcs
# [<function yell at 0x10ff96510>,
#  <method 'lower' of 'str' objects>,
#  <method 'capitalize' of 'str' objects>]


# This is weird but you can even do:

funcs[0]("heyho")
#"HEYHO!"


