# In a Python program, the if statement is how you perform this sort of decision-making. 
# It allows for conditional execution of a statement or group of statements based on the value of an expression.

if (weather==nice):
  mow_the_lawn()
  
  
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

x = 20
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

    
name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# Hello Joe

# Conditional expression in a python way

# <expr1> if <conditional_expr> else <expr2> 

raining = False
print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the beach

raining = True
print("Let's go to the", 'beach' if not raining else 'library')
# Let's go to the library




