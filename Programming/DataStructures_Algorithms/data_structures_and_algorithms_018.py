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

# Let f(n) and g(n) be functions mapping positive integers to positive real numbers.
# We say that f(n) is O(g(n)) if there is a real constant c > 0 and an integer constant
# n0 ≥ 1 such that

# f(n) ≤ cg(n),       for n ≥ n0.

# This definition is often referred to as the “big-Oh” notation, for it is sometimes 
# pronounced as “f(n) is big-Oh of g(n).” Figure 3.5 illustrates the general definition.

# The big-Oh notation allows us to say that a function f(n) is “less than or equal
# to” another function g(n) up to a constant factor and in the asymptotic sense as n
# grows toward infinity. This ability comes from the fact that the definition uses “≤”
# to compare f(n) to a g(n) times a constant, c, for the asymptotic cases when n ≥ n0.

# However, it is considered poor taste to say “f(n) ≤ O(g(n)),” since the big-Oh
# already denotes the “less-than-or-equal-to” concept. Likewise, although common,
# it is not fully correct to say “f(n) = O(g(n)),” with the usual understanding of the
# “=” relation, because there is no way to make sense of the symmetric statement,
# “O(g(n)) = f(n).” It is best to say,

# “ f(n) is O(g(n)).”
