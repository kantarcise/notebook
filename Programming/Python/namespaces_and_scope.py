# An assignment statement creates a symbolic name that you can use to reference an object. 
# The statement x = 'foo' creates a symbolic name x that refers to the string object 'foo'.

# In a program of any complexity, you’ll create hundreds or thousands of such names, each pointing to a specific object. 
# How does Python keep track of all these names so that they don’t interfere with one another?

# Namespaces

# In a Python program, there are four types of namespaces:

#     Built-In
#     Global
#     Enclosing
#     Local

# These have differing lifetimes. As Python executes a program, it creates namespaces as necessary and deletes them when they’re no longer needed.

# The Built-In Namespace

# The built-in namespace contains the names of all of Python’s built-in objects. These are available at all times when Python is running.


# dir(__builtins__)

# ['ArithmeticError', 'AssertionError', 'AttributeError',
#  'BaseException','BlockingIOError', 'BrokenPipeError', 'BufferError',
#  'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
#  'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError',
#  'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError',
#  'Exception', 'False', 'FileExistsError', 'FileNotFoundError',
#  'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
#  'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
#  'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt',
#  'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None',
#  'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError',
#  'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
#  'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
#  'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration',
#  'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
#  'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
#  'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
#  'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
#  'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__',
#  '__doc__', '__import__', '__loader__', '__name__', '__package__',
#  '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray',
#  'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex',
#  'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
#  'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset',
#  'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input',
#  'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list',
#  'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
#  'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr',
#  'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
#  'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']


# You’ll see some objects here that you may recognize from previous tutorials—for example, the StopIteration exception,
# built-in functions like max() and len(), and object types like int and str.


# The Python interpreter creates the built-in namespace when it starts up. 
# This namespace remains in existence until the interpreter terminates.

def f():
    print('Start f()')
    def g():
        print('Start g()')
        print('End g()')
        return
    g()
    print('End f()')
    return

f()

# Start f()
# Start g()
# End g()
# End f()

# When the main program calls f(), Python creates a new namespace for f(). 
# Similarly, when f() calls g(), g() gets its own separate namespace. The namespace
# created for g() is the local namespace, and the namespace created for f() is the enclosing namespace.

# Each of these namespaces remains in existence until its respective function terminates. 

# For a defined object called x Python will (LEGB):
  
# Local: If you refer to x inside a function, then the interpreter first searches for it in the innermost scope that’s local to that function.
# Enclosing: If x isn’t in the local scope but appears in a function that resides inside another function, then the interpreter searches in the enclosing function’s scope.
# Global: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.
# Built-in: If it can’t find x anywhere else, then the interpreter tries the built-in scope.

# The built-in function globals() returns a reference to the current global namespace dictionary.

globals()['y'] = 100

globals()

# {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None,
# '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
# 'x': 'foo', 'y': 100}

y
# 100

globals()['y'] = 3.14159

y
# 3.14159

# You get the idea.
