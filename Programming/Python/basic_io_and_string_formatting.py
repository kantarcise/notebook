# For a program to be useful, it usually needs to communicate
# with the outside world by obtaining input data from the user 
# and displaying result data back to the user. 
# In this tutorial, you’ll learn about Python input and output.

# The input() function pauses program execution to allow the user to type in a line of input
# from the keyboard. Once the user presses the Enter key, all characters typed are read and returned as a string:

user_input = input()
# foo bar baz
user_input
# 'foo bar baz'

name = input("What is your name? ")
# What is your name? Winston Smith
name
# 'Winston Smith'

# input() always returns a string. 

# Writing Output to the Console

first_name = Winston
last_name = Smith

print("Name:", first_name, last_name)
# Name: Winston Smith

# Printing With Advanced Features

# print() takes a few additional arguments 
# that provide modest control over the format of the output. 
# Each of these is a special type of argument called a keyword argument. 

print("foo", 42, "bar", sep="/")
# foo/42/bar

print("foo", 42, "bar", sep="...")
# foo...42...bar

# Default end is a newline but you can:
print("foo", end="/")
# foo/

# The f-string syntax is one of the modern ways of string formatting. 
# The fastest too.
# All you need to do is add the letter f or F at the beginning of your string.

name = input("What is your name? ")
# What is your name? Winston

age = int(input("How old are you? "))
# How old are you? 24

f"Hello, {name}. You are {age}."
# Hello, Winston. You are 24.

important_number = 23
number_of_wins = 7

print(f"The number of wins you have today = {number_of_wins}, #{important_number} would be proud")
