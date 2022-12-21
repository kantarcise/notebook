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

# For Loops

# Python’s for-loop syntax is a more convenient alternative to a while loop when
# iterating through a series of elements. The for-loop syntax can be used on any
# type of iterable structure, such as a list, tuple str, set, dict, or file (we will discuss
# iterators more formally in Section 1.8). Its general syntax appears as follows.

for element in iterable:
    # do stuff
 
# As an instructive example of such a loop, we consider the task of computing
# the sum of a list of numbers. (Admittedly, Python has a built-in function, sum, for
# this purpose.) We perform the calculation with a for loop as follows, assuming that
# data identifies the list:

total = 0
for val in data:
    total += val # note use of the loop variable, val

# The loop body executes once for each element of the data sequence, with the 
# identifier, val, from the for-loop syntax assigned at the beginning of each pass to a
# respective element. It is worth noting that val is treated as a standard identifier. If
# the element of the original data happens to be mutable, the val identifier can be
# used to invoke its methods. But a reassignment of identifier val to a new value has
# no affect on the original data, nor on the next iteration of the loop.

# As a second classic example, we consider the task of finding the maximum
# value in a list of elements (again, admitting that Python’s built-in max function
# already provides this support). If we can assume that the list, data, has at least one
# element, we could implement this task as follows:

biggest = data[0] # as we assume nonempty list
for val in data:
    if val > biggest:
    biggest = val

# Although we could accomplish both of the above tasks with a while loop, the
# for-loop syntax had an advantage of simplicity, as there is no need to manage an
# explicit index into the list nor to author a Boolean loop condition. Furthermore, we
# can use a for loop in cases for which a while loop does not apply, such as when
# iterating through a collection, such as a set, that does not support any direct form
# of indexing.

# Index-Based For Loops

# The simplicity of a standard for loop over the elements of a list is wonderful; 
# however, one limitation of that form is that we do not know where an element resides
# within the sequence. In some applications, we need knowledge of the index of an
# element within the sequence. For example, suppose that we want to know where
# the maximum element in a list resides.

# Rather than directly looping over the elements of the list in that case, we prefer
# to loop over all possible indices of the list. For this purpose, Python provides
# a built-in class named range that generates integer sequences.
# In simplest form, the syntax range(n) generates the
# series of n values from 0 to n − 1. Conveniently, these are precisely the series of
# valid indices into a sequence of length n. Therefore, a standard Python idiom for
# looping through the series of indices of a data sequence uses a syntax,

for j in range(len(data)):

# In this case, identifier j is not an element of the data—it is an integer. But the
# expression data[j] can be used to retrieve the respective element. For example, we
# can find the index of the maximum element of a list a

big index = 0
for j in range(len(data)):
    if data[j] > data[big index]:
        big index = j
