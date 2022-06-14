# By the end of this, you will be able to create complex expressions by combining objects and operators.

a = 20
b = 30

a + b - 5 

# A sequence of operands and operators, like a + b - 5, is called an expression.
# Python supports many operators for combining data objects into expressions.

#
# Arithmetic Operators
#

a = 4
b = 3

# Unary Positive
+a 
# 4

# Unary Negation
-b
# -3

# Addition
a + b
# 7

# Subtraction
a - b
# 1

# Multiplication
a * b
# 12

# Division
a / b
# 1.3333333333333333

# Modulo
a % b
# 1

# Floor Division
a // b
# 1

# Exponentiation
a ** b
# 64


#
# Comparison Operators
#

a = 10
b = 20

# Equal to
a == b
# False

# Not equal to
a != b
# True

# Less than or equal to
a <= b
# True

# Greater than or equal to
a >= b
# False

a = 30
b = 30

a == b
# True

a <= b
# True

a >= b
# True


# Bitwise Operators

# & 	a & b 	  bitwise AND 	Each bit position in the result is the logical AND of the bits in the corresponding position of the operands. (1 if both are 1, otherwise 0.)
# | 	a | b 	  bitwise OR 	Each bit position in the result is the logical OR of the bits in the corresponding position of the operands. (1 if either is 1, otherwise 0.)
# ~ 	~a 	      bitwise negation 	Each bit position in the result is the logical negation of the bit in the corresponding position of the operand. (1 if 0, 0 if 1.)
# ^ 	a ^ b 	  bitwise XOR (exclusive OR) 	Each bit position in the result is the logical XOR of the bits in the corresponding position of the operands. (1 if the bits in the operands are different, 0 if they are the same.)
# >> 	a >> n 	  Shift right n places 	Each bit is shifted right n places.
# << 	a << n 	  Shift left n places 	Each bit is shifted left n places.

# Operator Precedence

# lowest precedence 	                        or 	Boolean OR
# 	                                          and 	Boolean AND
# 	                                          not 	Boolean NOT
# 	                                          ==, !=, <, <=, >, >=, is, is not 	comparisons, identity
# 	                                          | 	bitwise OR
# 	                                          ^ 	bitwise XOR
# 	                                          & 	bitwise AND
# 	                                          <<, >> 	bit shifts
# 	                                          +, - 	addition, subtraction
# 	                                          *, /, //, % 	multiplication, division, floor division, modulo
# 	                                          +x, -x, ~x 	unary positive, unary negation, bitwise negation##
# highest precedence 	                        ** 	exponentiation


# Left at - Augmented Assignment Operators
