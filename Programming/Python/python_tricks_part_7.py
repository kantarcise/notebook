# Defining Your Own Exception Classes

# When I started using Python, I was hesitant to write custom exception
# classes in my code. But defining your own error types can be of great
# value. You’ll make potential error cases stand out clearly, and as a
# result, your functions and modules will become more maintainable.

# You can also use custom error types to provide additional debugging information.

def validate(name):
    if len(name) < 10:
        raise ValueError

# When a name fails to validate, it'll look like this ins the debug stack.

validate('joe')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#     validate('joe')
#   File "<input>", line 3, in validate
#     raise ValueError
# ValueError

# This is not really helpful.







# Defining your own exception types will state your code’s intent more clearly and make it easier to debug.
