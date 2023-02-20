# Algorithm Analysis

# Experimental Studies

# If an algorithm has been implemented, we can study its running time by executing
# it on various test inputs and recording the time spent during each execution. A
# simple approach for doing this in Python is by using the time function of the time module.

from time import time
start time = time()                 # record the starting time
# run algorithm
end time = time()                   # record the ending time
elapsed = end time − start time     # compute the elapsed time


# An elapsed time measured in this fashion is a decent reflection of the algorithm
# efficiency, but it is by no means perfect. The time function measures relative to what is
# known as the “wall clock.” Because many processes share use of a computer’s central processing unit (or CPU), the
# elapsed time will depend on what other processes are running on the computer
# when the test is performed. 

# A fairer metric is the number of CPU cycles that are
# used by the algorithm. This can be determined using the clock function of the time
# module, but even this measure might not be consistent if repeating the identical
# algorithm on the identical input, and its granularity will depend upon the computer
# system. 

# Python includes a more advanced module, named timeit, to help automate
# such evaluations with repetition to account for such variance among trials.

# Because we are interested in the general dependence of running time on the size
# and structure of the input, we should perform independent experiments on many
# different test inputs of various sizes.


# Challenges of Experimental Analysis

# While experimental studies of running times are valuable, especially when fine-
# tuning production-quality code, there are three major limitations to their use for
# algorithm analysis:

# • Experimental running times of two algorithms are difficult to directly com-
# pare unless the experiments are performed in the same hardware and software
# environments.

# • Experiments can be done only on a limited set of test inputs; hence, they
# leave out the running times of inputs not included in the experiment (and
# these inputs may be important).

# • An algorithm must be fully implemented in order to execute it to study its
# running time experimentally.

# Moving Beyond Experimental Analysis

# Our goal is to develop an approach to analyzing the efficiency of algorithms that:
# 1. Allows us to evaluate the relative efficiency of any two algorithms in a way
# that is independent of the hardware and software environment.
# 2. Is performed by studying a high-level description of the algorithm without
# need for implementation.
# 3. Takes into account all possible inputs.

# To analyze the running time of an algorithm without performing experiments, we
# perform an analysis directly on a high-level description of the algorithm (either in
# the form of an actual code fragment, or language-independent pseudo-code). We
# define a set of primitive operations such as the following:

# • Assigning an identifier to an object
# • Determining the object associated with an identifier
# • Performing an arithmetic operation (for example, adding two numbers)
# • Comparing two numbers
# • Accessing a single element of a Python list by index
# • Calling a function (excluding operations executed within the function)
# • Returning from a function.

# Instead of trying to determine the specific execution time of each
# primitive operation, we will simply count how many primitive operations
# are executed, and use this number t as a measure of the running
# time of the algorithm.

# This operation count will correlate to an actual running time in a specific computer,
# for each primitive operation corresponds to a constant number of instructions,
# and there are only a fixed number of primitive operations

# Measuring Operations as a Function of Input Size

# To capture the order of growth of an algorithm’s running time, we will associate,
# with each algorithm, a function f(n) that characterizes the number of primitive
# operations that are performed as a function of the input size n.


# Focusing on the Worst-Case Input.

# An algorithm may run faster on some inputs than it does on others of the same size.
# Thus, we may wish to express the running time of an algorithm as the function of
# the input size obtained by taking the average over all possible inputs of the same
# size. Unfortunately, such an average-case analysis is typically quite challenging.
# It requires us to define a probability distribution on the set of inputs, which is often
# a difficult task.

# Worst-case analysis is much easier than average-case analysis, as it requires
# only the ability to identify the worst-case input, which is often simple. Also, this
# approach typically leads to better algorithms.
