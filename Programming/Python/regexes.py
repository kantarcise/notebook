# Rather than searching for a fixed substring like '123', 
# suppose you wanted to determine whether a string contains any three consecutive
# decimal digit characters, as in the strings 'foo123bar', 'foo456bar', '234baz', and 'qux678'.

# Strict character comparisons won’t cut it here. This is where regexes in Python come to the rescue.

# Regex functionality in Python resides in a module named re.

re.search(<regex>, <string>)

# Scans a string for a regex match.

# from re import search
# search(...)

s = 'foo123bar'

# One last reminder to import!
import re

re.search('123', s)
# <_sre.SRE_Match object; span=(3, 6), match='123'>

# kinda like find() so far, here comes the good part

# Consider again the problem of how to determine whether a string contains any three consecutive decimal digit characters.

# In a regex, a set of characters specified in square brackets ([]) makes up a character class. 
# This metacharacter sequence matches any single character that is in the class, as demonstrated in the following example:

re.search('[0-9][0-9][0-9]', 'foo456bar')
# <_sre.SRE_Match object; span=(3, 6), match='456'>

re.search('[0-9][0-9][0-9]', '234baz')
# <_sre.SRE_Match object; span=(0, 3), match='234'>

re.search('[0-9][0-9][0-9]', 'qux678')
# <_sre.SRE_Match object; span=(3, 6), match='678'>


# The dot (.) metacharacter matches any character except a newline, so it functions like a wildcard

s = 'foo123bar'
re.search('1.3', s)
# <_sre.SRE_Match object; span=(3, 6), match='123'>

s = 'foo13bar'
print(re.search('1.3', s))
# None








