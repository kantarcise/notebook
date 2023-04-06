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

#  The big-Oh notation allows us to ignore constant factors and lower-order terms and
# focus on the main components of a function that affect its growth.

# Example 3.8: 5n^4 + 3n^3 + 2n^2 + 4n + 1 is O(n^4) .

# Justification: Note that 5n^4 + 3n^3 + 2n^2 + 4n + 1 ≤ (5 + 3 + 2 + 4 + 1)n^4 = cn^4 ,
# for c = 15, when n ≥ n0 = 1.

# Thus, the highest-degree term in a polynomial is the term that determines the
# asymptotic growth rate of that polynomial.

# In general, we should use the big-Oh notation to characterize a function as closely
# as possible. While it is true that the function f (n) = 4n^3 + 3n^2 is O(n^5) or even
# O(n^4), it is more accurate to say that f (n) is O(n^3). 

# Consider, by way of analogy, a scenario where a hungry traveler driving along a long country road happens upon
# a local farmer walking home from a market. If the traveler asks the farmer how
# much longer he must drive before he can find some food, it may be truthful for the
# farmer to say, “certainly no longer than 12 hours,” but it is much more accurate
# (and helpful) for him to say, “you can find a market just a few minutes drive up this
# road.” Thus, even with the big-Oh notation, we should strive as much as possible
# to tell the whole truth.

