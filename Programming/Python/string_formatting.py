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
