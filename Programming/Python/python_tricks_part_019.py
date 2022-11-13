# Looping & Iteration

# Writing Pythonic Loops

# One of the easiest ways to spot a developer with a background in C-
# style languages who only recently picked up Python is to look at how they write loops.

my_items = ['a', 'b', 'c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

# In Python you can write loops that handle both of these responsibilities 
#  automatically. It’s a great idea to take advantage of that. For example,
# it’s much harder to write accidental infinite loops if your code
# doesn’t have to keep track of a running index. It also makes the code
# more concise and therefore more readable.

# The range type represents an immutable sequence of numbers. Its
# advantage over a regular list is that it always takes the same small
# amount of memory. Range objects don’t actually store the individual
# values representing the number sequence—instead, they function as
# iterators and calculate the sequence values on the fly. So, rather than
# incrementing i manually on each loop iteration, we could take advantage 
# of the range() function and write something like this:

for i in range(len(my_items)):
    print(my_items[i])
    
# As I mentioned, in Python, for-loops are really “for-each” loops that
# can iterate directly over items from a container or sequence, without
# having to look them up by index. I can use this to simplify this loop even more:

for item in my_items:
    print(item)
    
# With indexes

for i, item in enumerate(my_items):
    print(f'{i}: {item}')

# 0: a
# 1: b
# 2: c

# same with dictionaries:

emails = { 'Bob': 'bob@example.com',
           'Alice': 'alice@example.com',
         }

for name, email in emails.items():
    print(f'{name} -> {email}')
    
# 'Bob -> bob@example.com'
# 'Alice -> alice@example.com'
