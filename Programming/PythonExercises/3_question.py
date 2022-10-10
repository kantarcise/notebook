# Question: With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included). 
# Then the program should print the dictionary. 

# Suppose the following input is supplied to the program: 8 
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# For a dictionary, the .keys and .values functions are read only.
# dict.update is a method, not a variable you can assign a value to. 

def run(n):
    
    _the_dict = {}
    for counter in range(1,n+1):
        _the_dict.update({ f"{counter}": counter * counter})
    
    print(_the_dict)
  
if __name__ == "__main__":
    x = int(input())
    run(x)
