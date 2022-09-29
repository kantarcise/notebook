import datetime

# String Conversion (Every Class Needs a __repr__)

# When you define a custom class in Python and then try to print one of
# its instances to the console (or inspect it in an interpreter session), you
# get a relatively unsatisfying result. The default “to string” conversion
# behavior is basic and lacks detail:


class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    
    # added method
    def __str__(self):
        return f"A {self.color} car!"
    
    # And also added
    def __repr__(self):
        return "__repr__ method"
        
my_car = Car("red", 28934)

print(my_car)
# <__console__.Car object at 0x109b73da0>

my_car
# <__console__.Car object at 0x109b73da0>

# By default all you get is a string containing the class name and the id of
# the object instance (which is the object’s memory address in CPython.)
# That’s better than nothing, but it’s also not very useful.

# __str__ is one of Python’s “dunder” (double-underscore) methods
# and gets called when you try to convert an object into a string through
# the various means that are available:

# After the added methods of str and repr:

print(my_Car)
# A red car!
"{}".format(my_car)
# "A red car!"
my_car
# __repr__ method

# This experiment confirms that inspecting an object in a Python interpreter 
# session simply prints the result of the object’s __repr__.

# So, how to they differ in real world?
# Let's use datetime as an example.

today = datetime.date.today()

str(today)
# "2022-09-29"
repr(today)
# "datetime.date(2022, 9, 29)"

# You can keep this test in mind when you are writing your own methods.

# If you don’t add a __str__ method, Python falls back on the result
# of __repr__ when looking for __str__. Therefore, I recommend that
# you always add at least a __repr__ method to your classes. This will
# guarantee a useful string conversion result in almost all cases, with a
# minimum of implementation work.

# Here is a quality repr example:

def __repr__(self):
    return (f'{self.__class__.__name__}('
            f'{self.color!r}, {self.mileage!r})')
