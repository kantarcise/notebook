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
