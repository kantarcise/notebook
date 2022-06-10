
# Variable assignment

a = b = c = 300

# Can print them all

# A Python variable is a symbolic name that is a reference or pointer to an object. 
# Once an object is assigned to a variable, you can refer to the object by that name. 
# But the data itself is still contained within the object.


var = 23.5
print(var)
# 23.5

var = "Now I'm a string"
print(var)
# Now I'm a string

print(300)
# 300

type(300)
# <class 'int'>


# Object Identity

# The built-in Python function id() returns an object’s integer identifier.
# Using the id() function, you can verify that two variables indeed point to the same object.

n = 300
m = n 

id(n)
# 60127840

id(m)
# 60127840

m = 400
id(m)
# 60127872

# Deep Dive: Caching Small Integer Values


# For purposes of optimization, the interpreter creates objects for the integers in 
# the range [-5, 256] at startup, and then reuses them during program execution.
# Thus, when you assign separate variables to an integer value
# in this range, they will actually reference the same object.

m = 300
n = 300
id(m)
# 60062304

id(n)
# 60062896


m = 30
n = 30
id(m)
# 1405569120
id(n)
# 1405569120


# Reserved Keywords

# There is one more restriction on identifier names. 
# The Python language reserves a small set of keywords that designate special 
# language functionality. No object can have the same name as a reserved word.

# 33 of them:

# False 	  def 	    if 	      raise
# None 	    del 	    import 	  return
# True 	    elif 	    in 	      try
# and 	    else 	    is 	      while
# as 	      except 	  lambda 	  with
# assert 	  finally 	nonlocal 	yield
# break 	  for 	    not 	
# class 	  from 	    or 	
# continue 	global 	  pass 	
