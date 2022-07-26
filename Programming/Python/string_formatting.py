# string formatting can be helpful with a lot of different use cases

# In general it looks like:
#  <template>.format(<positional_argument(s)>, <keyword_argument(s)>)

print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))
# 6 bananas cost $1.74

# Starting with Python 3.1, you can omit the numbers in the replacement fields, in 
# which case the interpreter assumes sequential order. This is referred to as automatic field numbering:

print('{}/{}/{}'.format('foo', 'bar', 'baz'))
# 'foo/bar/baz'

# Keyword Arguments
# Keyword arguments are inserted into the template string in place of keyword replacement fields with the same name:

'{x}/{y}/{z}'.format(x='foo', y='bar', z='baz')
# 'foo/bar/baz'


# We can use this formatting for lists and dictionaries.

a = ['foo', 'bar', 'baz']
'{0[0]}, {0[2]}'.format(a)
# 'foo, baz'
'{my_list[0]}, {my_list[2]}'.format(my_list=a)
# 'foo, baz'

d = {'key1': 'foo', 'key2': 'bar'}
d['key1']
# 'foo'
'{0[key1]}'.format(d)
# 'foo'
d['key2']
# 'bar'
'{my_dict[key2]}'.format(my_dict=d)
# 'bar'


# Attributes of objects aswell.

z = 3 + 5j
type(z)
# <class 'complex'>
z.real
# 3.0
z.imag
# 5.0

z
# (3+5j)
'real = {0.real}, imag = {0.imag}'.format(z)
# 'real = 3.0, imag = 5.0'

# A value using the less than sign (<) indicates that the output is left-justified:

'{0:<8s}'.format('foo')
# 'foo     '
'{0:<8d}'.format(123)
# '123     '

# This behavior is the default for string values.

""""""

# A value using the greater than sign (>) indicates that the output should be right-justified:

'{0:>8s}'.format('foo')
# '     foo'
'{0:>8d}'.format(123)
# '     123'

# This behavior is the default for numeric values.

# A value using a caret (^) indicates that the output should be centered in the output field:

'{0:^8s}'.format('foo')
# '  foo   '
'{0:^8d}'.format(123)
# '  123   '

# You can also fill in a print formatting
'{0:*^8s}'.format('foo')
# '**foo***' 

# f strings - all you really need

# The magic of f-strings is that you can embed Python expressions directly inside them. Any portion of
# an f-string that’s enclosed in curly braces ({}) is treated as an 
# expression. The expression is evaluated and converted to string representation, and
# the result is interpolated into the original string in that location:

s = 'bar'
print(f'foo\n{s}\nbaz')
# foo
# bar
# baz

# About all the things you can do with f strings:

# Indexing, slicing, and key references:

a = ['foo', 'bar', 'baz']
d = {'foo': 1, 'bar': 2}

print(f'First item in list a = {a[0]}')
# First item in list a = foo

print(f'Last two items in list a = {a[-2:]}')
# Last two items in list a = ['bar', 'baz']

print(f'List a reversed = {a[::-1]}')
# List a reversed = ['baz', 'bar', 'foo']

print(f"Dict value for key 'bar' is {d['bar']}")
# Dict value for key 'bar' is 2


# Function and method calls:

a = ['foo', 'bar', 'baz', 'qux', 'quux']
print(f'List a has {len(a)} items')
# List a has 5 items

s = 'foobar'
f'--- {s.upper()} ---'
# '--- FOOBAR ---'

d = {'foo': 1, 'bar': 2}
print(f"Dict value for key 'bar' is {d.get('bar')}")
# Dict value for key 'bar' is 2

# Conditional expressions:

x = 3
y = 7
print(f'The larger of {x} and {y} is {x if x > y else y}')
# The larger of 3 and 7 is 7

age = 13
f'I am {"a minor" if age < 18 else "an adult"}.'
# 'I am a minor.'

# Object attributes:

z = 3+5j
z
# (3+5j)

print(f'real = {z.real}, imag = {z.imag}')
# real = 3.0, imag = 5.0

