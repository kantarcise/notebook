# Control Flow

# In this section, we review Python’s most fundamental control structures: conditional
# statements and loops. Common to all control structures is the syntax used
# in Python for defining blocks of code. The colon character is used to delimit the
# beginning of a block of code that acts as a body for a control structure. If the body
# can be stated as a single executable statement, it can technically placed on the same
# line, to the right of the colon. However, a body is more typically typeset as an
# indented block starting on the line following the colon. Python relies on the indentation
# level to designate the extent of that block of code, or any nested blocks of
# code within. 

# Conditionals
# Conditional constructs (also known as if statements) provide a way to execute a
# chosen block of code based on the run-time evaluation of one or more Boolean
# expressions. In Python, the most general form of a conditional is written as follows:

if first condition:
    first body
elif second condition:
    second body
elif third condition:
    third body
else:
    fourth body

# Each condition is a Boolean expression, and each body contains one or more commands
# that are to be executed conditionally. If the first condition succeeds, the first
# body will be executed; no other conditions or bodies are evaluated in that case.
# If the first condition fails, then the process continues in similar manner with the
# evaluation of the second condition. The execution of this overall construct will
# cause precisely one of the bodies to be executed. There may be any number of
# elif clauses (including zero), and the final else clause is optional. 

if response:
# as a shorthand for the equivalent,
if response != '':

#  As a simple example, a robot controller might have the following logic:

if door is closed:
    open_door()
advance()

# Notice that the final command, advance(), is not indented and therefore not part of
# the conditional body. It will be executed unconditionally (although after opening a
# closed door).

# We may nest one control structure within another, relying on indentation to
# make clear the extent of the various bodies. Revisiting our robot example, here is a
# more complex control that accounts for unlocking a closed door.

if door is closed:
    if door is locked:
        unlock_door()
    open_door()
advance()

# Loops

# To be Continued

# Python offers two distinct looping constructs. A while loop allows general repetition
# based upon the repeated testing of a Boolean condition. A for loop provides
# convenient iteration of values from a defined series (such as characters of a string,
# elements of a list, or numbers within a given range). We discuss both forms in this section.

# While Loops

# The syntax for a while loop in Python is as follows:
while condition:
    body

# As with an if statement, condition can be an arbitrary Boolean expression, and
# body can be an arbitrary block of code (including nested control structures). The
# execution of a while loop begins with a test of the Boolean condition. If that condition
# evaluates to True, the body of the loop is performed. After each execution of
# the body, the loop condition is retested, and if it evaluates to True, another iteration
# of the body is performed. When the conditional test evaluates to False (assuming
# it ever does), the loop is exited and the flow of control continues just beyond the
# body of the loop.

# As an example, here is a loop that advances an index through a sequence of
# characters until finding an entry with value X or reaching the end of the sequence.

j = 0
while j < len(data) and data[j] != X :
    j += 1

# The len function, which we will introduce in Section 1.5.2, returns the length of a
# sequence such as a list or string. The correctness of this loop relies on the short-
# circuiting behavior of the and operator, as described on page 12. We intentionally
# test j < len(data) to ensure that j is a valid index, prior to accessing element
# data[j]. Had we written that compound condition with the opposite order, the evaluation
# of data[j] would eventually raise an IndexError when X is not found.

# As written, when this loop terminates, variable j’s value will be the index of
# the leftmost occurrence of X , if found, or otherwise the length of the sequence
# (which is recognizable as an invalid index to indicate failure of the search). It is
# worth noting that this code behaves correctly, even in the special case when the list
# is empty, as the condition j < len(data) will initially fail and the body of the loop
# will never be executed.
