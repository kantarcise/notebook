# Additional Python Conveniences
# In this section, we introduce several features of Python that are particularly convenient
# for writing clean, concise code. Each of these syntaxes provide functionality
# that could otherwise be accomplished using functionality that we have introduced
# earlier in this chapter. However, at times, the new syntax is a more clear and direct
# expression of the logic.

# 1.9.1 Conditional Expressions
# Python supports a conditional expression syntax that can replace a simple control
# structure. The general syntax is an expression of the form:

expr1 if condition else expr2

# This compound expression evaluates to expr1 if the condition is true, and otherwise
# evaluates to expr2. For those familiar with Java or C++, this is equivalent to the
# syntax, condition ? expr1 : expr2, in those languages.

# As an example, consider the goal of sending the absolute value of a variable, n,
# to a function (and without relying on the built-in abs function, for the sake of example).
# Using a traditional control structure, we might accomplish this as follows:

if n >= 0:
    param = n
else:
    param = −n
result = foo(param) # call the function

# With the conditional expression syntax, we can directly assign a value to variable,
# param, as follows:

param = n if n >= 0 else n * -1 # pick the appropriate value
result = foo(param) # call the function

# In fact, there is no need to assign the compound expression to a variable. A conditional
# expression can itself serve as a parameter to the function, written as follows:

result = foo(n if n >= 0 else n * -1)

# Sometimes, the mere shortening of source code is advantageous because it
# avoids the distraction of a more cumbersome control structure. However, we recommend
# that a conditional expression be used only when it improves the readability
# of the source code, and when the first of the two options is the more “natural” case,
# given its prominence in the syntax. (We prefer to view the alternative value as more
# exceptional.)

# 1.9.2 Comprehension Syntax

# A very common programming task is to produce one series of values based upon
# the processing of another series. Often, this task can be accomplished quite simply
# in Python using what is known as a comprehension syntax. We begin by demon-
# strating list comprehension, as this was the first form to be supported by Python.
# Its general form is as follows:

[ expression for value in iterable if condition ]

# We note that both expression and condition may depend on value, and that the
# if-clause is optional. The evaluation of the comprehension is logically equivalent
# to the following traditional control structure for computing a resulting list:

result = []

for value in iterable:
    if condition:
        result.append(expression)

# As a concrete example, a list of the squares of the numbers from 1 to n, that is

[1, 4, 9, 16, 25, . . . , n2], can be created by traditional means as follows:

squares = [ ]
for k in range(1, n+1):
    squares.append(k k)

# With list comprehension, this logic is expressed as follows:

squares = [k*k for k in range(1, n+1)]

# As a second example, Section 1.8 introduced the goal of producing a list of factors
# for an integer n. That task is accomplished with the following list comprehension:

factors = [k for k in range(1,n+1) if n % k == 0]

# Python supports similar comprehension syntaxes that respectively produce a
# set, generator, or dictionary. We compare those syntaxes using our example for
# producing the squares of numbers.

[ k*k for k in range(1, n+1) ] list comprehension
{ k*k for k in range(1, n+1) } set comprehension
( k*k for k in range(1, n+1) ) generator comprehension
{ k : k*k for k in range(1, n+1) } dictionary comprehension

# The generator syntax is particularly attractive when results do not need to be stored
# in memory. For example, to compute the sum of the first n squares, the generator
# syntax, total = sum(k k for k in range(1, n+1)), is preferred to the use of an
# explicitly instantiated list comprehension as the parameter.
