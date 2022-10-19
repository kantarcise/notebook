# Question: Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case. 

# Also please include simple test function to test the class methods.

class Stringer:
    def __init__(self):
        self.string = ""

    def __repr__(self):
        return(f'{self.__class__.__name__} class with the string:' f"{self.string!r}")

    def __str__(self):
        return(f'A string printer class')
      
    def getString(self):
        print("Enter your string!")
        self.string = input()
      
    def printString(self):
        print(self.string.upper())
