# Question: 

# Write a program which will find all such numbers which
# are divisible by 7 but are not a multiple of 5, between 
# 2000 and 3200 (both included). The numbers obtained should
# be printed in a comma-separated sequence on a single line.

# List Comprehension
#  newlist = [expression for item in iterable if condition == True] 

def run():
    list__ = [x for x in range(2000,3200) if x%7 == 0 and x%5 != 0 ]
    
    # This will print brackets aswell, so not true.
    # print(list__)
    
    # This will work
    print(*list__, sep=", ")

if __name__ == "__main__":
    run()
