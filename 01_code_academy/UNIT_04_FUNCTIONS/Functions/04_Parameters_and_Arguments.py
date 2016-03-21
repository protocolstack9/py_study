#!/usr/bin/python


"""
Parameters and Arguments

Let's reexamine the first line that defined square in the previous exercise:

def square(n):

n is a parameter of square. A parameter acts as a variable name for a passed in argument. With the previous example, we called square with the argument 10. In this instance the function was called, n holds the value 10.

A function can require as many parameters as you'd like, but when you call the function, you should generally pass in a matching number of arguments.
"""

def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!
