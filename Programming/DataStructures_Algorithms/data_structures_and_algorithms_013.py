# Example, Range Class

# Prior to Python 3, range() was a function and it returned a list instance with elements within a range.
# This was problematic beacuse it was initializing a list with range of numbers.

# In python 3 this was solved with lazy evaluation.

# Rather than creating a new list instance, range
# is a class that can effectively represent the desired range of elements without ever
# storing them explicitly in memory.

class Range:
    """A class that mimics the built in Range Class"""

    def __init__(self, start, stop = None, step=1 ):
        """Initalize a Range instance"""
        if step == 0:
            raise ValueError("Step cannot be zero")

        if stop is None:
            start, stop = 0 , start

        # Calculate the effective lenght
        self._lenght = max(0,(stop - start + step -1 ) // step)
        
        # need knowladge of start and step yo support getitem.
        self._start = start
        self._step = step

    def __len__(self):
        """Returns number of entries in the range"""
        return self._lenght

    def __getitem__(self, k):
        """Return entry at index k"""
        if k < 0:
            k =+ len(self)
        if not 0 <= k < self._lenght:
            raise IndexError ("index out of range")

        return self._start + k * self._step
