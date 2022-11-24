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

