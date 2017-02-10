# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""
import sys
import unittest  # this makes Python unittest module available

def inputCheck():
    firstInput = input("input the first side (A)")
    secondInput = input("input the first side (B)")
    thirdInput = input("input the first side (C)")

    # Check if the input is only the valid type (Numbers)
    try:
        sideOne = int(firstInput)
        sideTwo = int(secondInput)
        sideThree = int(thirdInput)
        print(classifyTriangle(sideOne, sideTwo, sideThree))

    except ValueError:
        print("That is not an int, the inputs are wrong!")
        return 'Wrong Input'


def classifyTriangle(a, b, c):
    """

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'


      BEWARE: there may be a bug or two in this code

    """
    # require that the input values be > 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput';

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    elif ((a * a) + (b * b)) == (c * c):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isoceles'


def runClassifyTriangle(a, b, c):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifyTriangle(a, b, c))


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testClassifyTriangle1(self):  # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testClassifyTriangle2(self):
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', 'Should be Equilateral')
        self.assertEqual(classifyTriangle(10, 15, 30), 'NotATriangle', 'Should be NotATriangle')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', 'Should be NotATriangle')
        self.assertEqual(classifyTriangle(-1, -2, 5), 'InvalidInput', 'Should be NotATriangle')
        self.assertEqual(classifyTriangle(1000, 2, 5), 'InvalidInput', 'Should be NotATriangle')

    def testClassifyTriangleRight(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', 'Should be Right')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', 'Should be Right')
        self.assertEqual(classifyTriangle(7, 24, 25), 'Right', 'Should be Right')
        self.assertEqual(classifyTriangle(65, 72, 97), 'Right', 'Should be Right')

    def testClassifyTriangleEquilateral(self):
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', 'Should be Equilateral')
        self.assertEqual(classifyTriangle(5, 5, 5), 'Equilateral', 'Should be Equilateral')
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', 'Should be Equilateral')

    def testClassifyTriangleScalene(self):
        self.assertEqual(classifyTriangle(36, 67, 32), 'Scalene', 'Should be Scalene')
        self.assertEqual(classifyTriangle(199, 198, 2), 'Scalene', 'Should be Scalene')

    def testClassifyTriangleIsoceles(self):
        self.assertEqual(classifyTriangle(1, 100, 100), 'Isoceles', 'Should be Isoceles')
        self.assertEqual(classifyTriangle(100, 1, 100), 'Isoceles', 'Should be Isoceles')
        self.assertEqual(classifyTriangle(100, 100, 1), 'Isoceles', 'Should be Isoceles')
        self.assertEqual(classifyTriangle(5, 5, 1), 'Isoceles', 'Should be Isoceles')

    # Testing the inputs
    def testWrongInput(self):
        original_input = __builtins__.input
        __builtins__.input = lambda _: 'a' # The input is character For that the code should handle it and return wrong input
        self.assertEqual(inputCheck(), 'Wrong Input')
        __builtins__.input = original_input



if __name__ == '__main__':
    # examples of running the  code
    # inputs examples: 1,2,3    1,1,1     3,4,5
    inputCheck()

    print('Begin UnitTest')
    unittest.main(exit=False)  # this runs all of the tests - use this line if running from Spyder
    # unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
