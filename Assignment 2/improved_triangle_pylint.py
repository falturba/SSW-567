# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.
Note that this code includes intentional errors for you to find.
@author: jrr
"""
import unittest     # this makes Python unittest module available

def classify_triangle(side1, side2, side3):
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
    return_string = ""
    # require that the input values be > 0 and <= 200
    if side1 > 200 or side2 > 200 or side3 > 200:
        return_string = 'InvalidInput'

    elif side1 <= 0 or side2 <= 0 or side3 <= 0:
        return_string = 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    elif not (isinstance(side1, int) and isinstance(side2, int) and isinstance(side3, int)):
        return_string = 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    elif (side1 >= (side2 + side3)) or (side2 >= (side1 + side3)) or (side3 >= (side1 + side2)):
        return_string = 'NotATriangle'

    # now we know that we have a valid triangle
    elif side1 == side2 and side2 == side3:
        return_string = 'Equilateral'
    elif ((side1 * side1) + (side2 * side2)) == (side3 * side3):
        return_string = 'Right'
    elif (side1 != side2) and (side2 != side3) and (side1 != side3):
        return_string = 'Scalene'
    else:
        return_string = 'Isoceles'
    return return_string
def run_classify_triangle(side1, side2, side3):
    """ invoke buggyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', side1, ',', side2, ',', side3, ')=',
          classify_triangle(side1, side2, side3))

# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """Triangle Test Case"""
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def test_classify_triangle1(self): # test invalid inputs
        """From Professor's TestCase"""
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_invalid_inputs(self):
        """Test Invalid and Not Triangle"""
        self.assertEqual(classify_triangle(0, 0, 0), 'InvalidInput', 'Should be NotATriangle')
        self.assertEqual(classify_triangle(-1, -2, 5), 'InvalidInput', 'Should be NotATriangle')
        self.assertEqual(classify_triangle(1000, 2, 5), 'InvalidInput', 'Should be NotATriangle')
        self.assertEqual(classify_triangle(10, 15, 30), 'NotATriangle', 'Should be NotATriangle')

    def test_classify_triangle_right(self):
        """Test Right Triangle"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', 'Should be Right')
        self.assertEqual(classify_triangle(5, 12, 13), 'Right', 'Should be Right')
        self.assertEqual(classify_triangle(7, 24, 25), 'Right', 'Should be Right')
        self.assertEqual(classify_triangle(65, 72, 97), 'Right', 'Should be Right')

    def test_classify_triangle_equil(self):
        """Test Equilateral"""
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral', 'Should be Equilateral')
        self.assertEqual(classify_triangle(200, 200, 200), 'Equilateral', 'Should be Equilateral')
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(10, 10, 10), 'Equilateral', 'Should be Equilateral')

    def test_classify_triangle_scalene(self):
        """Test Scalene"""
        self.assertEqual(classify_triangle(36, 67, 32), 'Scalene', 'Should be Scalene')
        self.assertEqual(classify_triangle(199, 198, 2), 'Scalene', 'Should be Scalene')

    def test_classify_triangle_isoceles(self):
        """Test Isoceles"""
        self.assertEqual(classify_triangle(1, 100, 100), 'Isoceles', 'Should be Isoceles')
        self.assertEqual(classify_triangle(100, 1, 100), 'Isoceles', 'Should be Isoceles')
        self.assertEqual(classify_triangle(100, 100, 1), 'Isoceles', 'Should be Isoceles')


if __name__ == '__main__':
    # examples of running the  code
    run_classify_triangle(1, 2, 3)
    run_classify_triangle(1, 1, 1)
    run_classify_triangle(3, 4, 5)
    print 'Begin UnitTest'
    # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=False)
    # this runs all of the tests - use this line if running from the command line
    # unittest.main(exit=True)
