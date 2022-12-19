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
if response != :

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
