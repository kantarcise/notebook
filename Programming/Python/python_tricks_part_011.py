# Instance, Class, and Static Methods

# In this chapter you’ll see what’s behind class methods, static methods,
# and regular instance methods in Python.

# If you develop an intuitive understanding for their differences, you’ll
# be able to write object-oriented Python that communicates its intent
# more clearly and will be easier to maintain in the long run.

class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

 # "method()" is an instance method.

# Through the self parameter, instance methods can freely access attributes
# and other methods on the same object. This gives them a lot
# of power when it comes to modifying an object’s state.

# Not only can they modify object state, instance methods can also
# access the class itself through the self.__class__ attribute. This
# means instance methods can also modify class state.

 # "classmethod()" is a class method.
    
# Instead of accepting a self parameter, class methods take a cls parameter
# that points to the class—and not the object instance—when the method is called.

# Since the class method only has access to this cls argument, it can’t
# modify object instance state. That would require access to self. However, class
# methods can still modify class state that applies across all instances of the class.

 # "staticmethod()" is a static method.
    
# This type of method doesn’t take a self or a cls parameter, although,
# of course, it can be made to accept an arbitrary number of other parameters.

# As a result, a static method cannot modify object state or class state.
# Static methods are restricted in what data they can access—they’re
# primarily a way to namespace your methods.

obj = MyClass()
obj.method()
# ('instance method called', <MyClass instance at 0x11a2>)

# When the method is called, Python replaces the self argument with
# the instance object, obj . We could ignore the syntactic sugar provided
# by the obj.method() dot-call syntax and pass the instance object manually to get the same result:
    
MyClass.method(obj)
# ('instance method called', <MyClass instance at 0x11a2>)

# By the way, instance methods can also access the class itself through
# the self.__class__ attribute. This makes instance methods powerful in terms of
# access restrictions—they can freely modify state on the object instance and on the class itself.

obj.classmethod()
# ('class method called', <class MyClass at 0x11a2>)


obj.staticmethod()
# 'static method called'

# Did you see how we called staticmethod() on the object and were
# able to do so successfully? Some developers are surprised when they
# learn that it’s possible to call a static method on an object instance.

# Here is a real example now:

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def__repr__(self):
        return f'Pizza({self.ingredients!r})'

Pizza(['cheese', 'tomatoes'])
# Pizza(['cheese', 'tomatoes'])

# Delicious Pizza Factories With @classmethod

Pizza(['mozzarella', 'tomatoes'])
Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms'])
Pizza(['mozzarella'] * 4)

# Let's make a better interface for the pizza objects to our users.

class BetterPizza:
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def__repr__(self):
        return f'Pizza({self.ingredients!r})'
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

# Note how I’m using the cls argument in the margherita and
# prosciutto factory methods instead of calling the Pizza constructor directly.

# This is a trick you can use to follow the Don’t Repeat Yourself (DRY)8
# principle. If we decide to rename this class at some point, we won’t
# have to remember to update the constructor name in all of the factory functions.

# Now, what can we do with these factory methods? Let’s try them out:

BetterPizza.margherita()
# Pizza(['mozzarella', 'tomatoes'])
BetterPizza.prosciutto()
# Pizza(['mozzarella', 'tomatoes', 'ham'])

# As you can see, we can use the factory functions to create new Pizza
# objects that are configured just the way we want them. They all use the
# same __init__ constructor internally and simply provide a shortcut for remembering
# all of the various ingredients.

# Python only allows one __init__ method per class. Using class methods
# makes it possible to add as many alternative constructors as necessary.
# This can make the interface for your classes self-documenting
# (to a certain degree) and simplify their usage.

# When to use static methods:

import math

class PizzaWithStaticMethod:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients
       
    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    defarea(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
p
# Pizza(4, {self.ingredients})
p.area()
# 50.26548245743669
Pizza.circle_area(4)
# 50.26548245743669

# In the above example, it’s clear that circle_area() can’t modify the
# class or the class instance in any way. (Sure, you could always work
# around that with a global variable, but that’s not the point here.)

# Now, why is that useful?

# Flagging a method as a static method is not just a hint that a method
# won’t modify class or instance state. As you’ve seen, this restriction is also enforced by the Python runtime.

# Techniques like that allow you to communicate clearly about parts
# of your class architecture so that new development work is naturally
# guided to happen within these boundaries. Of course, it would be
# easy enough to defy these restrictions. But in practice, they often help
# avoid accidental modifications that go against the original design.



    
