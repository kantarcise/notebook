# Generator Expressions

# As I learned more about Python’s iterator protocol and the different
# ways to implement it in my own code, I realized that “syntactic sugar”
# was a recurring theme.

# You see, class-based iterators and generator functions are two expressions
# of the same underlying design pattern.

# Generator functions give you a shortcut for supporting the iterator
# protocol in your own code, and they avoid much of the verbosity of
# class-based iterators. With a little bit of specialized syntax, or 
# syntactic sugar, they save you time and make your life as a developer easier.

# This is a recurring theme in Python and in other programming 
# languages. As more developers use a design pattern in their programs,
# there’s a growing incentive for the language creators to provide 
# abstractions and implementation shortcuts for it.

# That’s how programming languages evolve over time—and as developers,
# we reap the benefits. We get to work with more and more powerful
# building blocks, which reduces busywork and lets us achieve more in less time.

# Earlier in this book you saw how generators provide syntactic sugar
# for writing class-based iterators. The generator expressions we’ll
# cover in this chapter add another layer of syntactic sugar on top.

# Generator expressions give you an even more effective shortcut for
# writing iterators. With a simple and concise syntax that looks like a
# list comprehension, you’ll be able to define iterators in a single line of code.

# Here’s an example:

iterator = ('Hello' for i in range(3))

# Careful about the paranthesis. it's circular.
# This is basicallt one line version of this:

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

iterator = bounded_repeater('Hello', 3)

