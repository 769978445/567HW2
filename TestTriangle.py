# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')


    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(11, 11, 11), 'Equilateral','11,11,11 should be equilateral')

    def testIsocelesTrianglesA(self):
        self.assertEqual(classifyTriangle(6, 6, 5), 'Isoceles','6, 6, 5 should be Isoceles')

    def testIsocelesTrianglesB(self):
        self.assertEqual(classifyTriangle(12, 13, 12), 'Isoceles','12, 13, 12 should be Isoceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(12, 8, 13), 'Scalene','12, 8, 13 should be Scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(17, 11, 13), 'Scalene','17, 11, 13 should be Scalene')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle','1, 2, 3 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(15, 7, 7), 'NotATriangle','15, 7, 7 is not a triangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(6, 3, 3), 'NotATriangle','6, 3, 3 is not a triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(2,False,2), 'InvalidInput','2,False,2 is an invalid input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(-1, -2, -1), 'InvalidInput','-1, -2, -1 is an invalid input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

