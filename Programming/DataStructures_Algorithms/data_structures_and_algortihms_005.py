# Simple Input and Output

# In this section, we address the basics of input and output in Python, describing 
# standard input and output through the user console, and Python’s support for reading
# and writing text files.

# Console Input and Output

# The print Function

# The built-in function, print, is used to generate standard output to the console.
# In its simplest form, it prints an arbitrary sequence of arguments, separated by
# spaces, and followed by a trailing newline character. For example, the command
# print("maroon" , 5) outputs the string "maroon 5\n" . Note that arguments need
# not be string instances. A nonstring argument x will be displayed as str(x). Without
# any arguments, the command print( ) outputs a single newline character.

# The print function can be customized through the use of the following keyword
# parameters (see Section 1.5 for a discussion of keyword parameters):

# • By default, the print function inserts a separating space into the output between
# each pair of arguments. The separator can be customized by providing
# a desired separating string as a keyword parameter, sep. For example, colon-
# separated output can be produced as print(a, b, c, sep= : ). The separating
# string need not be a single character; it can be a longer string, and it can be
# the empty string, sep= , causing successive arguments to be directly concatenated.

# • By default, a trailing newline is output after the final argument. An alternative
# trailing string can be designated using a keyword parameter, end. Designating
# the empty string end= suppresses all trailing characters.

# • By default, the print function sends its output to the standard console. However,
# output can be directed to a file by indicating an output file stream using file as a keyword parameter.
