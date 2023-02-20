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

# In this section, we briefly discuss the seven most important functions used in the
# analysis of algorithms.

# 
# The Constant Function
# 

# The simplest function we can think of is the constant function. This is the function,

f(n) = c

# for some fixed constant c, such as c = 5, c = 27, or c = 210. That is, for any
# argument n, the constant function f(n) assigns the value c.

# 
# The Logarithm Function
# 

# One of the interesting and sometimes even surprising aspects of the analysis of
# data structures and algorithms is the ubiquitous presence of the logarithm function,

f(n) = logb n, for some constant b > 1. 

# This function is defined as follows:
x = logb n if and only if bx = n.

# By definition, logb 1 = 0. The value b is known as the base of the logarithm.
# The most common base for the logarithm function in computer science is 2,
# as computers store integers in binary, and because a common operation in many
# algorithms is to repeatedly divide an input in half. In fact, this base is so common
# that we will typically omit it from the notation when it is 2. That is, for us,

logn = log2 n.

# 
# The Linear Function
# 

# Another simple yet important function is the linear function,
f(n) = n.
# That is, given an input value n, the linear function f assigns the value n itself.

# 
# The N-Log-N Function
# 

# The next function we discuss in this section is the n-log-n function,
f(n) = nlogn,

# that is, the function that assigns to an input n the value of n times the logarithm
# base-two of n. This function grows a little more rapidly than the linear function and
# a lot less rapidly than the quadratic function; therefore, we would greatly prefer an
# algorithm with a running time that is proportional to nlogn, than one with quadratic running time.


# 
# The Quadratic Function
# 

# Another function that appears often in algorithm analysis is the quadratic function,
f(n) = n**2.
# That is, given an input value n, the function f assigns the product of n with itself
# (in other words, “n squared”).

# The main reason why the quadratic function appears in the analysis of algo-
# rithms is that there are many algorithms that have nested loops, where the inner
# loop performs a linear number of operations and the outer loop is performed a
# linear number of times.

# 
# The Cubic Function and Other Polynomials
# 
# Continuing our discussion of functions that are powers of the input, we consider
# the cubic function,
f(n) = n**3,
# which assigns to an input value n the product of n with itself three times. This func-
# tion appears less frequently in the context of algorithm analysis than the constant,
# linear, and quadratic functions previously mentioned, but it does appear from time to time.

# The Exponential Function
# Another function used in the analysis of algorithms is the exponential function,
f(n) = b**n,
# where b is a positive constant, called the base, and the argument n is the exponent.
# That is, function f(n) assigns to the input argument n the value obtained by multiplying the base b by itself n times.

# Summary

# constant    logarithm     linear      n-log-n      quadratic      cubic      exponential 
# 1           logn          n           nlogn        n**2           n**3       a**n

# Ideally, we would like data structure operations to run in times proportional
# to the constant or logarithm function, and we would like our algorithms to run in
# linear or n-log-n time. Algorithms with quadratic or cubic running times are less
# practical, and algorithms with exponential running times are infeasible for all but
# the smallest sized inputs. 

# Ceiling and Floor Functions

# The analysis of an algorithm may sometimes involve the use
# of the floor function and ceiling function, which are defined respectively as follows:

# • ⌊x⌋ = the largest integer less than or equal to x.
# • ⌈x⌉ = the smallest integer greater than or equal to x.

# Asymptotic Analysis

# In algorithm analysis, we focus on the growth rate of the running time as a function
# of the input size n, taking a “big-picture” approach. For example, it is often enough
# just to know that the running time of an algorithm grows proportionally to n.

# We analyze algorithms using a mathematical notation for functions that disregards
# constant factors. Namely, we characterize the running times of algorithms
# by using functions that map the size of the input, n, to values that correspond to
# the main factor that determines the growth rate in terms of n. This approach re-
# flects that each basic step in a pseudo-code description or a high-level language
# implementation may correspond to a small number of primitive operations.

# Thus, we can perform an analysis of an algorithm by estimating the number of primitive
# operations executed up to a constant factor, rather than getting bogged down in
# language-specific or hardware-specific analysis of the exact number of operations
# that execute on the computer.


def find_max(data):
    """Return the maximum element from a nonempty list"""
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest
  
# This is a classic example of an algorithm with a running time that grows pro-
# portional to n, as the loop executes once for each data element, with some fixed
# number of primitive operations executing for each pass. In the remainder of this
# section, we provide a framework to formalize this claim.

# The “Big-Oh” Notation
  
