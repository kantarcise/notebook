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
        
# Default Paramater Values 

# Python provides means for functions to support more than one possible calling
# signature. Such a function is said to be polymorphic (which is Greek for “many
# forms”). Most notably, functions can declare one or more default values for parameters,
# thereby allowing the caller to invoke a function with varying numbers of
# actual parameters. As an artificial example, if a function is declared with signature

def foo(a, b=15, c=27):

# There are three parameters, the last two of which offer default values. A caller is
# welcome to send three actual parameters, as in foo(4, 12, 8), in which case the default
# values are not used. If, on the other hand, the caller only sends one parameter,
# foo(4), the function will execute with parameters values a=4, b=15, c=27. If a
# caller sends two parameters, they are assumed to be the first two, with the third being
# the default. Thus, foo(8, 20) executes with a=8, b=20, c=27. However, it is
# illegal to define a function with a signature such as bar(a, b=15, c) with b having
# a default value, yet not the subsequent c; if a default parameter value is present for
# one parameter, it must be present for all further parameters.

# As a more motivating example for the use of a default parameter, we revisit
# the task of computing a student’s GPA (see Code Fragment 1.1). Rather than assume
# direct input and output with the console, we prefer to design a function that
# computes and returns a GPA. Our original implementation uses a fixed mapping
# from each letter grade (such as a B−) to a corresponding point value (such as
# 2.67). While that point system is somewhat common, it may not agree with the
# system used by all schools. (For example, some may assign an A+ grade a value
# higher than 4.0.) Therefore, we design a compute gpa function, given in Code
# Fragment 1.2, which allows the caller to specify a custom mapping from grades to
# values, while offering the standard point system as a default.

def compute gpa(grades, points={ A+ :4.0, A :4.0, A- :3.67, B+ :3.33,
                                 B :3.0, B- :2.67, C+ :2.33, C :2.0,
                                 C :1.67, D+ :1.33, D :1.0, F :0.0}):
    num courses = 0
    total points = 0
    for g in grades:
        if g in points: # a recognizable grade
            num courses += 1
            total points += points[g]   
    return total points / num courses

# As an additional example of an interesting polymorphic function, we consider
# Python’s support for range. (Technically, this is a constructor for the range class,
# but for the sake of this discussion, we can treat it as a pure function.) Three calling
# syntaxes are supported. The one-parameter form, range(n), generates a sequence of
# integers from 0 up to but not including n. A two-parameter form, range(start,stop)
# generates integers from start up to, but not including, stop. A three-parameter
# form, range(start, stop, step), generates a similar range as range(start, stop), but
# with increments of size step rather than 1.

# This combination of forms seems to violate the rules for default parameters.
# In particular, when a single parameter is sent, as in range(n), it serves as the stop
# value (which is the second parameter); the value of start is effectively 0 in that
# case. However, this effect can be achieved with some sleight of hand, as follows:

def range(start, stop=None, step=1):
    if stop is None:
        stop = start
    start = 0
    ...

# From a technical perspective, when range(n) is invoked, the actual parameter n will
# be assigned to formal parameter start. Within the body, if only one parameter is
# received, the start and stop values are reassigned to provide the desired semantics.
