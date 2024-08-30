# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'add' functions from the 'mymodule' module.
from mymodule import add

# Define a test case class for testing the 'add' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestAdd(unittest.TestCase): 

    # Define the first test method for the 'add' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'add(2, 4)' returns 6.
        self.assertEqual(add(2, 4), 6)

        # Check that calling 'add(0, 0)' returns 0.
        self.assertEqual(add(0, 0), 0)

        # Check that calling 'add(2.3, 3.6)' returns 5.9.
        self.assertEqual(add(2.3, 3.6), 5.9) 

        # Check that calling 'add("hello", "world")' returns "helloworld".
        self.assertEqual(add("hello", "world"), "helloworld")

        # Check that calling 'add(2.3000, 4.300)' returns 6.6.
        self.assertEqual(add(2.3000, 4.300), 6.6) 

        # Check that calling 'add(-2, -2)' not returns 0.
        self.assertNotEqual(add(-2, -2), 0) 

unittest.main()
