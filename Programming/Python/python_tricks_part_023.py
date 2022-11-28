# Generators Are Simplified Iterators

# In the chapter on iterators we spent quite a bit of time writing a
# class-based iterator. This wasn’t a bad idea from an educational
# perspective—but it also demonstrated how writing an iterator class
# requires a lot of boilerplate code. To tell you the truth, as a “lazy”
# developer, I don’t like tedious and repetitive work.

# And yet, iterators are so useful in Python. They allow you to write
# pretty for-in loops and help you make your code more Pythonic and
# efficient. If there only was a more convenient way to write these 
# iterators in the first place...

# Surprise, there is! Once more, Python helps us out with some syntactic
# sugar to make writing iterators easier. In this chapter you’ll see
# how to write iterators faster and with less code using generators and
# the yield keyword.


class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value


# This is where Python’s generators enter the scene. If I rewrite this
# iterator class as a generator, it looks like this:

def repeater(value):
    while True:
        yield value

# We just went from seven lines of code to three. Not bad, eh? As you
# can see, generators look like regular functions but instead of using the
# return statement, they use yield to pass data back to the caller.

# Now, how do these generators work? They look like normal functions,
# but their behavior is quite different. For starters, calling a generator
# function doesn’t even run the function. It merely creates and returns
# a generator object:

repeater('Hey')
# <generator object repeater at 0x107bcdbf8>

# The code in the generator function only executes when next() is
# called on the generator object:

generator_obj = repeater('Hey')
next(generator_obj)
# 'Hey'

## DIFFERENCE BETWEEN RETURN AND YIELD

# And that’s quite a fitting mental model for what happens here. You
# see, when a return statement is invoked inside a function, it 
# permanently passes control back to the caller of the function. When a yield
# is invoked, it also passes control back to the caller of the function—but
# it only does so temporarily.

# Whereas a return statement disposes of a function’s local state, a
# yield statement suspends the function and retains its local state. In
# practical terms, this means local variables and the execution state of
# the generator function are only stashed away temporarily and not
# thrown out completely. Execution can be resumed at any time by
# calling next() on the generator:

# Generators That Stop Generating

def repeat_three_times(value):
    yield value
    yield value
    yield value
    
# Notice how this generator function doesn’t include any kind of loop.
# In fact it’s dead simple and only consists of three yield statements.
# If a yield temporarily suspends execution of the function and passes
# back a value to the caller, what will happen when we reach the end of
# this generator? Let’s find out:

for x in repeat_three_times('Hey there'):
   print(x)

# 'Hey there'
# 'Hey there'
# 'Hey there'

# As you may have expected, this generator stopped producing new 
# values after three iterations. We can assume that it did so by raising
# a StopIteration exception when execution reached the end of the function.

# Let’s come back to another example from the iterators chapter. The
# BoundedIterator class implemented an iterator that would only repeat
# a value a set number of times:

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

# Why don’t we try to re-implement this BoundedRepeater class as a
# generator function. Here’s my first take on it:

def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value

# This is intentionally made the while loop in this function a little unwieldy. I
# wanted to demonstrate how invoking a return statement from a generator
# causes iteration to stop with a StopIteration exception. We’ll
# soon clean up and simplify this generator function some more, but
# first let’s try out what we’ve got so far:

for x in bounded_repeater('Hi', 4):
    print(x)

# 'Hi'
# 'Hi'
# 'Hi'
# 'Hi'

# Great! Now we have a generator that stops producing values after
# a configurable number of repetitions. It uses the yield statement to
# pass back values until it finally hits the return statement and iteration stops.

# Like I promised you, we can further simplify this generator. We’ll take
# advantage of the fact that Python adds an implicit return None statement
# to the end of every function. This is what our final implementation looks like:

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

# Key Takeaways
# • Generator functions are syntactic sugar for writing objects that
# support the iterator protocol. Generators abstract away much
# of the boilerplate code needed when writing class-based iterators.
# • The yield statement allows you to temporarily suspend execution
# of a generator function and to pass back values from it.
# • Generators start raising StopIteration exceptions after control
# flow leaves the generator function by any means other than a yield statement.
