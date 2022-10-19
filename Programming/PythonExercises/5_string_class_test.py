# Question: Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case. 

# Also please include simple test function to test the class methods.

import unittest

from 5_string_class import Stringer 

class TestStringer(unittest.TestCase):

    def test_getString(self):
        string_object = Stringer()
        string_object.getString()
        # self.assertTrue(c.apple.consumed, "Expected apple to be consumed")

    def test_printString(self):
        string_object = Stringer()
        string_object.printString()
        # self.assertEquals(c.apple, food, "Expected apple to have been picked")

if __name__ == '__main__':
    unittest.main()
