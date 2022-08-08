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
