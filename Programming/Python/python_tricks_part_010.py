# Class vs Instance Variable Pitfalls

# Class variables are declared inside the class definition (but outside
# of any instance methods). They’re not tied to any particular instance
# of a class. Instead, class variables store their contents on the class
# itself, and all objects created from a particular class share access to the
# same set of class variables. This means, for example, that modifying
# a class variable affects all object instances at the same time.

# Instance variables are always tied to a particular object instance.
# Their contents are not stored on the class, but on each individual object
# created from the class. Therefore, the contents of an instance variable
# are completely independent from one object instance to the next.
# And so, modifying an instance variable only affects one object instance at a time.

class Dog:
    num_legs = 4                  # <- Class variable

    def __init__(self, name):
        self.name = name          # <- Instance variable

jack = Dog('Jack')
jill = Dog('Jill')
jack.name, jill.name
# ('Jack', 'Jill')

jack.num_legs, jill.num_legs
# (4, 4)
Dog.num_legs
# 4

# If we however:
Dog.name
# AttributeError: "type object "Dog" has no attribute "name""

# What if we want to change a Dog's leg count.

Dog.num_legs = 6
# This will change everything.

jack.num_legs, jill.num_legs
# (6, 6)

# We can:
Dog.num_legs = 4
jack.num_legs = 6

jack.num_legs, jill.num_legs, Dog.num_legs
# (6, 4, 4)

# Looks decent ? 

# You see, the trouble here is that while we got the result we wanted (extra
# legs for Jack), we introduced a num_legs instance variable to the
# Jack instance. And now the new num_legs instance variable “shadows”
# the class variable of the same name, overriding and hiding it when we access the object instance scope:

jack.num_legs, jack.__class__.num_legs
# (6, 4)

# Another example.

# The following CountedObject class keeps track of how many times
# it was instantiated over the lifetime of a program (which
# might actually be an interesting performance metric to know):

class CountedObject:
    num_instances = 0
  
    def __init__(self):
        self.__class__.num_instances += 1


# CountedObject keeps a num_instances class variable that serves as
# a shared counter. When the class is declared, it initializes the counter to zero and then leaves it alone.

# Every time you create a new instance of this class, it increments the
# shared counter by one when the __init__ constructor runs:


CountedObject.num_instances
# 0
CountedObject().num_instances
# 1
CountedObject().num_instances
# 2
CountedObject().num_instances
# 3
CountedObject.num_instances
# 3

# Notice how this code needs to jump through a little hoop to make sure it increments the counter variable on the class. 

# It would’ve been an easy mistake to make if I had written the constructor as follows:

# WARNING: This implementation contains a bug

class BuggyCountedObject:
    num_instances = 0
    
    def __init__(self):
        self.num_instances += 1
        
BuggyCountedObject.num_instances
# 0
BuggyCountedObject().num_instances
# 1
BuggyCountedObject().num_instances
# 1
BuggyCountedObject().num_instances
# 1
BuggyCountedObject.num_instances
# 0

# This (buggy) implementation never increments the shared counter because I made
# the mistake I explained in the “Jack the Dog” example earlier. This
# implementation won’t work because I accidentally “shadowed” the
# num_instance class variable by creating an instance variable of the
# same name in the constructor.

# It correctly calculates the new value for the counter (going from 0 to 1),
# but then stores the result in an instance variable—which means other
# instances of the class never even see the updated counter value.
