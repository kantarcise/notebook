# Dictionary Tricks

# Python’s dictionaries have a get() method for looking up a key while
# providing a fallback value. This can be handy in many situations. Let
# me give you a simple example to show you what I mean. Imagine
# we have the following data structure that’s mapping user IDs to user names:

name_for_userid = {
   382: 'Alice',
   950: 'Bob',
   590: 'Dilbert',
}

def greeting(userid):
    return ('Hi %s!' % name_for_userid[userid])
  
# Looks cool right? 

# LOL NO

greeting(382)
# 'Hi Alice!'
greeting(33333333)
# KeyError: 33333333

# We can cover our back with a condition?

def greeting(userid):
    if userid in name_for_userid:
        return 'Hi %s!' % name_for_userid[userid]
    else:
        return 'Hi there!'


# But there’s still room for improvement. While this new implementation
# gives us the expected results and seems small and clean enough, it
# can still be improved. I’ve got some gripes with the current approach:

# 1) It’s inefficient because it queries the dictionary twice.
# 2) It’s verbose since part of the greeting string is repeated, for example.
# 3) It’s not Pythonic—the official Python documentation specifically
# recommends an “easier to ask for forgiveness than
# permission” (EAFP) coding style for these situations:

# “This common Python coding style assumes the existence
# of valid keys or attributes and catches exceptions
# if the assumption proves false.”

# We can do a try catch ?

def greeting(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there'

# But we can still improve this further and come up with a cleaner solution.
# Python’s dictionaries have a get() method on them which supports
# a “default” parameter that can be used as a fallback value.

def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')

greeting(950)
# 'Hi Bob!'
greeting(333333)
# 'Hi there!'
  
# Key Takeaways
# • Avoid explicit key in dict checks when testing for membership.
# • EAFP-style exception handling or using the built-in get()
# method is preferable.
# • In some cases, the collections.defaultdict class from the
# standard library can also be helpful.




