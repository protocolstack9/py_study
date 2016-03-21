#!/usr/bin/python

"""
Function Imports
Nice work! Now Python knows how to take the square root of a number.

However, we only really needed the sqrt function, and it can be frustrating to have to keep typing math.sqrt().

It's possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it's done with the from keyword:

from module import function
Now you can just type sqrt() to get the square root of a number no more math.sqrt()!
"""

from math import sqrt

print sqrt(25)
