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
    
# Inheritance

# A natural way to organize various structural components of a software package
# is in a hierarchical fashion, with similar abstract definitions grouped together in
# a level-by-level manner that goes from specific to more general as one traverses
# up the hierarchy.

# In object-oriented programming, the mechanism for a modular and hierarchical organization
# is a technique known as inheritance. This allows a new class to be defined
# based upon an existing class as the starting point. In object-oriented terminology,
# the existing class is typically described as the base class, parent class, or super-
# class, while the newly defined class is known as the subclass or child class.

# There are two ways in which a subclass can differentiate itself from its superclass.
# A subclass may specialize an existing behavior by providing a new implementation
# that overrides an existing method. A subclass may also extend its superclass by providing brand new methods.

# Here is an example 

# BaseException
#     +-- SystemExit
#     +-- KeyboardInterrupt
#     +-- GeneratorExit
#     +-- Exception
#          +-- StopIteration
#          +-- StandardError
#          |    +-- BufferError
#          |    +-- ArithmeticError
#          |    |    +-- FloatingPointError
#          |    |    +-- OverflowError
#          |    |    +-- ZeroDivisionError
#          |    +-- AssertionError
#          |    +-- AttributeError
#          |    +-- EnvironmentError
#          |    |    +-- IOError
#          |    |    +-- OSError
#          |    |         +-- WindowsError (Windows)
#          |    |         +-- VMSError (VMS)
#          |    +-- EOFError
#          |    +-- ImportError
#          |    +-- LookupError
#          |    |    +-- IndexError
#          |    |    +-- KeyError
#          |    +-- MemoryError
#          |    +-- NameError
#          |    |    +-- UnboundLocalError
#          |    +-- ReferenceError
#          |    +-- RuntimeError
#          |    |    +-- NotImplementedError
#          |    +-- SyntaxError
#          |    |    +-- IndentationError
#          |    |         +-- TabError
#          |    +-- SystemError
#          |    +-- TypeError
#          |    +-- ValueError
#          |         +-- UnicodeError
#          |              +-- UnicodeDecodeError
#          |              +-- UnicodeEncodeError
#          |              +-- UnicodeTranslateError
#          +-- Warning
#               +-- DeprecationWarning
#               +-- PendingDeprecationWarning
#               +-- RuntimeWarning
#               +-- SyntaxWarning
#               +-- UserWarning
#               +-- FutureWarning
#           +-- ImportWarning
#           +-- UnicodeWarning
#           +-- BytesWarning

# Here is an example for inheritence.

class CreditCard:
    """A consumer credit card"""
    def __init__(self, customer, bank, acnt, limit):
        """Initalize a new credit card
        
        Initial balance is zero
        
        customer            the name of the customer        eg. Ali Pek
        bank                the name of the bank            eg. Bank of America
        acnt                the account identifier number   eg. 5391 0375 9387 5309
        limit               the card limit                  eg. $ 1000       
        balance             the total debt of card          eg. $ 250
        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank   

    def get_account(self):
        return self._acnt  

    def get_limit(self):
        return self._limit

    def get_balance(self): 
        return self._balance    

    def charge(self,price):
        """Charge given price to the card, assuming sufficient limit
        
        Returns True if the charge was successful, False otherwise"""

        if price + self._balance > self._limit:
            print("Insufficient Limit")
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount



class DangerousCreditCard(CreditCard):
    """ An extention to the Credit Card that has compound interest and fees
    
    """
    def __init__(self,customer,bank,acnt,limit, apr):
        """Initalize a new Dangerous credit card
        
        Initial balance is zero
        
        customer            the name of the customer        eg. Ali Pek
        bank                the name of the bank            eg. Bank of America
        acnt                the account identifier number   eg. 5391 0375 9387 5309
        limit               the card limit                  eg. $ 1000       
        balance             the total debt of card          eg. $ 250
        apr                 the annual percentage rate      eg. 0.0825 for %8.25 APR  
        """
        super().__init__(customer,bank,acnt,limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess 5 fee if charge is denied.
        """
        success = super().charge(price)
        if not success:
            self._balance -= 5
        
        return success
        
    def process_month(self):
        """Asses monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
