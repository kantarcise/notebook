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


# The remainder of the function definition is known as the body of the function.
# As is the case with control structures in Python, the body of a function is
# typically expressed as an indented block of code. Each time a function is called,
# Python creates a dedicated activation record that stores information relevant to the
# current call. This activation record includes what is known as a namespace 
# to manage all identifiers that have local scope within the current call.
# The namespace includes the function’s parameters and any other identifiers that are
# defined locally within the body of the function. An identifier in the local scope
# of the function caller has no relation to any identifier with the same name in the
# caller’s scope (although identifiers in different scopes may be aliases to the same
# object). In our first example, the identifier n has scope that is local to the function
# call, as does the identifier item, which is established as the loop variable.

# Return Statement

# A return statement is used within the body of a function to indicate that the function
# should immediately cease execution, and that an expressed value should be
# returned to the caller. If a return statement is executed without an explicit argument,
# the None value is automatically returned. Likewise, None will be returned if
# the flow of control ever reaches the end of a function body without having executed
# a return statement. Often, a return statement will be the final command within the
# body of the function, as was the case in our earlier example of a count function.

# However, there can be multiple return statements in the same function, with conditional
# logic controlling which such command is executed, if any. As a further
# example, consider the following function that tests if a value exists in a sequence.

def contains(data, target):
    for item in target:
        if item == target: # found a match
            return True
    return False

# If the conditional within the loop body is ever satisfied, the return True statement is
# executed and the function immediately ends, with True designating that the target
# value was found. Conversely, if the for loop reaches its conclusion without ever
# finding the match, the final return False statement will be executed.

# Information Passing

# To be a successful programmer, one must have clear understanding of the mechanism
# in which a programming language passes information to and from a function.
# In the context of a function signature, the identifiers used to describe the
# expected parameters are known as formal parameters, and the objects sent by the
# caller when invoking the function are the actual parameters. Parameter passing
# in Python follows the semantics of the standard assignment statement. When a
# function is invoked, each identifier that serves as a formal parameter is assigned, in
# the function’s local scope, to the respective actual parameter that is provided by the
# caller of the function.

# For example, consider the following call to our count function from line 8:

prizes = count(grades, A )

# Just before the function body is executed, the actual parameters, grades and A ,
# are implicitly assigned to the formal parameters, data and target, as follows:

data = grades
target = A

# The communication of a return value from the function back to the caller is
# similarly implemented as an assignment. Therefore, with our sample invocation of
# prizes = count(grades, A ), the identifier prizes in the caller’s scope is assigned
# to the object that is identified as n in the return statement within our function body.

# An advantage to Python’s mechanism for passing information to and from a
# function is that objects are not copied. This ensures that the invocation of a function
# is efficient, even in a case where a parameter or return value is a complex object.

# Mutable Parameters

# Python’s parameter passing model has additional implications when a parameter is
# a mutable object. Because the formal parameter is an alias for the actual parameter,
# the body of the function may interact with the object in ways that change its state.
# Considering again our sample invocation of the count function, if the body of the
# function executes the command data.append( F ), the new entry is added to the
# end of the list identified as data within the function, which is one and the same as
# the list known to the caller as grades. As an aside, we note that reassigning a new
# value to a formal parameter with a function body, such as by setting data = [ ],
# does not alter the actual parameter; such a reassignment simply breaks the alias.

# Our hypothetical example of a count method that appends a new element to a
# list lacks common sense. There is no reason to expect such a behavior, and it would
# be quite a poor design to have such an unexpected effect on the parameter. There
# are, however, many legitimate cases in which a function may be designed (and
# clearly documented) to modify the state of a parameter. As a concrete example,
# we present the following implementation of a method named scale that’s primary
# purpose is to multiply all entries of a numeric data set by a given factor.

def scale(data, factor):
    for j in range(len(data)):
        data[j] = factor
