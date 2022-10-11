# Question: Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program: 34,67,55,33,12,98 
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

def list_and_tuple_generator(input_list):
    the_tuple = tuple(input_list)
    print(input_list)
    print(the_tuple)
  
if __name__ == "__main__":
    numbers = input().split(',')
    list_and_tuple_generator(numbers)
