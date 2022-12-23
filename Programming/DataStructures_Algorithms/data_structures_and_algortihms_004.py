# Functions

# We use the general term function to describe a traditional, stateless function that is 
# invoked without the context of a particular class or an instance of that class, such as
# sorted(data). We use the more specific term method to describe a member function
# that is invoked upon a specific object using an object-oriented message passing syntax, such as data.sort( )

def count(data, target):
    n = 0
    for item in data:
        if item == target: # found a match
            n += 1
    return n
 
# The first line, beginning with the keyword def, serves as the function’s signature.
# This establishes a new identifier as the name of the function (count, in this example),
# and it establishes the number of parameters that it expects, as well as names
# identifying those parameters (data and target, in this example). Unlike Java and
# C++, Python is a dynamically typed language, and therefore a Python signature
# does not designate the types of those parameters, nor the type (if any) of a return
# value. Those expectations should be stated in the function’s documentation and can
# be enforced within the body of the function, but misuse of a function will only be detected at run-time.
