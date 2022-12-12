# Expressions, Operators, and Precedence

# In the previous section, we demonstrated how names can be used to identify existing
# objects, and how literals and constructors can be used to create instances of
# built-in classes. Existing values can be combined into larger syntactic expressions
# using a variety of special symbols and keywords known as operators. 

# The semantics of an operator depends upon the type of its operands. For example, when a
# and b are numbers, the syntax a + b indicates addition, while if a and b are strings,
# the operator indicates concatenation. In this section, we describe Python’s operators
# in various contexts of the built-in types.

# We continue, in Section 1.3.1, by discussing compound expressions, such as
# a + b c, which rely on the evaluation of two or more operations. The order
# in which the operations of a compound expression are evaluated can affect the
# overall value of the expression. For this reason, Python defines a specific order of
# precedence for evaluating operators, and it allows a programmer to override this
# order by using explicit parentheses to group subexpressions.

# Logical Operators
# Python supports the following keyword operators for Boolean values:

not           # unary negation
and           # conditional and
or            # conditional or

# The and and or operators short-circuit, in that they do not evaluate the second
# operand if the result can be determined based on the value of the first operand.
# This feature is useful when constructing Boolean expressions in which we first test
# that a certain condition holds (such as a reference not being None), and then test a
# condition that could have otherwise generated an error condition had the prior test
# not succeeded.

# 
# Equality Operators
# 

# Python supports the following operators to test two notions of equality:

is        # same identity
is  not   # different identity
==        # equivalent
!=        # not equivalent

# The expression a is b evaluates to True, precisely when identifiers a and b are
# aliases for the same object. The expression a == b tests a more general notion of
# equivalence. If identifiers a and b refer to the same object, then a == b should also
# evaluate to True. Yet a == b also evaluates to True when the identifiers refer to
# different objects that happen to have values that are deemed equivalent. 

# The precise notion of equivalence depends on the data type. For example, two strings are considered
# equivalent if they match character for character. Two sets are equivalent if
# they have the same contents, irrespective of order. In most programming situations,
# the equivalence tests == and != are the appropriate operators; use of is and is not
# should be reserved for situations in which it is necessary to detect true aliasing.

# 
# Comparison Operators
# 

# Data types may define a natural order via the following operators:

<       # less than
<=      # less than or equal to
>       # greater than
>=      # greater than or equal to

# These operators have expected behavior for numeric types, and are defined 
# lexicographically, and case-sensitively, for strings. An exception is raised if operands
# have incomparable types, as with 5 < hello .

# 
# Arithmetic Operators
# 

# Python supports the following arithmetic operators:

+         # addition
−         # subtraction
*         # multiplication
/         # true division - 27 / 4 results in the float value 6.75.
//        # integer division -  27 // 4 evaluating to int value 6 (the mathematical floor of the quotient)
%         # the modulo operator - 27 % 4 evaluating to int value 3, the remainder of the integer division

# The use of addition, subtraction, and multiplication is straightforward, noting that if
# both operands have type int, then the result is an int as well; if one or both operands
# have type float, the result will be a float.

# We note that languages such as C, C++, and Java do not support the // operator; instead, the / 
# operator returns the truncated quotient when both operands have integral type, and the
# result of true division when at least one operand has a floating-point type

# Python carefully extends the semantics of // and % to cases where one or both
# operands are negative. For the sake of notation, let us assume that variables n
# and m represent respectively the dividend and divisor of a quotient n
# m , and that q = n // m and r = n % m. Python guarantees that q * m + r will equal n. We
# already saw an example of this identity with positive operands, as 6 ∗ 4 + 3 = 27.

# When the divisor m is positive, Python further guarantees that 0 ≤ r < m. As
# a consequence, we find that −27 // 4 evaluates to −7 and −27 % 4 evaluates
# to 1, as (−7) ∗ 4 + 1 = −27. When the divisor is negative, Python guarantees that
# m < r ≤ 0. As an example, 27 // −4 is −7 and 27 % −4 is −1, satisfying the
# identity 27 = (−7) ∗ (−4) + (−1).

# The conventions for the // and % operators are even extended to floating-
# point operands, with the expression q = n // m being the integral floor of the
# quotient, and r = n % m being the “remainder” to ensure that q m + r equals
# n. For example, 8.2 // 3.14 evaluates to 2.0 and 8.2 % 3.14 evaluates to 1.92, as
# 2.0 ∗ 3.14 + 1.92 = 8.2.

# 
# Bitwise Operators
# 

# Python provides the following bitwise operators for integers:

∼       # bitwise complement (prefix unary operator)
&       # bitwise and
|       # bitwise or
ˆ       # bitwise exclusive-or
<<      # shift bits left, filling in with zeros
>>      # shift bits right, filling in with sign bit

# 
# Sequence Operators
# 

# Each of Python’s built-in sequence types (str, tuple, and list) support the following operator syntaxes:

s[j]                                  # element at index j
s[start:stop]                         # slice including indices [start,stop)
s[start:stop:step]                    # slice including indices start, start + step,
                                      # start + 2 step, . . . , up to but not equalling or stop
s + t                                 # concatenation of sequences
k * s                                 # shorthand for s + s + s + ... (k times)
val in s                              # containment check
val not in s                          # non-containment check

# To Be Continued
