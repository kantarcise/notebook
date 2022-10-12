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

