# Protected Members

# Our PredatoryCreditCard subclass directly accesses the data member self. balance,
# which was established by the parent CreditCard class. The underscored name, by
# convention, suggests that this is a nonpublic member, so we might ask if it is okay
# that we access it in this fashion. While general users of the class should not be
# doing so, our subclass has a somewhat privileged relationship with the superclass.
# Several object-oriented languages (e.g., Java, C++) draw a distinction for nonpublic
# members, allowing declarations of protected or private access modes. Members
# that are declared as protected are accessible to subclasses, but not to the general
# public, while members that are declared as private are not accessible to either. In
# this respect, we are using balance as if it were protected (but not private).

# Python does not support formal access control, but names beginning with a single
# underscore are conventionally akin to protected, while names beginning with a
# double underscore (other than special methods) are akin to private. In choosing to
# use protected data, we have created a dependency in that our PredatoryCreditCard
# class might be compromised if the author of the CreditCard class were to change
# the internal design. 

# Inheritence, Understanding it.


class Progression:
    """Iterator producing a generic progression
    
    Default iterator produces the whole numbers 0,1,2
    """

    def __init__(self, start =0) -> None:
        """ Initialize current to the first value of progression.
        """
        self._current = start

    def _advance(self):
        """ Update self._current to a new value.
        This should be overridden by subclasses.
        By convention, if current is set to None, this designates the 
        end of a finite progression.
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance() 
            return answer

    def __iter__(self):
        """By convention, an iterator should return itself."""
        return self

    def print_progression(self, n : int):
        """Print next n values of the progression"""
        print(" ".join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    """Iterator producing arithmetic progression"""

    def __init__(self, start=0, increment = 1) -> None:
        """ Create a new arithmetic progression.

        increment       the fixed constant to add to each term (default 1)
        start           the first term of the progression (default 0)

        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._increment

class GeometricProgression(Progression):
    """Iterator producing geometric progression"""
    def __init__(self, base = 2, start=1) -> None:
        """ Create a new geometric progression.

        base            the fixed constant multiplied to each term (default 2)
        start           the first term of the progression (default 1)

        """
        super().__init__(start)
        self. base = base

    def _advance(self):
        """Update current value by multiplying it by base"""
        self._current *= self.base

class FibonacciProgression(Progression):
    """Iterator producing Fibonacci progression"""

    def __init__(self, first= 0, second=1) -> None:
        """Create a new fibonacci progression.
        first                   the first term of the progression (default 0)
        second                  the second term of the progression (default 1)
        """       
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current

if __name__ == "__main__" :
    print( "Default progression:" )
    Progression().print_progression(10)
    print( "Arithmetic progression with increment 5:" )
    ArithmeticProgression(increment = 5).print_progression(10)
    print( "Arithmetic progression with increment 5 and start 2:" )
    ArithmeticProgression(increment = 5, start = 2).print_progression(10)
    print( "Geometric progression with default base:" )
    GeometricProgression().print_progression(10)
    print( "Geometric progression with base 3:" )
    GeometricProgression(3).print_progression(10)
    print( "Fibonacci progression with default start values:" )
    FibonacciProgression().print_progression(10)
    print( "Fibonacci progression with start values 4 and 6:" )
    FibonacciProgression(4, 6).print_progression(10)
    
# Default progression:
# 0 1 2 3 4 5 6 7 8 9

# Arithmetic progression with increment 5:
# 0 5 10 15 20 25 30 35 40 45

# Arithmetic progression with increment 5 and start 2:
# 5 7 9 11 13 15 17 19 21 23

# Geometric progression with default base:
# 1 2 4 8 16 32 64 128 256 512

# Geometric progression with base 3:
# 1 3 9 27 81 243 729 2187 6561 19683

# Fibonacci progression with default start values:
# 0 1 1 2 3 5 8 13 21 34

# Fibonacci progression with start values 4 and 6:
# 4 6 10 16 26 42 68 110 178 288
