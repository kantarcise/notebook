# Question: 

# Write a program which can compute the factorial of
# a given numbers. The results should be printed in a comma-separated
# sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320


def recursive_factorial(number):
    if number == 0:
        return 1 
    return number * recursive_factorial(number - 1)

if __name__ == "__main__":

    x=int(input())
    print(recursive_factorial(x))
