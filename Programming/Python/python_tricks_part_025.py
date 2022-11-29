# Iterator Chains

# Here is a cool thing you can do with generators:

# Let's define 2 of them

integers = range(8)
# [1, 2, 3, 4, 5, 6, 7, 8]
squared = (i * i for i in integers)
# [1, 4, 9, 16, 25, 36, 49, 64]
negated = (-i for i in squared)
# [-1, -4, -9, -16, -25, -36, -49, -64]

negated
# <generator object <genexpr> at 0x1098bcb48>
list(negated)
# [0, -1, -4, -9, -16, -25, -36, -49]


# --------------
# Real world example

# One of the most popular example of using the generator function is to read a large text file.


def read_file(file_name):
    text_file = open(file_name, 'r')
    line_list = text_file.readlines()
    text_file.close()
    return line_list

def read_file_yield(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline()
        if not line_data:
            text_file.close()
            break
        yield line_data
        
# If you print a changing file size and memory usage you'll see:

# File size     |          Return Statement        |               Generator               |
# 26 MB	        |   Memory: 392.8 MB, Time: 27.03s | 	   Memory: 5.52 MB, Time: 29.61s     |
# 263 MB	      |   Memory: 3.65 GB, Time: 273.56s |	   Memory: 5.55 MB, Time: 292.99s    |

# So the generator function is taking slightly extra time than the return statement. 
# It’s obvious because it has to keep track of the function state in every iterator next() call.

# But, with the yield keyword the memory benefits are enormous. The memory
# usage is directly proportional to the file size with the return statement.
# It’s almost constant with the generator function.


# Key Takeaways

# • Generators can be chained together to form highly efficient and
# maintainable data processing pipelines.
# • Chained generators process each element going through the
# chain individually.
# • Generator expressions can be used to write concise pipeline 
# definitions, but this can impact readability
